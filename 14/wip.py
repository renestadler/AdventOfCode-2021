input = open('input.txt', 'r').read().strip()

elems = [x for x in input.split("\n")[0]]
map = {(line.split(" -> ")[0][0], line.split(" -> ")[0][1]): line.split(" -> ")[1] for line in input.split("\n")[2:]}

pairs = {}
for e in zip(elems, elems[1:]):
    if e in pairs:
        pairs[e] += 1
    else:
        pairs[e] = 1
for i in range(40):
    newpairs = {}
    for pair in pairs:
        if map[pair]:
            e = (pair[0], map[pair])
            if e in newpairs:
                newpairs[e] += pairs[pair]
            else:
                newpairs[e] = pairs[pair]
            e = (map[pair], pair[1])
            if e in newpairs:
                newpairs[e] += pairs[pair]
            else:
                newpairs[e] = pairs[pair]
    pairs = newpairs
last = elems[::-1][0]
elems = dict()
for pair in pairs.items():
    if pair[0][0] in elems:
        elems[pair[0][0]] += pair[1]
    else:
        elems[pair[0][0]] = pair[1]
    if pair[0][1] in elems:
        elems[pair[0][1]] += pair[1]
    else:
        elems[pair[0][1]] = pair[1]

elems = {x: y // 2 for x, y in elems.items()}
elems[last] += 1
result = max(elems.values()) - min(elems.values())
print("Result: {}".format(result))
