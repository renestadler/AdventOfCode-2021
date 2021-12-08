input = open('input.txt', 'r').read().strip()

input = [int(x) for x in input.split(",")]

for i in range(80):
    for j in range(len(input)):
        input[j] -= 1
        if (input[j] == -1):
            input[j] = 6
            input.append(8)
result = len(input)
print("Result: {}".format(result))
