input = open('input.txt', 'r').read().strip()

input_lines = [x for x in input.split("\n")]
bytes=input_lines
idx = 0
while(len(bytes) > 1):
    ctr = 0
    for byte in bytes:
        if byte[idx] == '1':
            ctr += 1
    if ctr >= len(bytes)/2:
        bytes = [x for x in bytes if x[idx] == '1']
    else:
        bytes = [x for x in bytes if x[idx] == '0']
    idx +=1
oxygen = int(bytes[0], 2)

bytes=input_lines
idx = 0
while(len(bytes) > 1):
    ctr = 0
    for byte in bytes:
        if byte[idx] == '1':
            ctr += 1
    if ctr < len(bytes)/2:
        bytes = [x for x in bytes if x[idx] == '1']
    else:
        bytes = [x for x in bytes if x[idx] == '0']
    idx +=1

carbon = int(bytes[0], 2)

result = oxygen*carbon
print("Result: {}".format(result))
