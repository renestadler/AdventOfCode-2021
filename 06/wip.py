input = open('input.txt', 'r').read().strip()

input = [int(x) for x in input.split(",")]

cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0,0]
for i in input:
    cnt[i + 1] += 1
for i in range(256):
    for j in range(1, len(cnt)):
        cnt[j - 1] = cnt[j]
    cnt[7] += cnt[0]
    cnt[9] = cnt[0]
    cnt[0] = 0
result = sum(cnt)
print("Result: {}".format(result))
