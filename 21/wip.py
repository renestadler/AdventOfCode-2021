from collections import defaultdict

input = open('input.txt', 'r').read().strip()

roll_counts = []
for _ in range(10):
    roll_counts.append(0)
    # count how many different ways there are to roll each possible value
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            roll_counts[i + j + k] += 1
p1Pos = int(input.split("\n")[0].split(": ")[1])
p2Pos = int(input.split("\n")[1].split(": ")[1])

states = {(p1Pos, p2Pos, 0, 0): 1}
p1Wins = 0
p2Wins = 0
p1Turn = True
dice = 1
while len(states) > 0:
    new_states = defaultdict(int)
    for s in states.keys():
        for roll in range(3, 10):
            if p1Turn:
                p1Pos = (s[0] + roll - 1) % 10 + 1  # move the piece
                new_score = s[2] + p1Pos  # updat the score
                if new_score >= 21:
                    p1Wins += states[s] * roll_counts[roll]
                else:
                    new_states[(p1Pos, s[1], new_score, s[3])] += states[s] * roll_counts[roll]
            else:
                p2Pos = (s[1] + roll - 1) % 10 + 1
                new_score = s[3] + p2Pos
                if new_score >= 21:
                    p2Wins += states[s] * roll_counts[roll]
                else:
                    new_states[(s[0], p2Pos, s[2], new_score)] += states[s] * roll_counts[roll]
    p1Turn = not p1Turn
    states = new_states
result = p1Wins if p1Wins > p2Wins else p2Wins
print("Result: {}".format(result))
