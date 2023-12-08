import re
from time import sleep

def gcd(a, b):
    a %= b
    if a == 0:
        return b
    else:
        return gcd(b, a)

def direct(char):
    return 0 if char == 'L' else 1

def run(data):
    dirs = data[0]
    all_nodes = {}
    for line in data[2:]:
        node, opts = line.split(" = ")
        all_nodes[node] = re.sub("[(),]", "", opts).split()

    node = "AAA"
    i = 0
    while node != "ZZZ":
        char = dirs[i % len(dirs)]
        node = all_nodes[node][direct(char)]
        i += 1
    print(f"Part 1: {i}")

    nodes = [node for node in all_nodes if node[2] == 'A']
    lcm = 1
    for j, node in enumerate(nodes):
        i = 0
        while node[2] != 'Z':
            char = dirs[i % len(dirs)]
            node = all_nodes[node][direct(char)]
            i += 1
        lcm = lcm * i // gcd(lcm, i)
    print(f"Part 2: {lcm}")
