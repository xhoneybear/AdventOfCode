from pathlib import Path

with open(Path(__file__).parent / "input/input_10.txt", "r") as f:
    instructions = f.readlines()

cycles = 0

for i in range(0, len(instructions)):
    if "noop" in instructions[i]:
        cycles += 1
    elif "addx" in instructions[i]:
        instructions[i] = instructions[i].removesuffix("\n").split(" ")
        instructions[i][1] = int(instructions[i][1])
        cycles += 2

register = 1
k = 0
wait = 1
signal = []
screen = ["."]*cycles

for i in range(1, cycles+1):

    if i == 20+40*k:
        signal.append((20+40*k)*register)
        k += 1

    for n in range(0, cycles, 40):
        if i-1-n in range(register-1, register+2) and i-1-n >= 0:
            screen[i-1] = "#"
    if instructions[0][0] == "addx":
        if wait == 1:
            wait = 0
            continue
        elif wait == 0:
            wait = 1
            register += instructions[0][1]
    instructions.pop(0)

strength = 0

for n in signal:
    strength += n

print("\nTotal signal strength:", strength, "\n")

for k in range(0, cycles, 40):
    for l in range(k, k+40):
        print(screen[l], end="")
    print()
print()