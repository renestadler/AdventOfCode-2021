input = open('input.txt', 'r').read().strip()

#input = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678"
input = [x for x in input.split("\n")]
input = [[int(y) for y in x] for x in input]
points = []
for i in range(len(input)):
    for j in range(len(input[i])):
        validUp = True
        validDown = True
        validLeft = True
        validRight = True
        if i != 0:
            validUp = input[i][j] < input[i - 1][j]
        if j != 0:
            validLeft = input[i][j] < input[i][j - 1]
        if i != len(input) - 1:
            validDown = input[i][j] < input[i + 1][j]
        if j != len(input[i]) - 1:
            validRight = input[i][j] < input[i][j + 1]
        if validUp and validLeft and validDown and validRight:
            points.append((i, j))
basins = []
for point in points:
    allPoints = {point}
    pointList = [point]
    while len(pointList) != 0:
        curPoint = pointList.pop()
        allPoints.add(curPoint)
        input[curPoint[0]][curPoint[1]] = -1
        if curPoint[0] != 0 and input[curPoint[0] - 1][curPoint[1]] != -1 and input[curPoint[0] - 1][curPoint[1]] != 9:
            pointList.append((curPoint[0] - 1, curPoint[1]))
        if curPoint[1] != 0 and input[curPoint[0]][curPoint[1] - 1] != -1 and input[curPoint[0]][curPoint[1] - 1] != 9:
            pointList.append((curPoint[0], curPoint[1] - 1))
        if curPoint[0] != len(input) - 1 and input[curPoint[0] + 1][curPoint[1]] != -1 and input[curPoint[0] + 1][curPoint[1]] != 9:
            pointList.append((curPoint[0] + 1, curPoint[1]))
        if curPoint[1] != len(input[0]) - 1 and input[curPoint[0]][curPoint[1] + 1] != -1 and input[curPoint[0]][curPoint[1] + 1] != 9:
            pointList.append((curPoint[0], curPoint[1] + 1))
    basins.append(len(allPoints))
basins = sorted(basins, reverse=True)
result = basins[0]*basins[1]*basins[2]
print("Result: {}".format(result))
