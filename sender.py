from scapy.all import Ether, Raw, sendp, get_if_hwaddr
import argparse

CUSTOM_ETHERTYPE = 0x88B5

def main():

    parser = argparse.ArgumentParser(description="Send custom Ethernet chat frames.")
    parser.add_argument("--iface", required=True, help="Interface to send on, example: enp0s8")
    parser.add_argument("--dst", required=True, help="Destination MAC address of receiver")
    parser.add_argument("--name", default="Sender", help="Name shown in chat")

    args = parser.parse_args()

    source_mac = get_if_hwaddr(args.iface)

    print("Custom ethernet Chat Sender")
    print("Interface:", args.iface)
    print("Source MAC: ", source_mac)
    print("Destination MAC:", args.dst)
    print("Custom EtherType:", hex(CUSTOM_ETHERTYPE))
    print("Type a message and press Enter")
    
    print("Type exit to quit")

    while True:
        message = input("> ")

        if message.lower() == "exit":
            print("Exiting sender")
            break

        payload = f"CHAT|1|{args.name}|{message}"

        frame = (
            Ether(
                dst=args.dst,
                src=source_mac,
                type=CUSTOM_ETHERTYPE
            )
            / Raw(load=payload.encode("utf-8"))
        )

        sendp(frame, iface=args.iface, verbose=False)

        print("Message sent")

if __name__ == "__main__":
    main()