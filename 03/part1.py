input = open('input.txt', 'r').read().strip()

input_lines = [int(x) for x in input.split("\n")]
bytes=[]
for line in input_lines:
    ctr = 0
    temp = line
    while temp > 0:
        if len(bytes)==ctr:
            bytes.append(0)
        if temp%10 == 1:
            bytes[ctr] += 1
        temp //= 10
        ctr += 1
gamma = 0
epsilon = 0
bytes = bytes[::-1]
for item in bytes:
    gamma *= 2
    epsilon *= 2
    if item < len(input_lines)/2:
        epsilon +=1
    if item > len(input_lines)/2:
        gamma +=1

result = gamma*epsilon
print("Result: {}".format(result))
