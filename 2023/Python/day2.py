import re

def run(data):
    limited = 0
    power = 0
    for i, line in enumerate(data):
        line = line.split(":")[1]
        line = line.split(";")
        for j, turn in enumerate(line):
            line[j] = turn.split(",")

        rgb_min = [0, 0, 0]
        impossible = False

        for j, turn in enumerate(line):
            for cubes in turn:
                n = int(cubes.split()[0])

                if "red" in cubes:
                    if n > rgb_min[0]:
                        rgb_min[0] = n
                elif "green" in cubes:
                    if n > rgb_min[1]:
                        rgb_min[1] = n
                elif "blue" in cubes:
                    if n > rgb_min[2]:
                        rgb_min[2] = n

        for j, c in enumerate(rgb_min):
            if c > 12 + j:
                impossible = True

        power += rgb_min[0] * rgb_min[1] * rgb_min[2]
        if not impossible:
            limited += i + 1

    print(f"Part 1: {limited}")
    print(f"Part 2: {power}")
