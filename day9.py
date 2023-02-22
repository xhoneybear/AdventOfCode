from os import system
from time import sleep
from pathlib import Path

with open(Path(__file__).parent / "input/input_9.txt", "r") as f:
    moves = f.readlines()

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

hor = [0]
vert = [0]
    
for i in range(0, len(moves)):
    temp = 0
    moves[i] = moves[i].split(" ")
    moves[i][1] = int(moves[i][1])
    if moves[i][0] == "U":
        vert.append(vert[-1]+moves[i][1])
    if moves[i][0] == "R":
        hor.append(hor[-1]+moves[i][1])
    if moves[i][0] == "D":
        vert.append(vert[-1]-moves[i][1])
    if moves[i][0] == "L":
        hor.append(hor[-1]-moves[i][1])

hor = sorted(hor)
vert = sorted(vert)

# Position recording: 0 - head, 9 - tail; [0],[1] - x,y coordinates
pos = []
for i in range(0,10):
    pos.append([-vert[0], -hor[0]])
    
hor = hor[-1] - hor[0]+1
vert = vert[-1] - vert[0]+1

# field = []
visited_short = []
visited_long = []

for i in range(0, vert):
    # row = []
    row_short = []
    row_long = []
    for j in range(0, hor):
        # row.append(".")
        row_short.append(0)
        row_long.append(0)
    # field.append(row)
    visited_short.append(row_short)
    visited_long.append(row_long)

visited_short[pos[0][0]][pos[0][1]] = 1
visited_long[pos[0][0]][pos[0][1]] = 1

# field[pos[0][0]][pos[0][1]] = "\033[1m\033[7m\033[36m0\033[0m"

# system("clear")

# for line in reversed(field):
#     for char in line:
#         print(char, end="")
#     print()

for move in moves:
    for step in range(0, move[1]):

        # for n in range(0,10):
        #     field[pos[n][0]][pos[n][1]] = "."

        if move[0] == "U":
            pos[0][0] += 1
        elif move[0] == "R":
            pos[0][1] += 1
        elif move[0] == "D":
            pos[0][0] -= 1
        elif move[0] == "L":
            pos[0][1] -= 1

        for n in range(1,10):

            if abs(pos[n-1][0]-pos[n][0]) == 2 or abs(pos[n-1][1]-pos[n][1]) == 2:
                pos[n][0] += sign(pos[n-1][0] - pos[n][0])
                pos[n][1] += sign(pos[n-1][1] - pos[n][1])
        
        # for n in range(9,-1, -1):

        #     field[pos[n][0]][pos[n][1]] = "\033[1m\033[7m\033[36m%s\033[0m" % n

        visited_short[pos[1][0]][pos[1][1]] = 1
        visited_long[pos[9][0]][pos[9][1]] = 1

        # sleep(0.1)
        # system("clear")

        # for line in reversed(field):
        #     for char in line:
        #         print(char, end="")
        #     print()
        # print(move)

visits_short = 0
visits_long = 0

for y in visited_short:
    for x in y:
        if x == 1:
            visits_short += 1

for y in visited_long:
    for x in y:
        if x == 1:
            visits_long += 1

print("Fields visited by a short rope:", visits_short)
print("Fields visited by a long rope:", visits_long)