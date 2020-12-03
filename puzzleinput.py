import sys
from os import path

with open(f"inputs/{path.basename(sys.argv[0])[:2]}.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def numbers():
    return [int(line) for line in lines]
