input = open('input.txt', 'r').read().strip()

elems = [x for x in input.split("\n")[0]]
map = {(line.split(" -> ")[0][0], line.split(" -> ")[0][1]): line.split(" -> ")[1] for line in input.split("\n")[2:]}

for i in range(10):
    newelems=[]
    for e in zip(elems,elems[1:]):
        if map[e]:
            newelems.append(e[0])
            newelems.append(map[e])
    newelems.append(elems[len(elems)-1])
    elems = newelems
result = elems.count(max(set(elems), key = elems.count))-elems.count(min(set(elems), key = elems.count))
print("Result: {}".format(result))
