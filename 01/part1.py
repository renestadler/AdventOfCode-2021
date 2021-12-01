input = open('input.txt', 'r').read().strip()
elems = input.split("\n")

last = int(elems[0])
ctr = 0
for i in range(1, len(elems)):
    if (int(elems[i]) > last):
        ctr += 1
    last = int(elems[i])
result = ctr
print("Result: {}".format(result))
