input = open('input.txt', 'r').read().strip()
results = []
for line in input.split("\n"):
    queue = []
    invalid = False
    for char in line:
        if char == '{' or char == '[' or char == '(' or char == '<':
            queue.append(char)
        elif char == '}' or char == ']' or char == ')' or char == '>':
            elem = queue.pop()
            if char == ')' and elem != '(':
                invalid = True
            elif char == ']' and elem != '[':
                invalid = True
            elif char == '}' and elem != '{':
                invalid = True
            elif char == '>' and elem != '<':
                invalid = True
    if not invalid:
        result = 0
        for char in queue[::-1]:
            result *= 5
            if char == '(':
                result += 1
            elif char == '[':
                result += 2
            elif char == '{':
                result += 3
            elif char == '<':
                result += 4
        results.append(result)
result = sorted(results)[int(len(results) / 2)]
print("Result: {}".format(result))
