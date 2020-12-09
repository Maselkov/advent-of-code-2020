import puzzleinput

numbers = puzzleinput.numbers
preamble_length = 25


def is_valid(number, preamble):
    for i, a in enumerate(preamble, 1):
        for b in preamble[i:]:
            if a + b == number:
                return True
    return False


def find_contagious_set(sum_target):
    for i, a in enumerate(numbers, 1):
        sum = a
        contagious_set = [a]
        if a >= sum_target:
            continue
        for b in numbers[i:]:
            sum += b
            contagious_set.append(b)
            if sum == sum_target:
                return contagious_set
            if sum > sum_target:
                break


vulnerability = None
for i, number in enumerate(numbers[preamble_length:], preamble_length):
    if not is_valid(number, numbers[i - preamble_length:i]):
        vulnerability = number
        break

result = sorted(find_contagious_set(vulnerability))
print(result[0] + result[-1])
