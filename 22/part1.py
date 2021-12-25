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
for area in areas:
    if -50 <= area[1] <= 50 and -50 <= area[2] <= 50 and -50 <= area[3] <= 50 and -50 <= area[4] <= 50 and -50 <= area[
        5] <= 50 and -50 <= area[6] <= 50:
        for i in range(area[1], area[2]+1):
            for j in range(area[3], area[4]+1):
                for k in range(area[5], area[6]+1):
                    pos[(i, j, k)] = area[0]

result = list(pos.values()).count(True)
print("Result: {}".format(result))
