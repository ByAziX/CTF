import pyshark
import os

os.chdir(os.path.dirname(__file__))

file = pyshark.FileCapture("ez.pcap")

total = bytes()

for packet in file:
    if "tcp" in dir(packet):
        if packet['ip'].dst == "10.100.210.88":
            ad = eval(f"0x{packet.tcp.flags[4:6]}").to_bytes()
            total += ad

print(total)

with open("res.txt", 'wb') as f:
    f.write(total)