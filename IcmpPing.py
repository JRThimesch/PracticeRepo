# THIS DOESN'T WORK ON THE LATEST VERSION OF SCAPY
# IT WORKS ON v2.4.0 OF SCAPY
# Python 3.7

# Jonathan Thimesch
# D696H345

from scapy.all import *
import socket

target = "www.google.com"
ipTarget = socket.gethostbyname(target)
#print(ipTarget)

for k in range(1, 16):
    packet = IP(dst = target, ttl = k) / ICMP()
    response = sr1(packet, verbose = 0)
    if response is None:
        print("no response")
        break
    elif response.src == ipTarget:
        print(k, "hops", "\t\tIP:", response.src)
        break
    else:
        print(k, "hops", "\t\tIP:", response.src)

