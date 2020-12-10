import puzzleinput

adapters = sorted(puzzleinput.numbers)
adapters.append(adapters[-1]+3)

one_diffs = 0
three_diffs = 0
jolts = 0
for adapter in adapters:
    difference = adapter - jolts
    if difference <= 3:
        jolts += difference
        if difference == 1:
            one_diffs += 1
        if difference == 3:
            three_diffs += 1

print(one_diffs * three_diffs)
