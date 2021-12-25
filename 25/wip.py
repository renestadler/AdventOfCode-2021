input = open('input.txt', 'r').read().strip()
lines = input.split("\n")

rightCucumbers = set()
downCucumbers = set()
xLen = len(lines)
yLen = len(lines[0])
for i, line in enumerate(lines):
    for j, x in enumerate(line):
        if x == '>':
            rightCucumbers.add((i, j))
        elif x == 'v':
            downCucumbers.add((i, j))
someMove = True
counter = 0
while someMove:
    counter += 1
    someMove = False
    newRightCucumbers = set()
    newDownCucumbers = set()
    for cucumber in rightCucumbers:
        pos = (cucumber[0], (cucumber[1] + 1) % yLen)
        if pos not in rightCucumbers and pos not in downCucumbers:
            newRightCucumbers.add(pos)
            someMove = True
        else:
            newRightCucumbers.add(cucumber)
    rightCucumbers = newRightCucumbers
    for cucumber in downCucumbers:
        pos = ((cucumber[0] + 1) % xLen, cucumber[1])
        if pos not in rightCucumbers and pos not in downCucumbers:
            newDownCucumbers.add(pos)
            someMove = True
        else:
            newDownCucumbers.add(cucumber)
    downCucumbers = newDownCucumbers
result = counter
print("Result: {}".format(result))
