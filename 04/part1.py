class Field:
    def __init__(self):
        self.field = []


input = open('input.txt', 'r').read().strip()
input = input.split("\n\n")
numbers = [int(x) for x in input[0].split(",")]
input = input[1:]
fields = []
for field in input:
    lines = field.split("\n")
    cur = Field()
    for line in lines:
        cur.field.append([int(x) for x in line.split()])
    fields.append(cur)

result = 0
done = False
for number in numbers:
    if not done:
        for field in fields:
            if not done:
                for i, line in enumerate(field.field):
                    for j, elem in enumerate(line):
                        if elem == number:
                            field.field[i][j] = -1
                transposed = [x for x in zip(*field.field)]
                for line in transposed:
                    if line.count(line[0]) == len(line):
                        done = True
                for line in field.field:
                    if line.count(line[0]) == len(line):
                        done = True
                if done:
                    for line in transposed:
                        for elem in line:
                            if elem != -1:
                                result += elem
                    result *= number

print("Result: {}".format(result))
