import puzzleinput
import copy

lines = puzzleinput.lines

starting_instructions = []
for line in lines:
    operation, argument = line.split()
    argument = int(argument)
    starting_instructions.append((operation, argument))


def execute(instructions):
    acc = 0
    pointer = 0
    executed = []
    while True:
        if pointer == len(instructions):
            print(acc)
            return None
        executed.append(pointer)
        if executed.count(pointer) == 2:
            pattern = executed[executed.index(pointer):len(executed) - 1]
            return pattern
        operation, argument = instructions[pointer]
        if operation == "acc":
            acc += argument
            pointer += 1
        if operation == "jmp":
            pointer += argument
        if operation == "nop":
            pointer += 1


repeating_pattern = execute(starting_instructions)
for pointer in repeating_pattern:
    operation, argument = starting_instructions[pointer]
    if operation == "acc":
        continue
    operation = "jmp" if operation == "nop" else "nop"
    new_instructions = copy.copy(starting_instructions)
    new_instructions[pointer] = (operation, argument)
    if not execute(new_instructions):
        break
