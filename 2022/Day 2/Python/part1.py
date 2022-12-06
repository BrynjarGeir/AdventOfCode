#data = "../data/test.txt"
data = "../data/input.txt"

with open(data) as f:
    lines = [line.rstrip().split() for line in f]

points = {'X':1, 'Y':2, 'Z':3}
wins = {'X':'C', 'Y':'A', 'Z':'B'}
draws = {'X':'A', 'Y':'B', 'Z':'C'}
win_points = 6
draw_points = 3
loose_points = 0

score = 0

for line in lines:
    player = line[1]
    opponent = line[0]
    score += points[player]
    if wins[player] == opponent:
        score += win_points
    elif draws[player] == opponent:
        score += draw_points
    else:
        score += loose_points


print(score)