import statistics

input = open('input.txt', 'r').read().strip()
input = [int(x) for x in input.split(",")]
result = 0
last = 100_000_000
for i in range (min(input), max(input)+1):
    cur = 0
    for val in input:
        cur += abs(i-val)
    if cur < last:
        last = cur
        result = i
print(result)
print(last)
result = last
print("Result: {}".format(result))
