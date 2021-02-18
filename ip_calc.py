import sys
import ipaddress as ip

class bcolors:
    ENDC = '\033[0m'
    WARNING = '\033[93m'

net = ip.IPv4Network(sys.argv[1], False)

host = list(net.hosts())
isGlobal = False
if net.is_global == True:
    isGlobal = True

print(
    f'|-----------------------------------------------------------|\n'
    f'|     Network              |     {net}            |\n'
    f'|     Netmask              |     {net.netmask}              |\n'
    f'|     {bcolors.WARNING}First host           |     {host[0]}{bcolors.ENDC}               |\n'
    f'|     {bcolors.WARNING}Last host            |     {host[-1]}{bcolors.ENDC}             |\n'
    f'|     Broadcast            |     {net.broadcast_address}             |    \n'
    f'|  Quantity avalible hosts |     {net.num_addresses - 2}                        |\n'
    f'|     Public               |     {isGlobal}                      |\n'
    f'|-----------------------------------------------------------|\n'
)