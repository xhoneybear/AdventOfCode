def move(pipe, shift):
    if pipe == '|':
        if shift[0] != 0:
            return (shift[0], 0)
    elif pipe == '-':
        if shift[1] != 0:
            return (0, shift[1])
    elif pipe == 'F':
        if shift[0] == -1:
            return (0, 1)
        elif shift[1] == -1:
            return (1, 0)
    elif pipe == '7':
        if shift[0] == -1:
            return (0, -1)
        elif shift[1] == 1:
            return (1, 0)
    elif pipe == 'J':
        if shift[0] == 1:
            return (0, -1)
        elif shift[1] == 1:
            return (-1, 0)
    elif pipe == 'L':
        if shift[0] == 1:
            return (0, 1)
        elif shift[1] == -1:
            return (-1, 0)
    raise ValueError

def run(data):
    for i, line in enumerate(data):
        if 'S' in line:
            start = [i, line.index('S')]
            position = start[:]
            break

    if data[start[0] + 1][start[1]] in ('|', 'J', 'L'):
        shift = (1, 0)
    elif data[start[0]][start[1] + 1] in ('-', '7', 'J'):
        shift = (0, 1)
    elif data[start[0] - 1][start[1]] in ('|', 'F', '7'):
        shift = (-1, 0)
    elif data[start[0]][start[1] - 1] in ('-', 'F', 'L'):
        shift = (0, -1)
    else:
        raise ValueError
    start_move = shift[:]
    position[0] += shift[0]
    position[1] += shift[1]
    edge = [tuple(position)]
    moves = 1
    while position != start:
        y = position[0]
        x = position[1]
        shift = move(data[y][x], shift)
        position[0] += shift[0]
        position[1] += shift[1]
        edge.append(tuple(position))
        moves += 1
    if start_move[0] != 0 or shift[0] != 0:
        temp = [c for c in data[start[0]]]
        temp[start[1]] = '|'
        temp = ''.join(temp)
        data[start[0]] = temp
    print(f"Part 1: {moves//2 + moves % 2}")

    area = 0
    y = 0
    while y < len(data):
        x = 0
        inside = False
        awaited = None
        while x < len(data[y]):
            if (y, x) in edge:
                if data[y][x] in ('|', awaited):
                    awaited = None
                    inside = not inside
                elif data[y][x] == 'F':
                    awaited = 'J'
                elif data[y][x] == 'L':
                    awaited = '7'
            else:
                area += inside
            x += 1
        y += 1
    print(f"Part 2: {area}")
