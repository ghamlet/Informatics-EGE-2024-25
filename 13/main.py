from ipaddress import  *

net = ip_network("218.194.82.148/255.255.255.192", 0)
mask = net.netmask  # маска сети
number_hosts = net.num_addresses  # количество узлов

net_addr = net.network_address  # адрес сети
net_addr_v2 = net[0]

min_ip_uzel = net[1]
max_ip_uzel = net[-2]

broadcast_ip = net[-1] # широковещательный адрес
broadcast_ip_v2 = net.broadcast_address


# перебор всех айпи из сети
for ip in net:
    ip2 = f"{ip:b}"
    ip_bin = bin(int(ip))[2:].zfill(32)

# перебор узлов сети
for ip in net.hosts():
    pass

# перебор масок
for mask in range(33):
    net = ip_network(f"218.48.192.56/{mask}", 0)
    if net.network_address == ip_address("218.48.192.0"):
        if net.num_addresses >= 500:
            print(net.netmask)


# Два узла находятся в разных подсетях
for m in range(33):
    net1 = ip_network(f"157.127.172.56/{m}",0)
    net2 =ip_network(f"157.127.191.78/{m}", 0)
    if net1.network_address != net2.network_address:
        print(m)

