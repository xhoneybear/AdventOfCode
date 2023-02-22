from pathlib import Path

with open(Path(__file__).parent / "input/input_1.txt", "r") as f:
    calories = f.readlines()

elves = []
elf = 0

for line in calories:
    if line == "\n":
        elves.append(elf)
        elf = 0
    else:
        elf += int(line)

print(max(elves))

elves = sorted(elves, reverse=True)

top = elves[:3]

kcal = 0

for i in top:
    kcal += i

print(kcal)