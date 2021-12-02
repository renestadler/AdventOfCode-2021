input = open('input.txt', 'r').read().strip()
elems = [int(x) for x in input.split("\n")]

last = int(elems[0] + elems[1] + elems[2])
ctr = 0
for i in range(1, len(elems) - 2):
    if (elems[i] + elems[i + 1] + elems[i + 2] > last):
        ctr += 1
    last = elems[i] + elems[i + 1] + elems[i + 2]
result = ctr
print("Result: {}".format(result))
