input = open('input.txt', 'r').read().strip()

field = [[int(y) for y in x] for x in input.split("\n")]
visited = [[False for y in x] for x in input.split("\n")]
visited[0][0] = True
steps = []
steps.append((0, 0, 6))
steps.append((0, 0, 0))
steps.append((0, 0, 4))
while len(steps) > 0:
    steps = sorted(steps, key=lambda x: x[2], reverse=True)
    step = steps.pop()
    if (step[0] == len(field) - 1 and step[1] == len(field[0]) - 1):
        result = step[2]
        break
    if step[0] > 0 and not visited[step[0] - 1][step[1]]:
        steps.append((step[0] - 1, step[1], step[2] + field[step[0] - 1][step[1]]))
        visited[step[0] - 1][step[1]] = True
    if step[1] > 0 and not visited[step[0]][step[1] - 1]:
        steps.append((step[0], step[1] - 1, step[2] + field[step[0]][step[1] - 1]))
        visited[step[0]][step[1] - 1] = True
    if step[0] < len(field) - 1 and not visited[step[0] + 1][step[1]]:
        steps.append((step[0] + 1, step[1], step[2] + field[step[0] + 1][step[1]]))
        visited[step[0] + 1][step[1]] = True
    if step[1] < len(field[0]) - 1 and not visited[step[0]][step[1] + 1]:
        steps.append((step[0], step[1] + 1, step[2] + field[step[0]][step[1] + 1]))
        visited[step[0]][step[1] + 1] = True
print("Result: {}".format(result))
