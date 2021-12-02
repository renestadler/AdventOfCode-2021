input = open('input.txt', 'r').read().strip()

input_lines = [x for x in input.split("\n")]
input = [(x.split(" ")[0],int(x.split(" ")[1])) for x in input_lines]
horizontal = 0
depth = 0
for (marker, num) in input:
    if marker == "forward":
        horizontal+=num
    if marker == "down":
        depth+=num
    if marker == "up":
        depth-=num
result = horizontal*depth
print("Result: {}".format(result))

