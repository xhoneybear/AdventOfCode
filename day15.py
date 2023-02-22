from pathlib import Path

with open(Path(__file__).parent / "input/input_15.txt", "r") as f:
    sensors = f.readlines()

sensor = []
beacon = []
radius = []

beacon_unique = []

width = 0
height = 0

for i in range(len(sensors)):
    sensors[i] = sensors[i].replace(",", "").replace("=", " ").replace(":", "").removesuffix("\n").split()
    
    temp_s = [int(sensors[i][3])]
    temp_s.append(int(sensors[i][5]))
    sensor.append(temp_s)

    temp_b = [int(sensors[i][11])]
    temp_b.append(int(sensors[i][13]))
    beacon.append(temp_b)

    if not temp_b in beacon_unique:
        beacon_unique.append(temp_b)

    radius.append(abs(sensor[i][0]-beacon[i][0])+abs(sensor[i][1]-beacon[i][1]))

    if temp_s[0]+1 > width:
        width = temp_s[0]+1
    if temp_s[1]+1 > height:
        height = temp_s[1]+1

width += 2*max(radius)

field = ["."]*width
taken = 0

for n in range(len(sensor)):
    print("Polling sensor", n+1, "out of", len(sensor), "...")
    for x in range(sensor[n][0]-radius[n], sensor[n][0]+radius[n]+1):
        if abs(x-sensor[n][0])+abs(2000000-sensor[n][1]) <= radius[n] and field[max(radius)+x] != "#":
            field[max(radius)+x] = "#"
            taken += 1

for n in range(len(beacon_unique)):
    if beacon_unique[n][1] == 2000000:
        field[max(radius)+beacon_unique[n][0]] = "B"
        taken -= 1

print(taken)

for y in range(4000000):
    print(y)
    for x in range(4000000):
        temp = 4000000**2
        emptyfield = True
        for n in range(len(radius)):
            if abs(sensor[n][0]-x)+abs(sensor[n][1]-y) < temp:
                temp = abs(sensor[n][0]-x)+abs(sensor[n][1]-y)
            if temp <= radius[n]:
                emptyfield = False
        if emptyfield == True:
            print("Tuning frequency:", (4000000*x)+y)
            break
    if emptyfield == True:
        break