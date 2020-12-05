import puzzleinput

lines = puzzleinput.lines

sids = []
for boarding_pass in lines:
    row = boarding_pass[:7]
    column = boarding_pass[7:]
    row = [0 if c == "F" else 1 for c in row]
    column = [0 if c == "L" else 1 for c in column]
    row = int("".join(str(i) for i in row), 2)
    column = int("".join(str(i) for i in column), 2)
    sid = row * 8 + column
    sids.append(sid)
sids.sort()
for i, sid in enumerate(sids):
    if sids[i + 1] == sid + 2:
        print(sid + 1)
        break
