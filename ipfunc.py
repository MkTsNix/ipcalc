import ipaddress as ip
from color import bcolors

def calc(ipaddr):
    '''
    Function calculate Netmask, First/Last host, Broadcast etc
    :param ipaddr: take from argv,
    :return: nothing, only print information
    '''
    net = ip.IPv4Network(ipaddr, False)
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

def startMsg():
    print(f'{bcolors.OKBLUE}\n'
          f'Usage: ip_calc.py [OPTIONS] COMMAND\n'
          f'\n'
          f'Options:\n'
          f'\t-h \t\t\t\t Run ip_calc.py for more information\n'
          f'\t-c [xxx.xxx.xxx.xxx/xx] \t Сalculate Network{bcolors.ENDC}')

def helpMsg():
    print(f'{bcolors.OKBLUE}'
          f'\n'
          f'This application can help you quickly calculate network size\n'
          f'Example:\n'
          f'\t ./ip_calc.py -c 192.168.0.0/24\n'
          f'\t or \n'
          f'\t python3 ip_calc.py -c 192.168.0.0/24{bcolors.ENDC}\n')