from math import ceil

def find_bound(mid, bound, off, beat):
    if bound * (mid - bound) > beat:
        if (bound - 1) * (mid - bound + 1) < beat:
            return bound
        return find_bound(mid, bound - off, ceil(off / 2), beat)
    else:
        return find_bound(mid, bound + off, ceil(off / 2), beat)

def run(data):
    times = list(map(int, data[0].split(":")[1].split()))
    distances = list(map(int, data[1].split(":")[1].split()))
    offsets = [0, 0, 0, 0]

    for i, time in enumerate(times):
        for s in range(time):
            distance = s * (time - s)
            if distance > distances[i]:
                offsets[i] += 1
    
    result = 1
    for i in range(4):
        result *= offsets[i]
    
    print(f"Part 1: {result}")

    time = int(data[0].replace(" ", "").split(":")[1])
    record = int(data[1].replace(" ", "").split(":")[1])
    midtime = ceil(time / 2)

    offset = 2 * (midtime - find_bound(time, midtime, ceil(time / 4), record)) + 1 - time % 2
    
    print(f"Part 2: {offset}")
