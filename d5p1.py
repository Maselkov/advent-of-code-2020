import puzzleinput

lines = puzzleinput.lines

highest_sid = 0
for boarding_pass in lines:
    row = boarding_pass[:7]
    column = boarding_pass[7:]
    row = [0 if c == "F" else 1 for c in row]
    column = [0 if c == "L" else 1 for c in column]
    row = int("".join(str(i) for i in row), 2)
    column = int("".join(str(i) for i in column), 2)
    sid = row * 8 + column
    if sid > highest_sid:
        highest_sid = sid
print(highest_sid)
