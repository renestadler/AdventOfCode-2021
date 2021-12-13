input = open('input.txt', 'r').read().strip()

dots = []
instructions = []
phaseTwo = False
for line in input.split("\n"):
    if line == "":
        phaseTwo = True
    elif not phaseTwo:
        dots.append((int(line.split(",")[0]), (int(line.split(",")[1]))))
    else:
        instructions.append((line.split("=")[0] == "fold along x", int(line.split("=")[1])))
for instruction in instructions:
    if instruction[0]:
        dots = [d for d in dots if d[0] != instruction[1]]
        temp = [(instruction[1] - (d[0] - instruction[1]), d[1]) for d in dots if d[0] > instruction[1]]
        dots = [d for d in dots if d[0] < instruction[1]]
        dots.extend(temp)
        dots = list(set(dots))
    else:
        dots = [d for d in dots if d[1] != instruction[1]]
        temp = [(d[0], instruction[1] - (d[1] - instruction[1])) for d in dots if d[1] > instruction[1]]
        dots = [d for d in dots if d[1] < instruction[1]]
        dots.extend(temp)
        dots = list(set(dots))
for j in range(8):
    for i in range(40):
        if (i, j) in dots:
            print("#", end='')
        else:
            print(".", end='')
    print("")
result = "AHGCPGAU"
print("Result: {}".format(result))
