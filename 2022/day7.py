from pathlib import Path

with open(Path(__file__).parent / "input/input_7.txt", "r") as f:
    output = f.readlines()

def maketree(path):

    global n, size, sizes

    while n < len(output):

        n += 1

        if output[n][0] == "$":

            if "cd" in output[n]:

                if ".." in output[n]:
                    sizes = []
                    pathsize = 0
                    deepcalc(path)
                    for i in sizes:
                        pathsize += i
                    if pathsize <= 100000:
                        size += pathsize
                    if pathsize >= deficit:
                        large_folders.append(pathsize)
                    break

                else:
                    temp = []
                    path.append(temp)
                    maketree(path[-1])

            elif "ls" in output[n]:

                n += 1

                while n < len(output):

                    if output[n][0] == "$":
                        n -= 1
                        break

                    elif output[n][0].isnumeric():
                        output[n] = output[n].split(" ")
                        path.append(int(output[n][0]))

                    n += 1

def deepcalc(path):

    for element in path:
        if type(element) == list:
            deepcalc(element)
        else:
            sizes.append(element)

root = []
large_folders = []
n = 0
size = 0
totalsize = 0

for line in output:
    line = line.split(" ")
    if line[0].isnumeric():
        totalsize += int(line[0])

deficit = totalsize - (70000000 - 30000000)

maketree(root)

todelete = sorted(large_folders)[0]

print("Total size of small directories:", size)
print("Size of the directory to delete:", todelete)