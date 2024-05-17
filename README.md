# piFinder
A Python Script Which Uses Scapy and NPCap for finding Raspberry pi's on your network.

Jer542: I have a raspberry pi that occaisionally restart, and typically is located at 192.168.1.8 on my network.  In the event that someone else connects and takes that address, I would like to be able to scan for the raspberry pi'

GitHub Copilot: You can use a Python script to scan your network for the Raspberry Pi. The script will ping each IP address in your subnet and check the MAC address of the responding device. Raspberry Pi's MAC address usually starts with "b8:27:eb", "dc:a6:32", or "e4:5f:01" for Raspberry Pi 4 and newer.

Here's a Python script that uses the `scapy` library to do this:

```python
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
```

This script will print out the IP addresses of all Raspberry Pis in your network. You can run this script whenever you need to find your Raspberry Pi.

Please note that you need to install the `scapy` library before running this script. You can install it using pip:

```bash
pip install scapy
```

Also, this script needs to be run with administrator privileges because it uses raw sockets.

Jer542: pip install for scapy?

GitHub Copilot: Yes, you can install the `scapy` library using pip. Open your terminal and run the following command:

```bash
pip install scapy
```

If you're using Python 3, you might need to use `pip3` instead:

```bash
pip3 install scapy
```

Remember, you might need to run these commands with administrator privileges (i.e., using `sudo` on Unix-based systems or running your command prompt as an administrator on Windows).

Jer542: WARNING: No libpcap provider available ! pcap won't be used
Traceback (most recent call last):
  File "c:\Users\jerem\OneDrive\Desktop\Python Projects\pi-detector.py", line 21, in <module>
    raspberry_pis = scan_network('192.168.1.1/24')
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\jerem\OneDrive\Desktop\Python Projects\pi-detector.py", line 9, in scan_network
    result = srp(packet, timeout=3, verbose=0)[0]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Python311\Lib\site-packages\scapy\sendrecv.py", line 687, in srp
    s = iface.l2socket()(promisc=promisc, iface=iface,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Python311\Lib\site-packages\scapy\arch\windows\__init__.py", line 1019, in __init__
    raise RuntimeError(
RuntimeError: Sniffing and sending packets is not available at layer 2: winpcap is not installed. You may use conf.L3socket orconf.L3socket6 to access layer 3

GitHub Copilot: The error message indicates that the `winpcap` library, which is required for packet sniffing and sending at layer 2, is not installed on your system. 

To resolve this issue, you need to install the `winpcap` or `npcap` library on your Windows machine. 

Here are the steps to install `npcap`:

1. Download the npcap installer from the [Npcap website](https://nmap.org/npcap/).
2. Run the installer. During the installation, make sure to check the option "Install Npcap in WinPcap API-compatible Mode".
3. After the installation is complete, restart your computer.

After these steps, you should be able to run your script without encountering the error.

Jer542: how can I do this for multiple types of hardware

GitHub Copilot: If you want to scan for multiple types of hardware, you would need to know the MAC address prefixes for those devices. Each manufacturer is assigned a unique MAC address prefix. 

You can modify the `scan_network` function to accept a list of MAC address prefixes and check if the MAC address of each responding device starts with any of the prefixes in the list.

Here's how you can modify the function:

```python
def scan_network(target_ip: str, mac_prefixes: List[str]) -> List[str]:
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []

    for sent, received in result:
        # Check if the MAC address is from a device with one of the specified MAC prefixes
        for prefix in mac_prefixes:
            if received.hwsrc.startswith(prefix):
                devices.append((received.psrc, received.hwsrc))

    return devices

# Replace '192.168.1.1/24' with your subnet
# Add the MAC address prefixes for the devices you want to scan for
mac_prefixes = ['b8:27:eb', 'dc:a6:32', 'e4:5f:01']
devices = scan_network('192.168.1.1/24', mac_prefixes)

for ip, mac in devices:
    print(f'Device found: IP={ip}, MAC={mac}')
```

This script will print out the IP and MAC addresses of all devices in your network that have a MAC address starting with one of the prefixes in the `mac_prefixes` list.

Jer542: write a readme for thsi

GitHub Copilot: # Raspberry Pi Network Scanner

This Python script scans your local network for Raspberry Pi devices. It uses the `scapy` library to send ARP requests to each IP address in your subnet and checks the MAC address of the responding devices. Raspberry Pi devices typically have MAC addresses that start with "b8:27:eb", "dc:a6:32", or "e4:5f:01".

## Requirements

- Python 3
- `scapy` library
- `winpcap` or `npcap` library (for Windows users)

## Installation

1. Install Python 3 if you haven't already. You can download it from the [official website](https://www.python.org/downloads/).

2. Install the `scapy` library using pip:

```bash
pip install scapy
```

3. If you're using Windows, install the `winpcap` or `npcap` library:

- Download the npcap installer from the [Npcap website](https://nmap.org/npcap/).
- Run the installer. During the installation, make sure to check the option "Install Npcap in WinPcap API-compatible Mode".
- Restart your computer.

## Usage

1. Open the `pi-detector.py` file in a text editor.

2. Replace '192.168.1.1/24' with your subnet.

3. Run the script:

```bash
python pi-detector.py
```

The script will print out the IP addresses of all Raspberry Pis in your network.
