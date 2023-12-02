#!/usr/bin/env python3

import re

def process_digits(line, inverted):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if inverted:
        line = line[::-1]
        for i, d in enumerate(digits):
            digits[i] = d[::-1]
    result = 0
    for i, c in enumerate(line):
        if c.isnumeric():
            return int(c)
        else:
            for j, d in enumerate(digits):
                if line[i:].startswith(d):
                    return j + 1
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
