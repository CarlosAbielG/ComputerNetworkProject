# Ethernet Chat: Layer 2 Messaging with Custom Ethernet Frames

## Project Overview
In this project we have implemented a simple chat system to allow two devices to communicate using the Ethernet frames in layer 2. In this case IP address, TCP, UDP and HTTP were not utilized but instead we have created modified Ethernet frames to send data directly from one device to another using the MAC address. 
The two devices are the sender and the receiver but the receiver is constantly listening what is happening on the network interface and it will detect any frame from the custom EtherType such the 0x88B5 and will decode the payload and get displayer at the terminal of the device.
The main goal of this project is to showcase how two devices are allow to communicate at the layer 2 (Link layer) before any IP address is established.

---

## Motivation
In current times we have seen many devices using very sophisticated application that uses high level protocols. But even without those protocols such as TCP, UDP etc. it is quire manageable to establish a local network communication with the proper Ethernet frame setup and the usage of the MAC address.

This project was created to better understand what happens at the lower layers of networking. It shows how data can be manually placed into an Ethernet frame, transmitted across a local virtual network, captured with Wireshark, and decoded by a receiving program.
This project has helped to have a better understanding of what is happening with the link layer despite being a lower layer it still carries huge importance in networking. We have shown that data can be manipulated into the Ethernet frame and we can transmit through a local virtual network and using Wireshark to visualize and decode the data. 


This project has made improvements in the following topics:

- Ethernet frame structure
- MAC addressing
- Link Layer communication
- Packet sniffing
- Custom protocol design
- Wireshark analysis
- Low level network programming

Real-world areas where this knowledge is useful include network troubleshooting, cybersecurity, embedded systems, custom device discovery, and protocol analysis.
In a real case scenario this project is essential for network troubleshooting, protocol analysis, and custom device discovery as well as in cybersecurity since we can see if anything has a malicious intent.

## Tools and Technologies Used

- Oracle VirtualBox
- Ubuntu Linux virtual machines
- Python 3
- Scapy
- Wireshark
- GitHub
- Visual Studio Code / GitHub Codespaces

---

## Network Topology

The project uses two Ubuntu virtual machines connected through a VirtualBox Internal Network.
Within this project I have used two vitual machines using Oracle VM both running Ubuntu and establish an internal network among them.   

```text
+-------------------------+          VirtualBox Internal Network        +-------------------------+
| Sender VM               |  -----------------------------------------> | Receiver VM             |
| Ubuntu                  |                                             | Ubuntu                  |
| Runs sender.py          |                                             | Runs receiver.py        |
| Sends custom frames     |                                             | Listens for frames      |
| MAC: 08:00:27:b9:a3:f7  |                                             | MAC: 08:00:27:43:12:0b  |
+-------------------------+                                             +-------------------------+
