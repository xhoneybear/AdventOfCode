#!/usr/bin/env python3

from importlib import import_module
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <day>")
    sys.exit(1)

day = sys.argv[1]

try:
    with open(f"../input/input_{day}.txt", "r") as f:
        data = f.read().splitlines()
    day = import_module(f"day{day}")
except FileNotFoundError:
    print(f"No input data for day {day}")
    sys.exit(1)
except ModuleNotFoundError:
    print(f"No solution for day {day}")
    sys.exit(1)

day.run(data)
