#!/usr/bin/python3
import sys
import ipaddress as ip

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) < 2:
    print(f'{bcolors.FAIL}ERROR: Please input network with prefix{bcolors.ENDC}\n'
          f'{bcolors.OKBLUE}Example: ./ip_calc.py 192.168.0.0/24 or python3 ip_calc.py 192.168.0.0/24{bcolors.ENDC}')
    sys.exit(1)


net = ip.IPv4Network(sys.argv[1], False)


host = list(net.hosts())
isGlobal = False
if net.is_global == True:
    isGlobal = True

print(
    f'|-----------------------------------------------------------|\n'
    f'     Network              |     {net}\n'
    f'     Netmask              |     {net.netmask}\n'
    f'     {bcolors.WARNING}First host{bcolors.ENDC}           |     {bcolors.WARNING}{host[0]}{bcolors.ENDC}\n'
    f'     {bcolors.WARNING}Last host{bcolors.ENDC}            |     {bcolors.WARNING}{host[-1]}{bcolors.ENDC}\n'
    f'     Broadcast            |     {net.broadcast_address}\n'
    f'  Quantity avalible hosts |     {net.num_addresses - 2}\n'
    f'     Public               |     {isGlobal}\n'
    f'|-----------------------------------------------------------|\n'
)