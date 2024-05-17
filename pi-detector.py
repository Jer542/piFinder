from scapy.all import ARP, Ether, srp
from typing import List

def scan_network(target_ip: str) -> List[str]:
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    raspberry_pis = []

    for sent, received in result:
        # Check if the MAC address is from a Raspberry Pi
        if received.hwsrc.startswith('b8:27:eb') or received.hwsrc.startswith('dc:a6:32') or received.hwsrc.startswith('e4:5f:01'):
            raspberry_pis.append(received.psrc)

    return raspberry_pis

# Replace '192.168.1.1/24' with your subnet
raspberry_pis = scan_network('192.168.1.1/24')

for raspberry_pi in raspberry_pis:
    print(f'Raspberry Pi found: {raspberry_pi}')