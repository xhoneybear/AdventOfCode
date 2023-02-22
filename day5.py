from pathlib import Path

with open(Path(__file__).parent / "input/input_5.txt", "r") as f:
    cargo = f.readlines()

h = 0

for line in cargo:
    if line.isspace():
        break
    h += 1

ship_raw = cargo[:h]
ship = []

for i in range(1, len(ship_raw[-1]), 4):
    stack = []
    for j in range(h-1, -1, -1):
        temp = ship_raw[j]
        if temp[i].isalpha() == True:
            stack.append(temp[i])
    ship.append(stack)

print("Before repacking:         ", end="")

for stack in ship:
    print(stack[-1], end="")
print()

cm9000 = []
cm9001 = []

for stack in ship:
    cm9000.append(stack)
    cm9001.append(stack)

moves = cargo[h+1:]

# CrateMover 9000

for move in moves:

    move = move.removesuffix("\n").split(" ")

    for i in range(0, len(move)):
        if move[i].isdecimal() == True:
            move[i] = int(move[i])

    count = -move[1]
    src = move[3]-1
    dst = move[5]-1

    cm9000[dst].extend(reversed(cm9000[src][count:]))
    cm9000[src] = cm9000[src][:count]

print("After CM9000 repacking:   ", end="")

for stack in cm9000:
    print(stack[-1], end="")
print()

# CrateMover 9001

for move in moves:

    move = move.removesuffix("\n").split(" ")

    for i in range(0, len(move)):
        if move[i].isdecimal() == True:
            move[i] = int(move[i])

    count = -move[1]
    src = move[3]-1
    dst = move[5]-1

    cm9001[dst].extend(cm9001[src][count:])
    cm9001[src] = cm9001[src][:count]

print("After CM9001 repacking:   ", end="")

for stack in cm9001:
    print(stack[-1], end="")
print()