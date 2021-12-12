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
        if i != len(input)-1:
            validDown = input[i][j] < input[i + 1][j]
        if j != len(input[i])-1:
            validRight = input[i][j] < input[i][j + 1]
        if validUp and validLeft and validDown and validRight:
            points.append((i,j))
result = 0
for point in points:
    result += 1+input[point[0]][point[1]]
print("Result: {}".format(result))
