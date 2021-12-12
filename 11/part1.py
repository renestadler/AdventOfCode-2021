input = open('input.txt', 'r').read().strip()
input = [x for x in input.split("\n")]
input = [[int(y) for y in x] for x in input]

result = 0
for i in range(100):
    input = [[y + 1 for y in x] for x in input]
    allPos = {(i, j) for i, x in enumerate(input) for j, y in enumerate(x) if y > 9}
    flashingPos = {(i, j) for i, x in enumerate(input) for j, y in enumerate(x) if y > 9}
    while len(flashingPos) > 0:
        pos = flashingPos.pop()
        if pos[0] > 0:
            input[pos[0] - 1][pos[1]] += 1
            if input[pos[0] - 1][pos[1]] > 9 and (pos[0] - 1, pos[1]) not in allPos:
                flashingPos.add((pos[0] - 1, pos[1]))
                allPos.add((pos[0] - 1, pos[1]))
            if pos[1] > 0:
                input[pos[0] - 1][pos[1] - 1] += 1
                if input[pos[0] - 1][pos[1] - 1] > 9 and (pos[0] - 1, pos[1] - 1) not in allPos:
                    flashingPos.add((pos[0] - 1, pos[1] - 1))
                    allPos.add((pos[0] - 1, pos[1] - 1))
            if pos[1] < 9:
                input[pos[0] - 1][pos[1] + 1] += 1
                if input[pos[0] - 1][pos[1] + 1] > 9 and (pos[0] - 1, pos[1] + 1) not in allPos:
                    flashingPos.add((pos[0] - 1, pos[1] + 1))
                    allPos.add((pos[0] - 1, pos[1] + 1))
        if pos[0] < 9:
            input[pos[0] + 1][pos[1]] += 1
            if input[pos[0] + 1][pos[1]] > 9 and (pos[0] + 1, pos[1]) not in allPos:
                flashingPos.add((pos[0] + 1, pos[1]))
                allPos.add((pos[0] + 1, pos[1]))
            if pos[1] > 0:
                input[pos[0] + 1][pos[1] - 1] += 1
                if input[pos[0] + 1][pos[1] - 1] > 9 and (pos[0] + 1, pos[1] - 1) not in allPos:
                    flashingPos.add((pos[0] + 1, pos[1] - 1))
                    allPos.add((pos[0] + 1, pos[1] - 1))
            if pos[1] < 9:
                input[pos[0] + 1][pos[1] + 1] += 1
                if input[pos[0] + 1][pos[1] + 1] > 9 and (pos[0] + 1, pos[1] + 1) not in allPos:
                    flashingPos.add((pos[0] + 1, pos[1] + 1))
                    allPos.add((pos[0] + 1, pos[1] + 1))
        if pos[1] > 0:
            input[pos[0]][pos[1] - 1] += 1
            if input[pos[0]][pos[1] - 1] > 9 and (pos[0], pos[1] - 1) not in allPos:
                flashingPos.add((pos[0], pos[1] - 1))
                allPos.add((pos[0], pos[1] - 1))
        if pos[1] < 9:
            input[pos[0]][pos[1] + 1] += 1
            if input[pos[0]][pos[1] + 1] > 9 and (pos[0], pos[1] + 1) not in allPos:
                flashingPos.add((pos[0], pos[1] + 1))
                allPos.add((pos[0], pos[1] + 1))
    result += len(allPos)
    for pos in allPos:
        input[pos[0]][pos[1]] = 0

print("Result: {}".format(result))
