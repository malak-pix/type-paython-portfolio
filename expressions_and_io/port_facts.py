#RFC 9293 : Transmission Control Protocol (TCP)
#RFC 791 :  Internet Protocol (IPv4)
PORT_BITS = 16
IPV4_BITS = 32
port_values = 2**PORT_BITS
highest_port_num = port_values-1
ipv4_address = 2**IPV4_BITS
print(f"Port Values:\t{port_values}")
print(f"Highest Port:\t{highest_port_num}")
print(f"IPV4 Address:\t{ipv4_address}")