import puzzleinput

lines = puzzleinput.lines

instructions = []
for line in lines:
    operation, argument = line.split()
    argument = int(argument)
    instructions.append((operation, argument))

acc = 0
pointer = 0
executed_instructions = []
while True:
    executed_instructions.append(pointer)
    operation, argument = instructions[pointer]
    if operation == "acc":
        acc += argument
        pointer += 1
    if operation == "jmp":
        pointer += argument
    if operation == "nop":
        pointer += 1
    if pointer in executed_instructions:
        print(acc)
        break
