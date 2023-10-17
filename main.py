#!/bin/python3

import argparse
import json

import helpers.printer as printer
from modules.zgrab2 import Zgrab2, Zgrab2Config


def scan(target):
    zgrab2 = Zgrab2(target)

    results = zgrab2.scan()

    if Zgrab2Config.json:
        json_string = json.dumps(results,
                                 default=lambda obj: obj.__dict__
                                 if not hasattr(obj, 'output_dir') else {key: value for
                                                                         key, value in
                                                                         obj.__dict__.items()
                                                                         if
                                                                         key != 'output_dir'})

        print(json_string)
        exit(0)

    for result in results:
        print(result.command)
        printer.print_dict(result.results_dict)
        printer.print_list(result.successful)


def delete(target):
    zgrab2 = Zgrab2(target)
    zgrab2.clear_results()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scans domain/ips using zgrab2, tested protocols are: bacnet, banner, dnp3, fox, ftp, http, imap, "
                    "ipp, modbus, mongodb, mssql, mysql, ntp, oracle, pop3, postgres, redis, siemens, smb, smtp, ssh, "
                    "telnet, tls")

    parser.add_argument("-d", '--delete', action="store_true", help="Delete")
    parser.add_argument("target", help="Target domain or ip e.g. google.com or x.x.x.x[/x]")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose")
    parser.add_argument("-j", "--json", action="store_true", help="output as json")

    args = parser.parse_args()

    if args.delete:
        delete(args.target)
        exit(0)

    Zgrab2Config.path = r'./zgrab2/zgrab2'

    if args.verbose:
        Zgrab2Config.verbose = True

    if args.json:
        Zgrab2Config.json = True

    scan(args.target)
