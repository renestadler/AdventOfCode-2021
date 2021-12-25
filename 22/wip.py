input = open('input.txt', 'r').read().strip()
lines = input.split("\n")
areas = []
for line in lines:
    on = True if line.split(" ")[0] == "on" else False
    regions = line.split(" ")[1].split(",")
    x = regions[0].split("=")[1].split("..")
    y = regions[1].split("=")[1].split("..")
    z = regions[2].split("=")[1].split("..")
    areas.append((on, int(x[0]), int(x[1]), int(y[0]), int(y[1]), int(z[0]), int(z[1])))
pos = {}

cubes = []
for area in areas:
    (op, startX, endX, startY, endY, startZ, endZ) = area
    for i in range(len(cubes)):
        (startX2, endX2, startY2, endY2, startZ2, endZ2) = cubes[i]
        if startX > endX2 or endX < startX2 or startY > endY2 or endY < startY2 or startZ > endZ2 or endZ < startZ2:
            continue
        cubes[i] = None
        if startX > startX2:
            cubes.append((startX2, startX - 1, startY2, endY2, startZ2, endZ2))
        if endX < endX2:
            cubes.append((endX + 1, endX2, startY2, endY2, startZ2, endZ2))
        if startY > startY2:
            cubes.append((max(startX2, startX), min(endX2, endX), startY2, startY - 1, startZ2, endZ2))
        if endY < endY2:
            cubes.append((max(startX2, startX), min(endX2, endX), endY + 1, endY2, startZ2, endZ2))
        if startZ > startZ2:
            cubes.append(
                (max(startX2, startX), min(endX2, endX), max(startY2, startY), min(endY2, endY), startZ2, startZ - 1))
        if endZ < endZ2:
            cubes.append(
                (max(startX2, startX), min(endX2, endX), max(startY2, startY), min(endY2, endY), endZ + 1, endZ2))
    if op:
        cubes.append((min(startX, endX), max(startX, endX), min(startY, endY), max(startY, endY), min(startZ, endZ),
                      max(startZ, endZ)))
    cubes = [cube for cube in cubes if cube is not None]
result = 0
for cube in cubes:
    [startX, endX, startY, endY, startZ, endZ] = cube
    result += (endX - startX + 1) * (endY - startY + 1) * (endZ - startZ + 1)
print("Result: {}".format(result))
