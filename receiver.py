from scapy.all import sniff, Ether, Raw
import argparse

CUSTOM_ETHERTYPE = 0x88B5

def handle_packet(packet):
    if Ether in packet and packet[Ether].type == CUSTOM_ETHERTYPE:
        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst


        if Raw in packet:
            try:
                payload = packet[Raw].load.decode("utf-8")

            except UnicodeDecodeError:

                print("Received a frame but payload can not be decoded ")
                return



            parts = payload.split("|", 3)

            if len(parts) == 4 and parts[0] == "CHAT":

                version = parts[1]
                username = parts[2]
                message = parts[3]

                print("--------------------------------")
                print("Custom Ethernet Caht Message Received")
                print("Source MAC:", src_mac)
                print("Destination MAC:", dst_mac)
                print("Protocol Version:", version)
                print("From:", username)
                print("Message:", message)
                print("--------------------------------")
            else:
                print("Received unknown payload:", payload)




def main():
    
    parser = argparse.ArgumentParser(description="Receive custom Ethernet chat frames")
    parser.add_argument("--iface", required=True, help="Interface to listen on, example: enp0s8")
    args = parser.parse_args()

    print("Listening for custom ethernet chat frames...")
    print("Interface:", args.iface)
    print("Custom EtherType :", hex(CUSTOM_ETHERTYPE))
    print("Press Ctrl+C to stop")

    sniff(
        iface=args.iface,
        prn=handle_packet,
        store=False
    )


if __name__ == "__main__":
    main()