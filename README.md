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
