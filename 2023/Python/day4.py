def run(data):
    score = 0
    cards = [1 for _ in range(len(data))]
    for i, card in enumerate(data):
        card = card[card.index(":") + 2:]
        card = card.split("|")
        winning = card[0].split()
        playing = card[1].split()
        points = 0
        scratchies = 0

        for n in playing:
            if n in winning:
                if points == 0:
                    points = 1
                else:
                    points *= 2
                scratchies += 1

        score += points

        for n in range(scratchies):
            cards[i + n + 1] += cards[i]

    print(f"Points: {score}")
    print(f"Cards:  {sum(cards)}")
