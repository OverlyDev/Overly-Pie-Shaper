import pydivert
import re


PACKET_FILTER = "(udp.SrcPort >= 27000 and udp.SrcPort <=27200) || (udp.DstPort >= 27000 and udp.DstPort <= 27200)"
STEAM_PATTERN = b"steamid:[0-9]{17}"


def filter_packets(allowed: dict):
    w = pydivert.WinDivert(PACKET_FILTER)
    w.open()

    while True:

        packet = w.recv()

        # drop xbox packets
        if b"xboxpwid" in packet.udp.payload:
            pass

        # drop psn packets
        if b"psn-" in packet.udp.payload:
            pass

        # filter steam packets
        if b"steamid" in packet.udp.payload:
            matches = re.findall(STEAM_PATTERN, packet.udp.payload)
            packet_ids = set()
            for i in matches:
                packet_ids.add(i.decode("utf-8").split(":")[1])

            packet_ids.difference_update(list(allowed.keys()))

            if len(packet_ids) == 0:
                w.send(packet)
            else:
                pass

        else:
            w.send(packet)
            pass
