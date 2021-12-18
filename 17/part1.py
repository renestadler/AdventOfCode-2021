input = open('input.txt', 'r').read().strip()

x = input.split("x=")[1].split(", ")[0].split("..")
y = input.split("y=")[1].split("..")
xStart = int(x[0])
xEnd = int(x[1])
yStart = int(y[0])
yEnd = int(y[1])
maxY = 0
maxYPos = 0

for i in range(5, 200):
    for j in range(5, 200):
        x = 0
        y = 0
        xVelocity = i
        yVelocity = j
        max = 0
        found = False
        while x < xEnd and y > yEnd:
            x += xVelocity
            y += yVelocity
            if max < y:
                max = y
            if xVelocity < 0:
                xVelocity += 1
            elif xVelocity > 0:
                xVelocity -= 1
            yVelocity -= 1
            if x >= xStart and x <= xEnd and y >= yStart and y <= yEnd:
                found = True
        if found and j >= maxY:
            maxY = j
            maxYPos = max

result = maxYPos
print("Result: {}".format(result))
