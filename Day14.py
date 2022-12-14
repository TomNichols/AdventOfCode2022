filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day14\input.txt"
test = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day14\test_input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def sign(non_zero_int):
    return int(non_zero_int/abs(non_zero_int))

def get_rock_path_coords(path):
    paths = []
    for line in read_input(path):
        coords = line.split(" -> ")
        pairs = []
        last_pair = []
        for pair in coords:
            x = int(pair.split(",")[0])
            y = int(pair.split(",")[1])
            pairs += [[x,y]]
        paths += [pairs]
    return paths

def create_grid(paths):

    # Get all the points which are rock
    rock_coords = []
    for path in paths:
        i = 0
        line = []
        for coord in path:
            if i != 0:
                diff = [last_coord[0] - coord[0] , last_coord[1] - coord[1]]
                if diff[0] != 0:
                    line += [[coord[0] + dx, coord[1]] for dx in range(0, diff[0]+sign(diff[0]), sign(diff[0]))]
                elif diff[1] != 0:
                    line += [[coord[0], coord[1] + dy] for dy in range(0, diff[1]+sign(diff[1]), sign(diff[1]))]
            last_coord = coord
            i += 1
        rock_coords.extend(line)
    rock_coords = [list(x) for x in set(tuple(x) for x in rock_coords)]

    # Get start and end of grid
    grid_start_x, grid_end_x = min([coord[0] for coord in rock_coords]), max([coord[0] for coord in rock_coords])
    grid_end_y = max([coord[1] for coord in rock_coords])
    grid = [[] for y in range(grid_end_y+1)]

    # Fill in the grid
    for y in range(0, grid_end_y+1):
        for x in range(grid_start_x, grid_end_x+1):
            if [x,y] in rock_coords:
                grid[y].append('#')
            else:
                grid[y].append(" ")
    return grid, [500 - grid_start_x, 0]

def visualise_grid(grid):
    for row in grid:
        print("".join(row))

def visualise_grid_2(grid):
    with open('out.txt', 'w') as f:
        for row in grid:
            f.write("".join(row)+ '\n')

def add_sand(grid, start_pos, depth):
    y = 0
    x = start_pos[0]
    while y < depth:
        if grid[y][x] != " ":
            if [x,y] == start_pos:
                return False
            if grid[y][x-1] == " ":
                x -= 1
            elif grid[y][x+1] == " ":
                x += 1
            else:
                grid[y-1][x] = 'o'
                return True
        y += 1
    return False

def expand_grid(grid, width):
    id = 0
    for row in grid:
        grid[id] = [" " for i in range(width)] + row + [" " for i in range(width)]
        id += 1 
    grid += [[" " for i in range(len(grid[0]))]]
    grid += [["#" for i in range(len(grid[0]))]]
    return grid

#Part 1
rock_paths = get_rock_path_coords(filename)
grid, start_pos = create_grid(rock_paths)
count = 0
while add_sand(grid, start_pos, len(grid)) != False:
    count += 1
visualise_grid(grid)
print(count)

#Part 2
rock_paths = get_rock_path_coords(filename)
grid, start_pos = create_grid(rock_paths)
width = 200
grid = expand_grid(grid, width)
start_pos[0] = start_pos[0] + width
count = 0
while add_sand(grid, start_pos, len(grid)) != False:
    count += 1
visualise_grid_2(grid)
print(count)