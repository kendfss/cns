import argparse, subprocess


from . env import *


# def handler(args):
    # while 1:
    #     cmd = input(">>> ")
    #     if cmd == "quit":
    #         return
    #     eval(cmd)

def handler(args):
    subprocess.run(['python', '-i', this])

def main():
    parser = argparse.ArgumentParser(description="REPL for pythonic file system management and navigation")
    # parser.add_argument('root', default='.', action='store', help="root to the package/path to the file")
    handler(parser.parse_args())