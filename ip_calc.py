#!/usr/bin/python3
import sys
import ipaddress as ip
import ipfunc
from color import bcolors

if len(sys.argv) < 2:
    ipfunc.startMsg()
    sys.exit(1)


if sys.argv[1] == '-h':
    ipfunc.helpMsg()
elif sys.argv[1] == '-c':
    if len(sys.argv) < 3:
        ipfunc.helpMsg()
        sys.exit(1)
    try:
        ipfunc.calc(sys.argv[2])
    except ip.AddressValueError:
        print(f'{bcolors.FAIL}Please input network with prefix or use help -h{bcolors.ENDC}')