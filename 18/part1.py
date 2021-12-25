from math import ceil

input = open('input.txt', 'r').read().strip()

lines = input.splitlines()


def explode(line, pos=0, depth=0, done=False):
    while pos < len(line):
        depth = depth + 1 if line[pos] == '[' else (depth - 1 if line[pos] == ']' else depth)
        if depth == 5:
            left, right = [int(x.strip()) for x in line[pos + 1: pos + line[pos:].index(']')].split(',')]
            line = line[:pos] + '0' + line[pos + line[pos:].index(']') + 1:]
            left_number = next((i + 1 for i, x in enumerate(line[:pos][::-1]) if x.isdigit()), None)
            right_number = next((i + 1 for i, x in enumerate(line[pos + 1:]) if x.isdigit()), None)
            if right_number:
                enum = right_number
                while line[pos + enum].isdigit():
                    enum += 1
                line = line[:pos + right_number] + str(int(line[pos + right_number: pos + enum]) + right) + line[
                                                                                                            enum + pos:]
            if left_number:
                enum, temp = left_number, []
                while line[pos - enum].isdigit():
                    temp.append(pos - enum)
                    enum += 1
                line = line[:min(temp)] + str(int(line[min(temp): max(temp) + 1]) + left) + line[max(temp) + 1:]
            pos, depth = -1, 0
            done = True
        pos += 1
    return done, line


def split_number(line, done=False):
    digit = next((int(y) for y in ''.join([x for x in line if x.isdigit() or x == ',']).split(',') if int(y) > 9), None)
    if digit:
        line = line[:line.index(str(digit))] + \
               '[{},{}]'.format(digit // 2, ceil(digit / 2)) + \
               line[line.index(str(digit)) + len(str(digit)):]
        done = True
    return done, line


def solve(line, success=True):
    while success:
        while success:
            success, line = explode(line)
        success, line = split_number(line)
    return line


def magnitude(row):
    while '[' in row:
        pos = 0
        while pos < len(row):
            if row[pos].isdigit():
                if not '[' in row[pos:] or row[pos:].index('[') > row[pos:].index(']'):
                    left, right = [int(x) for x in row[pos: row.index(']')].split(',')]
                    row = row[:pos - 1] + str(left * 3 + right * 2) + row[row.index(']') + 1:]
                    break
            pos += 1
    return int(row)


for i, x in enumerate(lines):
    lines[i] = solve(x)
end = lines[0]
for x in lines[1:]:
    end = solve('[{},{}]'.format(end, x))

result = magnitude(end)
print("Result: {}".format(result))
