from pathlib import Path

with open(Path(__file__).parent / "input/input_4.txt", "r") as f:
    pairs = f.readlines()

total_overlap = 0
partial_overlap = 0

for pair in pairs:
    
    elf = pair.removesuffix("\n").split(",")
    elf[0] = elf[0].split("-")
    elf[1] = elf[1].split("-")

    elf[0][0] = int(elf[0][0])
    elf[0][1] = int(elf[0][1])
    elf[1][0] = int(elf[1][0])
    elf[1][1] = int(elf[1][1])

    if (elf[0][0] <= elf[1][0] and elf[0][1] >= elf[1][1]) or (elf[0][0] >= elf[1][0] and elf[0][1] <= elf[1][1]):
        total_overlap += 1
    
    if (elf[0][0] >= elf[1][0] and elf[0][0] <= elf[1][1]) or (elf[0][1] >= elf[1][0] and elf[0][1] <= elf[1][1]) or (elf[1][0] >= elf[0][0] and elf[1][0] <= elf[0][1]) or (elf[1][1] >= elf[0][0] and elf[1][1] <= elf[0][1]):
        partial_overlap += 1

print(total_overlap)
print(partial_overlap)