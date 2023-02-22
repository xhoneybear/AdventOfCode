from pathlib import Path

with open(Path(__file__).parent / "input/input_2.txt", "r") as f:
    moves = f.readlines()

score = 0

for line in moves:
    if "X" in line:
        score += 1
        if "A" in line:
            score += 3
        elif "C" in line:
            score += 6
    elif "Y" in line:
        score += 2
        if "A" in line:
            score += 6
        elif "B" in line:
            score += 3
    elif "Z" in line:
        score += 3
        if "B" in line:
            score += 6
        elif "C" in line:
            score += 3

print(score)

score = 0

for line in moves:
    if "A" in line:
        if "X" in line:
            score += 3+0
        elif "Y" in line:
            score += 1+3
        elif "Z" in line:
            score += 2+6
    if "B" in line:
        if "X" in line:
            score += 1+0
        elif "Y" in line:
            score += 2+3
        elif "Z" in line:
            score += 3+6
    if "C" in line:
        if "X" in line:
            score += 2+0
        elif "Y" in line:
            score += 3+3
        elif "Z" in line:
            score += 1+6

print(score)