import puzzleinput

numbers = puzzleinput.numbers
preamble_length = 25


def is_valid(number, preamble):
    for i, a in enumerate(preamble, 1):
        for b in preamble[i:]:
            if a + b == number:
                return True
    return False


for i, number in enumerate(numbers[preamble_length:], preamble_length):
    if not is_valid(number, numbers[i - preamble_length:i]):
        print(number)
        break
