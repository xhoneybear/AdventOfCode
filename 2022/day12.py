from pathlib import Path

with open(Path(__file__).parent / "input/input_12.txt", "r") as f:
    elevation = f.readlines()

distance = []

for row in range(len(elevation)-1):
    elevation[row] = elevation[row][:-1]

for row in range(len(elevation)):
    distance.append([])
    for column in range(len(elevation[row])):
        distance[row].append("X")
        if elevation[row][column] == "S":
            coords_start = [column, row]
            elevation[row] = elevation[row].replace("S", "a")
            # distance[row][column] = 0
        elif elevation[row][column] == "E":
            coords_end = [column, row]
            elevation[row] = elevation[row].replace("E", "z")

def estimate(x,y,i):
    for a in range(y-1, y+2):
        if 0 <= a < len(elevation) and ord(elevation[a][x]) <= ord(elevation[y][x])+1 and (distance[a][x] == "X" or distance[a][x] > i):
            # print("x"+str(x)+", y"+str(a)+" -", i, elevation[a][x])
            distance[a][x] = i
            estimate(x,a,i+1)
    for b in range(x-1,x+2):
        if 0 <= b < len(elevation[0]) and ord(elevation[y][b]) <= ord(elevation[y][x])+1 and (distance[y][b] == "X" or distance[y][b] > i):
            # print("x"+str(b)+", y"+str(y)+" -", i, elevation[y][b])
            distance[y][b] = i
            estimate(b,y,i+1)

estimate(coords_start[0], coords_start[1], 1)

print("Length of the optimal route:", distance[coords_end[1]][coords_end[0]])

directlow = []

for y in range(len(elevation)):
    for x in range(len(elevation[0])):
        if elevation[y][x] == "a":
            # print(elevation[y][x], "- x"+str(x)+", y"+str(y))
            for a in range(y-1, y+2):
                for b in range(x-1, x+2):
                    if 0 <= a < len(elevation) and 0 <= b < len(elevation[0]) and abs(a-y)+abs(b-x) <= 1 and elevation[a][b] == "b" and not [y,x] in directlow:
                        directlow.append([y,x])
                        # print("Surrounding:", elevation[a][b], "- x"+str(b)+", y"+str(a))
                        # print("Trailing route: starting point: x"+str(x)+", y"+str(y))
                        estimate(x,y,1)

print("Length of the potential hiking trail:", distance[coords_end[1]][coords_end[0]])