#!/usr/bin/env python3

import re

def process_digits(line, inverted):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if inverted:
        line = line[::-1]
        for i, d in enumerate(digits):
            digits[i] = d[::-1]
    buffer = ""
    result = 0
    for i, c in enumerate(line):
        clear = True
        if c.isnumeric():
            return int(c)
        else:
            buffer += c
            for j, d in enumerate(digits):
                if d == buffer:
                    return j + 1
                elif d.startswith(buffer):
                    clear = False
            if clear:
                buffer = "" + c
    raise ValueError("No digit found in line " + line)

def run(data):
    sum = 0
    for line in data:
        line = re.sub(r"[^0-9]", "", line)
        if len(line) != 0:
            sum += int(line[0] + line[-1])
    print(f"Part 1: {sum}")

    sum = 0
    for line in data:
        result = 10 * process_digits(line, False) + process_digits(line, True)
        sum += result
    print(f"Part 2: {sum}")

if __name__ == '__main__':
    with open("../input/input_1.txt", "r") as f:
        data = f.readlines()
    run(data)
