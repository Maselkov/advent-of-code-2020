import puzzleinput

mask = []
mem = {}
for line in puzzleinput.lines:
    op, value = line.split(" = ")
    if op == "mask":
        mask = [int(m) if m.isdigit() else None for m in value]
        continue
    else:
        address = int(op[4:-1])
        value = int(value)
        value = [int(x) for x in bin(value)[2:]]
        value = ([0] * (36 - len(value))) + value
        for i, bit in enumerate(mask):
            if bit is not None:
                value[i] = bit

        mem[address] = int("".join(str(x) for x in value), 2)

print(sum(mem.values()))
