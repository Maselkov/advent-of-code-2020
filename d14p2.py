import puzzleinput
import itertools


def get_masks(mask):
    floats = mask.count(None)
    values = list([r for r in itertools.product([0, 1], repeat=floats)])
    masks = []
    for option in values:
        new = mask.copy()
        j = 0
        for i, bit in enumerate(new):
            if bit is None:
                new[i] = option[j]
                j += 1
            if bit == 0:
                new[i] = None
        masks.append(new)
    return masks


masks = []
mem = {}
for line in puzzleinput.lines:
    op, value = line.split(" = ")
    if op == "mask":
        masks = get_masks([int(m) if m.isdigit() else None for m in value])
        continue
    else:
        address = int(op[4:-1])
        value = int(value)
        address = [int(x) for x in bin(address)[2:]]
        address = ([0] * (36 - len(address))) + address
        for mask in masks:
            new_address = address.copy()
            for i, bit in enumerate(mask):
                if bit is not None:
                    new_address[i] = bit

            new_address = int("".join(str(x) for x in new_address), 2)
            diff = new_address - len(mem) + 1
            mem[new_address] = value

print(sum(mem.values()))
