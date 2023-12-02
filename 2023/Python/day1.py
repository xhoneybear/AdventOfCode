import re

def run(data):
    sum = 0
    for line in data:
        line = re.sub(r"[^0-9]", "", line)
        if len(line) != 0:
            sum += int(line[0] + line[-1])
    print(f"Part 1: {sum}")

    sum = 0
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in data:
        result = ""
        for i, c in enumerate(line):
            if c.isnumeric():
                result += c
                continue
            for j, digit in enumerate(digits):
                if line[i:].startswith(digit):
                    result += str(j + 1)
                    break
        if len(result) != 0:
            sum += int(result[0] + result[-1])
    print(f"Part 2: {sum}")
