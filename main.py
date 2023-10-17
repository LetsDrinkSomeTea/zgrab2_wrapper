import sys
import time

import helpers.printer as printer
from modules.zgrab2 import Zgrab2, Zgrab2Config


def main(target):
    zgrab2 = Zgrab2(target, verbose=True)

    zgrab2.start_scan()
    while zgrab2.is_running():
        time.sleep(1)
        printer.print_dict(zgrab2.get_status())

    for result in zgrab2.get_results():
        print(result.command)
        printer.print_dict(result.results_dict)
        printer.print_list(result.successful)


if __name__ == "__main__":
    if sys.argv[1] == '-h':
        print("Usage: python3 main.py <zgrab2_path> <target>")
        exit(1)

    if sys.argv[1] == 'init':
        Zgrab2Config.init()
        exit(1)

    Zgrab2Config.path = r'/home/kali/Desktop/zgrab2_wrapper/zgrab2/pkg/mod/github.com/zmap/zgrab2@v0.1.7/cmd/zgrab2/zgrab2'

    if len(sys.argv) == 3:
        Zgrab2Config.path = sys.argv[2]

    if len(sys.argv) >= 2:
        target = sys.argv[1]

    if len(sys.argv) == 1:
        target = input('intput target: ')

    main(target)