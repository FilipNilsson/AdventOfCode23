with open('input.txt') as file_:
    input_ = file_.read().splitlines()

nodes = {}
for line in input_[2:]:
    name, _, left, right = line.split()
    nodes[name] = (left[1:-1], right[:-1])

path = [int(x) for x in input_[0].replace('L', '0').replace('R', '1')]
path_length = len(path)
path_idx = 0

current_node = 'AAA'
jumps = 0
while current_node != 'ZZZ':
    current_node = nodes[current_node][path[path_idx]]
    path_idx = (path_idx + 1) % path_length
    jumps += 1
print(jumps)

# part 2
with open('input.txt') as file_:
    input_ = file_.read().splitlines()

nodes = {}
current_nodes = []
for line in input_[2:]:
    name, _, left, right = line.split()
    nodes[name] = (left[1:-1], right[:-1])
    if name.endswith('A'):
        current_nodes.append(name)

path = [int(x) for x in input_[0].replace('L', '0').replace('R', '1')]
path_length = len(path)
path_idx = 0

distances = []
for _ in current_nodes:
    distances.append(0)
current_nodes_length = len(current_nodes)
finished = False
jumps = 0
while not finished:
    finished = True
    for idx in range(current_nodes_length):
        if distances[idx]:
            continue
        current_nodes[idx] = nodes[current_nodes[idx]][path[path_idx]]
        if current_nodes[idx].endswith('Z'):
            distances[idx] = jumps + 1
        else:
            finished = False
    path_idx = (path_idx + 1) % path_length
    jumps += 1
from math import lcm
print(lcm(*distances))