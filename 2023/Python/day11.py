def run(data):
    rows = []
    cols = []
    galaxies = []

    for y, row in enumerate(data):
        if not '#' in row:
            rows.append(i)
            continue
        for x, c in enumerate(row):
            if c == '#':
                galaxies.append((x, y))
    for x, _ in enumerate(data[0]):
        if not '#' in [row[x] for _, row in enumerate(data)]:
            cols.append(x)

    short = long = 0
    for k, galaxy in enumerate(galaxies):
        for n in range(k + 1, len(galaxies)):
            y = (min(galaxies[n][0], galaxy[0]), max(galaxies[n][0], galaxy[0]))
            x = (min(galaxies[n][1], galaxy[1]), max(galaxies[n][1], galaxy[1]))

            short += y[1] - y[0] + x[1] - x[0]
            short += sum(1 for e in cols if e in range(y[0], y[1]))
            short += sum(1 for e in rows if e in range(x[0], x[1]))

            long += y[1] - y[0] + x[1] - x[0]
            long += sum(999999 for e in cols if e in range(y[0], y[1]))
            long += sum(999999 for e in rows if e in range(x[0], x[1]))

    print(f"Part 1: {short}")
    print(f"Part 2: {long}")
