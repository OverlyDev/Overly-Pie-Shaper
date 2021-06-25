from time import sleep

import click
import multiprocessing
from utils.cli_tools import (
    ask_add_data,
    ask_display_name,
    ask_exit,
    ask_start,
    ask_steamid,
    header,
    log,
)
from utils.file_tools import add_to_steamids, load_steamids_dict
from utils.shaper import filter_packets


@click.command()
def cli_menu():
    allowed = load_steamids_dict()

    while True:
        click.clear()
        header(allowed)

        if ask_add_data()["add"] is not False:
            steamid = ask_steamid()["steamid"]
            displayname = ask_display_name()["displayname"]
            add_to_steamids(steamid, displayname)
            allowed[steamid] = displayname
            continue

        if ask_start()["start"]:
            log("Running... Press Ctrl+C to stop", color="green")
            proc = multiprocessing.Process(target=filter_packets, args=(allowed,))
            proc.start()

            while True:
                try:
                    sleep(60)

                except KeyboardInterrupt:
                    proc.terminate()
                    log("Stopped", color="red")
                    break

        if ask_exit()["exit"]:
            log("See you next time!")
            exit()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    cli_menu()
