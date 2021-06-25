import pydivert
import re

PACKET_FILTER = "(udp.SrcPort >= 27000 and udp.SrcPort <=27200) || (udp.DstPort >= 27000 and udp.DstPort <= 27200)"
STEAM_PATTERN = b'steamid:[0-9]{17}'

PACKETS_TOTAL = 0
PACKETS_ALLOWED = 0
PACKETS_BLOCKED = 0


def do_the_thing(allowed: dict):
    w = pydivert.WinDivert(PACKET_FILTER)
    w.open()

    while True:
        packet = w.recv()

        if b"steamid" in packet.udp.payload:
            matches = re.findall(STEAM_PATTERN, packet.udp.payload)
            packet_ids = set()
            for i in matches:
                packet_ids.add(i.decode('utf-8').split(':')[1])

            packet_ids.difference_update(list(allowed.keys()))

            if len(packet_ids) == 0:
                w.send(packet)
            else:
                pass

        else:
            w.send(packet)
            pass


def load_steamids_dict() -> dict:
    ids = {}

    with open("steamids.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        steamid = line.split(" - ")[0]
        name = line.split(" - ")[1]
        ids[steamid] = name

    return ids


def load_steamids_str() -> str:
    ids = ""

    with open("steamids.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        ids += line

    return ids


if __name__ == '__main__':
    peeps = load_steamids_dict()
    print("\n\nNow Filtering\n\n")
    do_the_thing(peeps)
