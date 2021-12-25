input = open('input.txt', 'r').read().strip()
results = input.split("\n")[0]
image = input.split("\n\n")[1]
elems = {}
for i, line in enumerate(image.split("\n")):
    for j, elem in enumerate(line):
        elems[(i, j)] = elem

for k in range(2):

    newelems = {}
    minX = min(elems.keys(), key=lambda t: t[0])[0]
    maxX = max(elems.keys(), key=lambda t: t[0])[0]
    minY = min(elems.keys(), key=lambda t: t[1])[1]
    maxY = max(elems.keys(), key=lambda t: t[1])[1]
    for i in range(minX - 1, maxX + 2):
        for j in range(minY - 1, maxY + 2):
            pos = (i, j)
            num = 0
            if (pos[0] - 1, pos[1] - 1) in elems:
                num += 1 if elems[(pos[0] - 1, pos[1] - 1)] == '#' else 0
            else:
                num += k % 2
            num *= 2
            if (pos[0] - 1, pos[1]) in elems:
                num += 1 if elems[(pos[0] - 1, pos[1])] == '#' else 0
            else:
                num += k % 2
            num *= 2
            if (pos[0] - 1, pos[1] + 1) in elems:
                num += 1 if elems[(pos[0] - 1, pos[1] + 1)] == '#' else 0
            else:
                num += k % 2
            num *= 2
            if (pos[0], pos[1] - 1) in elems:
                num += 1 if elems[(pos[0], pos[1] - 1)] == '#' else 0
            else:
                num += k % 2
            num *= 2
            if (pos[0], pos[1]) in elems:
                num += 1 if elems[(pos[0], pos[1])] == '#' else 0
            else:
                num += k % 2
            num *= 2
            if (pos[0], pos[1] + 1) in elems:
                num += 1 if elems[(pos[0], pos[1] + 1)] == '#' else 0
            else:
                num += k % 2
            num *= 2
            if (pos[0] + 1, pos[1] - 1) in elems:
                num += 1 if elems[(pos[0] + 1, pos[1] - 1)] == '#' else 0
            else:
                num += k % 2
            num *= 2
            if (pos[0] + 1, pos[1]) in elems:
                num += 1 if elems[(pos[0] + 1, pos[1])] == '#' else 0
            else:
                num += k % 2
            num *= 2
            if (pos[0] + 1, pos[1] + 1) in elems:
                num += 1 if elems[(pos[0] + 1, pos[1] + 1)] == '#' else 0
            else:
                num += k % 2
            if num != 0 and num != len(results) - 1:
                newelems[(pos[0], pos[1])] = results[num]
            elif minX <= i <= maxX and minY <= j <= maxY:
                newelems[(pos[0], pos[1])] = results[num]

    elems = newelems
result = list(elems.values()).count('#')
print("Result: {}".format(result))