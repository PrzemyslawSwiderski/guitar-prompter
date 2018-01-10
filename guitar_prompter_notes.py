import random
import getopt
import sys

import os

import time

help_message = """
usage: guitar_prompter_notes [options]

Options: 
    -h                              display help
    -w, --pause_time <arg> 			time between notes randing (in seconds) (default 1)
    -s, --strings <arg> 		    strings separated by ',' (default E,A,D,G,H,e)
    -t, --tabs <arg> 			    tabs separated by ',' (default 1,2,3)
"""


def load_args(argv, config):
    try:
        opts, args = getopt.getopt(argv, "hw:s:t:",
                                   ["pause_time=", "strings=", "tabs="])
    except getopt.GetoptError:
        print(help_message)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_message)
            sys.exit()
        elif opt in ("-w", "--pause_time"):
            config["pause_time"] = float(arg)
        elif opt in ("-s", "--strings"):
            config["strings"] = arg.split(",")
        elif opt in ("-t", "--tabs"):
            config["tabs"] = arg.split(",")


def main(argv):
    config = {"pause_time": float("1"), "strings": "E,A,D,G,H,e".split(","), "tabs": "1,2,3".split(",")}

    load_args(argv, config)

    sleep_time = config["pause_time"]
    strings = config["strings"]
    tabs = config["tabs"]

    print("Starting script: (CTRL + C to exit)")
    while True:
        try:
            os.system('cls')
            randed_string = random.choice(strings)
            randed_tab = random.choice(tabs)
            print(f"\n\n\n               {randed_string}-{randed_tab}")
            time.sleep(sleep_time)
        except KeyboardInterrupt:
            print("Quiting Script")
            sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
