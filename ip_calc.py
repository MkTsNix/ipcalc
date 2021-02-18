import sys
import ipaddress as ip

# net = ip.IPv4Network('192.168.24.0/24')
# net = ip.IPv4Network(input('Input network: '))

net = ip.IPv4Network(sys.argv[1])

host = list(net.hosts())
isGlobal = False
if net.is_global == True:
    isGlobal = True

print(f'Network:        {net}\n'
      f'Mask:           {net.netmask}\n'
      f'Quantity:       {net.num_addresses}\n'
      f'First host:     {host[0]}\n'
      f'Last host:      {host[-1]}\n'
      f'Broadcast:      {net.broadcast_address}\n'
      f'Public:         {isGlobal}')
