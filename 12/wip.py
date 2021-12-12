from collections import Counter

input = open('input.txt', 'r').read().strip()

caves = {}
paths = []

for path in [x.strip() for x in input.split("\n")]:
    one, two = path.split('-')
    caves.setdefault(one, []).append(two)
    caves.setdefault(two, []).append(one)


def walk(cur, visited):
    visited.append(cur)
    numLower = {n: c for n, c in Counter(visited).items() if n.islower() and len(n) < 3 and c >= 2}
    for n in caves[cur]:
        if n.isupper() or (len(n) < 3 and len(numLower.keys()) == 0) or n not in visited:
            walk(n, visited.copy())
    paths.append(visited)


walk('start', [])
result = len([p for p in paths if p[-1] == 'end'])
print("Result: {}".format(result))
