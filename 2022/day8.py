from pathlib import Path

with open(Path(__file__).parent / "input/input_8.txt", "r") as f:
    grid = f.readlines()

for i in range(0, len(grid)):
    grid[i] = grid[i].removesuffix("\n")

visible = 0
scores = []

for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):

        state = 0
        scenic = 1
        vision = [0, 0, 0, 0]
        hidden = [0, 0, 0, 0]

        for n in range(y-1, -1, -1):
            vision[0] += 1
            if int(grid[n][x]) >= int(grid[y][x]):
                hidden[0] = 1
                break
        for e in range(x+1, len(grid[y])):
            vision[1] += 1
            if int(grid[y][e]) >= int(grid[y][x]):
                hidden[1] = 1
                break
        for s in range(y+1, len(grid)):
            vision[2] += 1
            if int(grid[s][x]) >= int(grid[y][x]):
                hidden[2] = 1
                break
        for w in range(x-1, -1, -1):
            vision[3] += 1
            if int(grid[y][w]) >= int(grid[y][x]):
                hidden[3] = 1
                break
        
        for a in hidden:
            state += a
        
        for a in vision:
            scenic *= a
        
        scores.append(scenic)
            
        if state != 4:
            visible += 1

print("Visible trees in grid:", visible)
print("Maximum scenic score: ", sorted(scores, reverse=True)[0])
