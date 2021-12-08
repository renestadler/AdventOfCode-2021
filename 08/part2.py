input = open('input.txt', 'r').read().strip()
lines = input.split("\n")
result = 0
for line in lines:
    inp, res = line.strip().split('|')
    inp = inp.split()
    res = res.split()
    combs = {}
    for c in inp:
        if len(c) == 7:
            combs[8] = ''.join(sorted(c))
        elif len(c) == 4:
            combs[4] = ''.join(sorted(c))
        elif len(c) == 3:
            combs[7] = ''.join(sorted(c))
        elif len(c) == 2:
            combs[1] = ''.join(sorted(c))

    for c in inp:
        if len(c) == 6:
            # 6 -> 1 not in it
            if not all([x in c for x in combs[1]]):
                combs[6] = ''.join(sorted(c))
            # 9 -> 4 in it
            elif all([x in c for x in combs[4]]):
                combs[9] = ''.join(sorted(c))
            else:
                combs[0] = ''.join(sorted(c))
    for c in inp:
        if len(c) == 5:
            # 3 -> 1 in it
            if all([x in c for x in combs[1]]):
                combs[3] = ''.join(sorted(c))
            # 9 -> cur in it
            elif all([x in combs[9] for x in c]):
                combs[5] = ''.join(sorted(c))
            else:
                combs[2] = ''.join(sorted(c))

    num = ''
    for c in res:
        test = ''.join(sorted(c))
        for k in combs.keys():
            if combs[k] == test:
                num = ''.join([num, str(k)])
    result += int(num)
print("Result: {}".format(result))
