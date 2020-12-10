import puzzleinput

adapters = sorted(puzzleinput.numbers)
adapters.insert(0, 0)
adapters.reverse()
cache = {}


def get_possibility_count(node):
    if node in cache:
        return cache[node]
    possibilities = 0
    for adapter in adapters:
        difference = node - adapter
        if 0 < difference <= 3:
            if adapter == 0:
                possibilities += 1
            possibilities += get_possibility_count(adapter)
    cache[node] = possibilities
    return possibilities


print(get_possibility_count(adapters[0]))
