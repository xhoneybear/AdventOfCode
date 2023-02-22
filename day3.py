from string import ascii_letters
from pathlib import Path

with open(Path(__file__).parent / "input/input_3.txt", "r") as f:
    rucksacks = f.readlines()

def priority(letter):
    index = ord(letter)
    if 97 <= index <= 122:
        index -= 96
    elif 65 <= index <= 90:
        index -= 38
    else:
        index = 0
    return index

total = 0

for sack in rucksacks:

    comp1 = sack[:int(len(sack)/2)]
    comp2 = sack[int(len(sack)/2):-1]

    for letter in ascii_letters:
        if letter in comp1 and letter in comp2:
            total += priority(letter)

print(total)

total = 0

for group in range(0, len(rucksacks), 3):
    for letter in ascii_letters:
        if letter in rucksacks[group] and letter in rucksacks[group+1] and letter in rucksacks[group+2]:
            total += priority(letter)

print(total)