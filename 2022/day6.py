from pathlib import Path

with open(Path(__file__).parent / "input/input_6.txt", "r") as f:
    buffer = f.readline()

for i in range(4,len(buffer)):
    temp = buffer[i-4:i]
    x = 0
    for ch in temp:
        x += temp.count(ch)
    if x == 4:
        print("Packet marker after", i, "characters")
        break

for i in range(14,len(buffer)):
    temp = buffer[i-14:i]
    x = 0
    for ch in temp:
        x += temp.count(ch)
    if x == 14:
        print("Message marker after", i, "characters")
        break