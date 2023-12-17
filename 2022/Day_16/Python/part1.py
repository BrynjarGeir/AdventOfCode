from collections import defaultdict

file = '../data/test'
#file = '../data/input'

leads_to = {}
flow_rate = {}

with open(file) as f:
    lines = [line.replace('Valve ', '').replace('has flow rate=', '').replace('; tunnels lead to valves', '').replace('; tunnel leads to valve', '').replace(',', '').rstrip().split() for line in f.readlines()]

for line in lines:
    leads_to[line[0]] = line[2:]
    flow_rate[line[0]] = int(line[1])

time = 30
paths = [['AA']]
opn = defaultdict(lambda: False)

for i in range(0,time,2):
    tmp_paths = paths
    for index, path in enumerate(paths):
        if not opn[path[-1]]:
            opn[path[-1]] = True

print("HERE")