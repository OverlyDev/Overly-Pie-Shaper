def load_steamids_dict() -> dict:
    ids = {}

    with open("steamids.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        steamid = line.split(" - ")[0].strip()
        name = line.split(" - ")[1].strip()
        ids[steamid] = name

    return ids


def load_steamids_str() -> str:
    ids = ""

    with open("steamids.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        ids += line

    return ids


def add_to_steamids(steamid, displayname):
    entry = steamid + " - " + displayname + "\n"
    with open("steamids.txt", "a") as f:
        f.writelines(entry)
