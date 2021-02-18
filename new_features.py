import sys
import ipaddress as ip

# net = ip.IPv4Network('192.168.24.0/24', False)

net = ip.IPv4Network(sys.argv[1], False)

host = list(net.hosts())
isGlobal = False
if net.is_global == True:
    isGlobal = True


print(
    f'|-----------------------------------------------------------|\n'
    f'|     Network              |     {net}            |\n'
    f'|     Netmask              |     {net.netmask}              |\n' 
    f'|  Quantity avalible hosts |     {net.num_addresses - 2}                        |\n'
    f'|     First host           |     {host[0]}               |\n'
    f'|     Last host            |     {host[-1]}             |\n'
    f'|     Broadcast            |     {net.broadcast_address}             |    \n'
    f'|     Public               |     {isGlobal}                      |\n'
    f'|-----------------------------------------------------------|\n'
)
