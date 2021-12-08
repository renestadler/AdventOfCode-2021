input = open('input.txt', 'r').read().strip()

dict = {}
for line in input.split("\n"):
    elems = line.split(" -> ")
    x1 = int(elems[0].split(",")[0])
    y1 = int(elems[0].split(",")[1])
    x2 = int(elems[1].split(",")[0])
    y2 = int(elems[1].split(",")[1])
    if (x1 > x2):
        (x1, x2) = (x2, x1)
    if (y1 > y2):
        (y1, y2) = (y2, y1)
    if x1 == x2 or y1 == y2:
        for i in range(x2 - x1 + 1):
            for j in range(y2 - y1 + 1):
                value = str(x1 + i) + "," + str(y1 + j)
                if value in dict:
                    dict[value] = dict[value] + 1
                else:
                    dict[value] = 1
result = 0
for value in dict.values():
    if value != 1:
        result += 1
print("Result: {}".format(result))
