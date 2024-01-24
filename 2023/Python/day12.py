from math import factorial

def fit(line, groups, index=0, limit=-2, part=0):
    global cache
    permut = 0
    if index == len(groups):
        permut += 1
        if '#' in line[part:]:
            return 1, False
        return 1, True

    n = len(line) - sum(groups, len(groups)) - limit
    result = 0

    for i in range(bool(index), n):
        new = part

        if '#' in line[new:new + i]:
            permut += 1
            continue
        new += i

        if '.' in line[new:new + groups[index]]:
            permut += 1
            continue
        old = new
        new += groups[index]

        if index + 1 < len(cache) and cache[index + 1][new] is not None:
            temp = sum(c for c in cache[index + 1][new + 1:] if c is not None)
        else:
            lim = limit - 1 + i
            d, temp = fit(line, groups, index + 1, lim, new)
            permut += d
        result += temp
        cache[index][old] = temp

    return permut, result

def run(data):
    global cache
    short = 0
    long = 0
    permut = 0
    done = 0
    for i, line in enumerate(data):
        folded, f_groups = line.split()
        unfolded = '?'.join([folded] * 5)

        folded = [c for c in folded]
        unfolded = [c for c in unfolded]

        f_groups = list(map(int, f_groups.split(',')))
        u_groups = f_groups[:] * 5

        n = len(unfolded) - sum(u_groups) + 1
        k = len(u_groups)

        cache = [[None] * len(unfolded) for _ in range(k)]
        print(len(unfolded), "prop")

        t = factorial(n) // (factorial(k) * factorial(n - k))
        print(f"Line {i} permutations\nPred: {t}")
        permut += t

        _, temp = fit(folded, f_groups)
        short += temp
        d, temp = fit(unfolded, u_groups)
        done += d
        long += temp
        print(f"Done: {d}")
        print(f"Result: {temp}\n")

    print(f"Part 1: {short}")
    print(f"Part 2: {long}")
    print(f"Permutations: {permut}")
    print(f"Permutations done: {done}")
