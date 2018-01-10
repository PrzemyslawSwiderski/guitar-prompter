import random
import getopt
import sys

import os

import time

help_message = """
usage: guitar_prompter_chords [options]

Options:
    -h                              display help
    -w, --pause_time <arg>           time between notes randing (in seconds) (default 1)
    -c, --chords <arg>              chords separated by ',' (default C,D,E,G,A,Am,Em)
"""


def load_args(argv, config):
    try:
        opts, args = getopt.getopt(argv, "hw:c:",
                                   ["pause_time=", "chords="])
    except getopt.GetoptError:
        print(help_message)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_message)
            sys.exit()
        elif opt in ("-w", "--pause_time"):
            config["pause_time"] = float(arg)
        elif opt in ("-c", "--strings"):
            config["chords"] = arg.split(",")


def main(argv):
    config = {"pause_time": float("1"), "chords": "C,D,E,G,A,Am,Em".split(",")}

    load_args(argv, config)

    sleep_time = config["pause_time"]
    chords = config["chords"]

    print("Starting script: (CTRL + C to exit)")
    while True:
        try:
            os.system('cls')
            randed_chord = random.choice(chords)
            print(f"\n\n\n                    {randed_chord}")
            time.sleep(sleep_time)
        except KeyboardInterrupt:
            print("Quiting Script")
            sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
