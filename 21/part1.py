input = open('input.txt', 'r').read().strip()
p1Pos = int(input.split("\n")[0].split(": ")[1])
p2Pos = int(input.split("\n")[1].split(": ")[1])
p1Score = 0
p2Score = 0
dice = 1
while p1Score < 1000 and p2Score < 1000:
    p1Pos += dice + dice + dice + 1 + 2
    p1Pos %= 10
    if p1Pos == 0:
        p1Pos = 10
    p1Score += p1Pos
    dice += 3
    if p1Score < 1000:
        p2Pos += dice + dice + dice + 1 + 2
        p2Pos %= 10
        if p2Pos == 0:
            p2Pos = 10
        p2Score += p2Pos
        dice += 3

result = (dice - 1) * (p1Score if p1Score < p2Score else p2Score)
print("Result: {}".format(result))
