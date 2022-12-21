#data = "../data/test.txt"
data = "../data/input.txt"

with open(data) as f:
    lines = [line.rstrip().split() for line in f]

points = {'X':1, 'Y':2, 'Z':3}
to_win = {'C':'X', 'A':'Y', 'B':'Z'}
to_draw = {'A':'X', 'B':'Y', 'C':'Z'}
to_loose = {'B':'X', 'C':'Y', 'A':'Z'}
win_points = 6
draw_points = 3
loose_points = 0

score = 0

for line in lines:
    strategy = line[1]
    opponent = line[0]
    if strategy == 'X':
        played = to_loose[opponent]
        score += points[played] + loose_points
    elif strategy == 'Y':
        played = to_draw[opponent]
        score += points[played] + draw_points
    else:
        played = to_win[opponent]
        score += points[played] + win_points

print(score)