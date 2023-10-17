#!/bin/python3

import json
import os
import subprocess
import time
from threading import Thread


class Zgrab2Config:
    path = ""
    verbose = False
    json = False


class Zgrab2:
    def __init__(self, target):
        self.tasks = []
        self.path = Zgrab2Config.path
        self.target = target.encode()
        self.verbose = Zgrab2Config.verbose

        self.modules = [
            Zgrab2Module('bacnet', self),
            Zgrab2Module('banner', self),
            Zgrab2Module('dnp3', self),
            Zgrab2Module('fox', self),
            Zgrab2Module('ftp', self),
            HttpModule(self, max_redirects=5),
            Zgrab2Module('imap', self),
            Zgrab2Module('ipp', self),
            Zgrab2Module('modbus', self),
            Zgrab2Module('mongodb', self),
            Zgrab2Module('mssql', self),
            Zgrab2Module('mysql', self),
            Zgrab2Module('ntp', self),
            Zgrab2Module('oracle', self),
            Zgrab2Module('pop3', self),
            Zgrab2Module('postgres', self),
            Zgrab2Module('redis', self),
            Zgrab2Module('siemens', self),
            Zgrab2Module('smb', self),
            Zgrab2Module('smtp', self),
            Zgrab2Module('ssh', self),
            Zgrab2Module('telnet', self),
            Zgrab2Module('tls', self)
        ]

    def start_scan(self) -> None:
        """Startet alle Module in einem eigenen Thread"""
        self.stop_scan()
        for module in self.modules:
            task = Thread(target=module.run)
            self.tasks.append(task)
            task.setName(module.command)
            task.start()

    def stop_scan(self) -> None:
        """Stoppt alle Module"""
        for task in self.tasks:
            task.terminate()
        self.tasks = []

    def scan(self) -> list:
        """Führt einen Scan aus und gibt eine Liste von Zgrab2Result Objekten zurück.
        Wrapper für start_scan und get_results"""
        self.start_scan()
        count_running, count_total = self.get_count_running()

        if self.verbose:
            print("Scanning...", end="", flush=True)
            count_done = count_total - count_running
            print(f'{count_done}/{count_total}', flush=True)

        while self.is_running():
            time.sleep(1)

            if self.verbose:
                print(".", end="", flush=True)

            if count_running < self.get_count_running()[0]:
                count_running = self.get_count_running()[0]
                count_done = count_total - count_running
                if self.verbose:
                    print(f'{count_done}/{count_total}', flush=True)

        if self.verbose:
            print("Done")

        return self.get_results()

    def is_running(self) -> bool:
        """Gibt True zurück, wenn noch mindestens ein Thread läuft"""
        for task in self.tasks:
            if task.is_alive():
                return True
        return False

    def get_status_by_name(self) -> dict:
        """Gibt ein Dictionary mit den Namen der Module und deren Status zurück
        Status kann "running" oder "completed" sein"""
        status = {}
        for task in self.tasks:
            status[task.getName()] = "running" if task.is_alive() else "completed"
        return status

    def get_count_running(self) -> (int, int):
        """Gibt ein Tupel mit den abgeschlossenen und der gesamten Anzahl an Modulen zurück"""
        count_done = 0
        for task in self.tasks:
            if task.is_alive():
                count_done += 1
        return count_done, len(self.tasks)

    def get_results(self) -> list:
        """Gibt eine Liste von Zgrab2Result Objekten zurück"""
        if self.is_running():
            return []
        results = []
        for module in self.modules:
            results.append(Zgrab2Result(module))
        return results

    def clear_results(self) -> None:
        """Löscht die Ergebnisdateien des Scans"""
        for module in self.modules:
            file_path = f'outputs/{self.target.decode("utf8")}/{module.command}.inf'
            if os.path.exists(file_path):
                os.remove(file_path)
        os.removedirs(f'outputs/{self.target.decode("utf8")}')


# Base class der Zgrab2 Module
class Zgrab2Module:
    def __init__(self, command, zgrab2: Zgrab2):
        self.zgrab2 = zgrab2
        self.command = command

    # Führt das Modul aus, speichert die Ergebnisse in outputs/<target>/<command>.inf
    # legt den Ordner outputs/<target> an, falls er noch nicht existiert
    def run(self, args=None):
        """Führt das Modul aus und speichert die Ergebnisse in outputs/<target>/<command>.inf
        legt den Ordner outputs/<target> an, falls er noch nicht existiert"""
        if args is None:
            args = []

        output_dir = f'outputs/{self.zgrab2.target.decode("utf8")}'
        file_path = f'{output_dir}/{self.command}.inf'
        subprocess_args = [Zgrab2Config.path, self.command,
                           '-o', file_path]
        subprocess_args.extend(args)

        subprocess.run(['mkdir', '-p', output_dir])
        subprocess.run(subprocess_args, input=self.zgrab2.target,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


class HttpModule(Zgrab2Module):
    """HTTP Module, da es den max-redirects Parameter braucht"""

    def __init__(self, zgrab2: Zgrab2, max_redirects=5):
        super().__init__('http', zgrab2)
        self.max_redirects = max_redirects

    def run(self, args=None):
        args = []
        if self.max_redirects > 0:
            args.append(f'--max-redirects={self.max_redirects}')
        super().run(args)


# Auswertung der Ergebnisse eines Zgrab2 Moduls
class Zgrab2Result:

    def __init__(self, module: Zgrab2Module):
        """Liest die Ergebnisse aus der Datei outputs/<target>/<command>.inf
        und speichert sie in self.results_dict
        self.results_dict ist ein Dictionary mit den Status als Key und der Anzahl als Value
        self.successful ist eine Liste mit den IPs/Domains, die einen Status von "success" haben"""
        self.output_dir = f'outputs/{module.zgrab2.target.decode("utf8")}'
        self.command = module.command
        self.results_dict: dict = {}
        self.command: str
        self.successful = []

        file_path = f'{self.output_dir}/{self.command}.inf'

        if not os.path.exists(file_path):
            return

        with open(file_path, 'r') as f:
            lines = f.readlines()
            if len(lines) > 0:
                for line in lines:
                    json_object = json.loads(line)
                    data = json_object['data']
                    command_data = data[self.command]
                    status = command_data['status']

                    if status in self.results_dict.keys():
                        self.results_dict[status] += 1
                    else:
                        self.results_dict[status] = 1

                    if status == 'success':
                        if 'ip' in json_object.keys():
                            self.successful.append(json_object['ip'])
                        elif 'domain' in json_object.keys():
                            self.successful.append(json_object['domain'])
