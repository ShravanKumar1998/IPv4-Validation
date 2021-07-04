valid_range = [0,128,192,224,240,248,252,254,255]
network_addr = [0,0,0,0]
def ipv4_chk(temp):
    for i in temp:
        if i>255 or i<0:
            return False
    return True

def subnet_chk(a):
    for i in range(0,3):
        if a[i]>255 or a[i]<0 or (a[i]<a[i+1]) or (a[i] not in valid_range):
            return False
    if a[3]>255 or a[3]<0 or (a[i] not in valid_range):
        return False
    return True

print('IPv4 Break Down Program')
while True:
    #IPv4 address
    ipv4= list(map(int,input('\nPlease enter an IPv4 Address (#.#.#.#): ').split('.')))

    #subnet or netmask
    subnet= list(map(int,input('Please enter the Subnet Mask (#.#.#.#): ').split('.')))  

    ipv4_valid = ipv4_chk(ipv4)
    subnet_valid = subnet_chk(subnet)
    
    #if ipv4 or subnet mask is not valid, take input from user again.
    if not(ipv4_valid and subnet_valid):
        print("""
        - The correct IP format is [0-255].[0-255].[0-255].[0-255]
          The correct Subnet Mask format is decimal equivalent of binary 1 bits for each octet 
          that represents the network 
          Each octet will be 255 until the network ends and the host address begins. Each full 
          octet of the host address will be 0. There may be 1 octet that represents both 
          network and host, and the valid values for this are: 
                      [0,128,192,224,240,248,254,255]
        - Example:  192.168.2.1 (no spaces)
                    255.255.255.128 (no spaces)""")
    else:
        break    


#IPv4 Address
bin_ip = [bin(ipv4[i])[2:].zfill(8) for i in range(0,4)]
print(f'\nAddress:\t {ipv4[0]}.{ipv4[1]}.{ipv4[2]}.{ipv4[3]}\t{bin_ip[0]}.{bin_ip[1]}.{bin_ip[2]}.{bin_ip[3]}')


#Prefix
prefix = 0
for i in range(0,4):
    prefix += bin(subnet[i]).count('1')
#subnet mask == prefix in binary format
bin_subn = [bin(subnet[i])[2:].zfill(8) for i in range(0,4)]
print(f'Prefix:\t\t /{prefix}\t\t{bin_subn[0]}.{bin_subn[1]}.{bin_subn[2]}.{bin_subn[3]}')


#Subnet mask or Netmask
#bin_subn = [bin(subnet[i])[2:].zfill(8) for i in range(0,4)]
print(f'Netmask:\t {subnet[0]}.{subnet[1]}.{subnet[2]}.{subnet[3]}\t{bin_subn[0]}.{bin_subn[1]}.{bin_subn[2]}.{bin_subn[3]}')


#Wildcard
wildcard = [0,0,0,0]
for i in range(0,4):
    wildcard[i] = 255 - subnet[i]
bin_wc = [bin(wildcard[i])[2:].zfill(8) for i in range(0,4)]
print(f'Wildcard:\t {wildcard[0]}.{wildcard[1]}.{wildcard[2]}.{wildcard[3]}\t{bin_wc[0]}.{bin_wc[1]}.{bin_wc[2]}.{bin_wc[3]}') 

print('-----------------------------------------------------------------------')

#Network IP
network = [0,0,0,0]
for i in range(0,4):
    network[i] = ipv4[i] & subnet[i]
bin_nw = [bin(network[i])[2:].zfill(8) for i in range(0,4)]
print(f'Network:\t {network[0]}.{network[1]}.{network[2]}.{network[3]}\t{bin_nw[0]}.{bin_nw[1]}.{bin_nw[2]}.{bin_nw[3]}')


#Minimum Host IP
host_min = network.copy()
host_min[-1] += 1
bin_hmin = [bin(host_min[i])[2:].zfill(8) for i in range(0,4)]
print(f'HostMin:\t {host_min[0]}.{host_min[1]}.{host_min[2]}.{host_min[3]}\t{bin_hmin[0]}.{bin_hmin[1]}.{bin_hmin[2]}.{bin_hmin[3]}')


#Maximum Host IP
host_max = [network[i] + wildcard[i] for i in range(0,4)]
host_max[-1] -= 1
bin_hmax = [bin(host_max[i])[2:].zfill(8) for i in range(0,4)]
print(f'HostMax:\t {host_max[0]}.{host_max[1]}.{host_max[2]}.{host_max[3]}\t{bin_hmax[0]}.{bin_hmax[1]}.{bin_hmax[2]}.{bin_hmax[3]}')


#Broadcast IP 
broadcast = [network[i] + wildcard[i] for i in range(0,4)]
bin_b = [bin(broadcast[i])[2:].zfill(8) for i in range(0,4)]
print(f'Broadcast:\t {broadcast[0]}.{broadcast[1]}.{broadcast[2]}.{broadcast[3]}\t{bin_b[0]}.{bin_b[1]}.{bin_b[2]}.{bin_b[3]}')


#Total no.of hosts
print(f'Host/Net:\t {2**(32-prefix)}')

