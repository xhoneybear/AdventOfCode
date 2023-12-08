from collections import Counter

def to_value(c, joker=False):
    match c:
        case 'T':
            return 10
        case 'J':
            if joker:
                return 1
            return 11
        case 'Q':
            return 12
        case 'K':
            return 13
        case 'A':
            return 14
        case _:
            return int(c)

def is_better(h1, hs1, c1, h2, hs2, c2, joker=False):
    cp1 = c1[hs1[0]] + c1[1] if hs1[0] != 1 else c1[hs1[0]]
    cp2 = c2[hs2[0]] + c2[1] if hs2[0] != 1 else c2[hs2[0]]
    if cp1 == cp2:
        c = c1[hs1[0]] + c1[1]
        if c in (2, 3):
            cp1 = c1[hs1[0]]
            cp2 = c2[hs2[0]]
            if c1[hs1[cp1]] > c2[hs2[cp2]]:
                return True
            elif c1[hs1[cp1]] < c2[hs2[cp2]]:
                return False
        h1 = list(map(lambda x: to_value(x, joker), h1))
        h2 = list(map(lambda x: to_value(x, joker), h2))
        for i in range(5):
            if h1[i] > h2[i]:
                return True
            elif h1[i] < h2[i]:
                return False
    elif cp1 > cp2:
        return True
    return False

def run(data):
    for joker in (False, True):
        sorted_hands = []
        sorted_bids = []
        winnings = 0
        for line in data:
            hand, bid = line.split()
            hand_sorted = list(map(lambda x: to_value(x, joker), hand))
            count = Counter(hand_sorted)
            hand_sorted = sorted(hand_sorted, key=lambda x: bool(x - 1) * (count[x] * 14 + x), reverse=True)
            inserted = False
            for i, hand_other in enumerate(sorted_hands):
                other_sorted = list(map(lambda x: to_value(x, joker), hand_other))
                count_other = Counter(other_sorted)
                other_sorted = sorted(other_sorted, key=lambda x: bool(x - 1) * (count_other[x] * 14 + x), reverse=True)
                if not is_better(hand, hand_sorted, count, hand_other, other_sorted, count_other, joker):
                    sorted_hands.insert(i, hand)
                    sorted_bids.insert(i, bid)
                    inserted = True
                    break
            if not inserted:
                sorted_hands.append(hand)
                sorted_bids.append(bid)
        for i, bid in enumerate(sorted_bids):
            winnings += (i + 1) * int(bid)
            print(sorted_hands[i])
        print(f"Part {1 + joker}: {winnings}")
