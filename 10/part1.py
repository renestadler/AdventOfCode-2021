input = open('input.txt', 'r').read().strip()
result = 0
for line in input.split("\n"):
    queue = []
    for char in line:
        if char == '{' or char == '[' or char == '(' or char == '<':
            queue.append(char)
        elif char == '}' or char == ']' or char == ')' or char == '>':
            elem = queue.pop()
            if char == ')' and elem != '(':
                result += 3
            elif char == ']' and elem != '[':
                result += 57
            elif char == '}' and elem != '{':
                result += 1197
            elif char == '>' and elem != '<':
                result += 25137
print("Result: {}".format(result))
