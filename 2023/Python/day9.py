def predict(history):
    diffs = []
    ready = True
    for i in range(len(history) - 1):
        diff = history[i + 1] - history[i]
        diffs.append(diff)
        if diff != 0:
            ready = False
    predicate = history[-1]
    if not ready:
        predicate += predict(diffs)
    return predicate

def run(data):
    future = 0
    past = 0
    for line in data:
        line = list(map(int, line.split()))
        future += predict(line)
        past += predict(line[::-1])

    print(f"Part 1: {future}")
    print(f"Part 2: {past}")