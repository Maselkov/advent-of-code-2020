import puzzleinput


class SnapshotMatchException(Exception):
    pass


start_decks = []
deck = []
for line in puzzleinput.lines:
    if not line:
        start_decks.append(deck)
        deck = []
        continue
    if "Player" in line:
        continue
    deck.append(int(line))
start_decks.append(deck)


def recursive_combat(decks):
    previous_states = set()

    def determine_winner():
        snapshot = (tuple(decks[0]), tuple(decks[1]))
        if snapshot in previous_states:
            raise SnapshotMatchException
        previous_states.add(snapshot)
        if not decks[0]:
            return 1, 0
        elif not decks[1]:
            return 0, 1
        if decks[0][0] <= len(decks[0]) - 1 and decks[1][0] <= len(
                decks[1]) - 1:
            copy_decks = [d.copy()[1:d[0] + 1] for d in decks]
            winner_index, loser_index, _ = recursive_combat(copy_decks)
        else:
            if decks[0][0] > decks[1][0]:
                loser_index = 1
                winner_index = 0
            else:
                loser_index = 0
                winner_index = 1

        winner = decks[winner_index]
        loser = decks[loser_index]
        winner.append(winner.pop(0))
        winner.append(loser.pop(0))
        return winner_index, loser_index

    while decks[0] and decks[1]:
        try:
            i, j = determine_winner()
        except SnapshotMatchException:
            i = 0
            j = 1
            break
    return i, j, decks


total = 0

while start_decks[0] and start_decks[1]:
    i, j, end_deck = recursive_combat(start_decks)
for i, card in enumerate(reversed(end_deck[i]), start=1):
    total += i * card
print(total)
