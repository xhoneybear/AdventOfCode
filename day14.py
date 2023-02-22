from pathlib import Path

with open(Path(__file__).parent / "input/input_14.txt", "r") as f:
    structurepath = f.readlines()

width = 0
height = 0

for i in range(len(structurepath)):
    structurepath[i] = structurepath[i].removesuffix("\n").split(" -> ")
    for j in range(len(structurepath[i])):
        structurepath[i][j] = structurepath[i][j].split(",")
        for k in range(2):
            structurepath[i][j][k] = int(structurepath[i][j][k])
        if structurepath[i][j][0]+1 > width:
            width = structurepath[i][j][0]+1
        if structurepath[i][j][1]+2 > height:
            height = structurepath[i][j][1]+2
width += 501+height-width

cave = []
for i in range(height):
    cave.append(["."]*width)
cave.append(["#"]*width)

for i in range(len(structurepath)):
    for j in range(len(structurepath[i])-1):
        vector_x = structurepath[i][j+1][0]-structurepath[i][j][0]
        vector_y = structurepath[i][j+1][1]-structurepath[i][j][1]
        if vector_x != 0:
            if vector_x > 0:
                step = 1
                vector_x += 1
            else:
                step = -1
                vector_x -= 1
            for x in range(0, vector_x, step):
                cave[structurepath[i][j][1]][structurepath[i][j][0]+x] = "#"
        else:
            if vector_y > 0:
                step = 1
                vector_y += 1
            else:
                step = -1
                vector_y -= 1
            for y in range(0, vector_y, step):
                cave[structurepath[i][j][1]+y][structurepath[i][j][0]] = "#"

units_floor = 0
units_abyss = 0
abyss = False
pile = False

while pile == False:
    sand = [500,0]
    ground = False

    while ground == False:
        if cave[sand[1]+1][sand[0]] == ".":
            sand[1] += 1
        elif cave[sand[1]+1][sand[0]-1] == ".":
            sand[1] += 1
            sand[0] -= 1
        elif cave[sand[1]+1][sand[0]+1] == ".":
            sand[1] += 1
            sand[0] += 1
        else:
            cave[sand[1]][sand[0]] = "o"
            ground = True
            units_floor += 1
            if sand[1] == height - 1:
                abyss = True
            if abyss == False:
                units_abyss += 1
            if sand == [500,0]:
                pile = True

for i in range(len(cave)):
    for j in range(500-height, width):
        print(cave[i][j], end="")
    print()
print("Sand units before flowing into the abyss:  ", units_abyss)
print("Sand units before blocking the sand source:", units_floor)