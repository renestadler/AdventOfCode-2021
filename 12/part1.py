input = open('input.txt', 'r').read().strip()

caves = {}
paths = []

for path in [x.strip() for x in input.split("\n")]:
    one, two = path.split('-')
    caves.setdefault(one, []).append(two)
    caves.setdefault(two, []).append(one)


def walk(cur, visited):
    visited.append(cur)
    for val in caves[cur]:
        if val.isupper() or val not in visited:
            walk(val, visited.copy())
    paths.append(visited)


walk('start', [])
result = len([p for p in paths if p[-1] == 'end'])
print("Result: {}".format(result))
