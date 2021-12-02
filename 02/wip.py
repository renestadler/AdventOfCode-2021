input = open('input.txt', 'r').read().strip()

input_lines = [x for x in input.split("\n")]
input = [(x.split(" ")[0],int(x.split(" ")[1])) for x in input_lines]
horizontal = 0
depth=0
aim = 0
for (marker, num) in input:
    if marker == "forward":
        horizontal+=num
        depth+=num*aim
    if marker == "down":
        aim+=num
    if marker == "up":
        aim-=num
result = horizontal*depth
print("Result: {}".format(result))

