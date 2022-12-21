import pickle

# Load resulting dictionary from part 1
with open('../data/file_system.pkl', 'rb') as f:
    file_system = pickle.load(f)


required_space, total_space, used_space = 30000000, 70000000, file_system['/'][0]
free_space = None

free_space = total_space - used_space
need_to_free = required_space - free_space

min_needed = float('inf')

for directory in file_system:
    if file_system[directory][0] >= need_to_free:
        min_needed = min(min_needed, file_system[directory][0])

print(min_needed)