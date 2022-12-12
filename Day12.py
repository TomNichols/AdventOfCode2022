import string
import heapq

filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day12\input.txt"
test = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day12\test_input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def map_heights(char):
    if char == "E":
        return "z"
    elif char == "S":
        return "a"
    else:
        return char

def create_graph(map):
    '''Creates a dict mapping points to the neighbouring nodes they can reach'''
    graph = {}
    start = goal = None
    for y in range(len(map)):
        for x in range(len(map[0])):
            graph[(x,y)] = []
            if map[y][x] == "S":
                start = (x,y)
                continue
            if map[y][x] == "E":
                goal = (x,y)
            for i, j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                try:
                    if j >= 0 and i >= 0:
                        elevation = string.ascii_lowercase.index(map_heights(map[j][i])) - string.ascii_lowercase.index(map_heights(map[y][x]))
                    else:
                        elevation = -999
                    if elevation >= -1: # Working back from the goal to the start
                        graph[(x,y)].append((i,j))
                except:
                    pass
    return graph, start, goal

def find_paths(graph, goal):
    q = [(0, goal)]
    path_lengths = {goal: 0}
    while len(q) > 0:
        cost, current = heapq.heappop(q)
        for node in graph[current]:
            if node not in path_lengths or cost + 1 < path_lengths[node]:
                path_lengths[node] = cost + 1
                heapq.heappush(q, (cost + 1, node))
    return path_lengths

def solve(filename):
    map = read_input(filename)
    graph, start, goal = create_graph(map)
    path_lengths = find_paths(graph, goal)
    path_lengths_pt2 = []
    for (x,y), l in path_lengths.items():
        if map[y][x] in "aS":
            path_lengths_pt2 += [l]
    print("Part 1:", path_lengths[start])
    print("Part 2:", min(path_lengths_pt2))

# Run through paths
print(solve(filename))