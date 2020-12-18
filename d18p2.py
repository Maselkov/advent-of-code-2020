import puzzleinput
import operator

signs = {"+": operator.add, "*": operator.mul}


def evaluate(expression):
    while True:
        for i in range(1, len(expression), 2):
            sign = expression[i]
            if sign != operator.add:
                continue
            expression[i - 1:i +
                       2] = [sign(expression[i - 1], expression[i + 1])]
            break
        else:
            break
    count = expression[0]
    for i in range(1, len(expression), 2):
        count = expression[i](count, expression[i + 1])
    return count


def evaluate_parentheses(line, start_pos):
    if line[start_pos] != "(":
        raise ValueError
    for i in range(start_pos + 1, len(line)):
        if line[i] == "(":
            end_pos, value = evaluate_parentheses(line, i)
            line[i:end_pos] = value
        if line[i] == ")":
            return i + 1, [evaluate(line[start_pos + 1:i])]


total = 0
for line in puzzleinput.lines:
    line = line.split(" ")
    added_index = 0
    line_copy = line.copy()
    for i, element in enumerate(line):
        left_parentheses = [c for c in element if c == "("]
        right_parentheses = [c for c in element if c == ")"]
        number = "".join(c for c in element if c.isdigit())
        if number:
            line_copy[i + added_index] = int(number)
        elif element in signs:
            line_copy[i + added_index] = signs[element]
        for p in left_parentheses:
            line_copy.insert(i + added_index, "(")
            added_index += 1
        for p in right_parentheses:
            line_copy.insert(i + 1 + added_index, ")")
            added_index += 1
    line = line_copy
    while True:
        for i, element in enumerate(line):
            if element == "(":
                end, value = evaluate_parentheses(line, i)
                line[i:end] = value
                break
        else:
            break
    total += evaluate(line)
print(total)
