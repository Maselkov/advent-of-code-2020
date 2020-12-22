import puzzleinput

decks = []
deck = []
for line in puzzleinput.lines:
    if not line:
        decks.append(deck)
        deck = []
        continue
    if "Player" in line:
        continue
    deck.append(int(line))

decks.append(deck)
while decks[0] and decks[1]:
    if decks[0][0] > decks[1][0]:
        loser = decks[1]
        winner = decks[0]
    else:
        loser = decks[0]
        winner = decks[1]
    winner.append(winner.pop(0))
    winner.append(loser.pop(0))

total = 0
for i, card in enumerate(reversed(winner), start=1):
    total += i * card
print(total)
