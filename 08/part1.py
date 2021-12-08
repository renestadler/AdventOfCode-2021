input = open('input.txt', 'r').read().strip()
input = input.split("\n")
lines = [x.split("|")[1] for x in input]
lines = [x.split(" ") for x in lines]
lines = [x for line in lines for x in line if len(x) in (2,3,4,7)]
result = len(lines)
print("Result: {}".format(result))
