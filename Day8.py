filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day8\input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def add_visible_trees_row(visible_trees, line, row_idx, direction):
    largest = -1
    if direction == "left":
        col_idx = 0
    else:
        col_idx = len(line)-1
    for char in line:
        if int(char) > largest:
            largest = int(char)
            visible_trees += [[row_idx, col_idx]]
        if direction == "left":
            col_idx += 1
        else:
            col_idx -= 1
    return visible_trees

def add_visible_trees_col(visible_trees, line, col_idx, direction):
    largest = -1
    if direction == "down":
        row_idx = 0
    else:
        row_idx = len(line)-1
    for char in line:
        if int(char) > largest:
            largest = int(char)
            visible_trees += [[row_idx, col_idx]]
        if direction == "down":
            row_idx += 1
        else:
            row_idx -= 1
    return visible_trees

def unique_visible_trees(visible_trees):
    return len(set(tuple(item) for item in visible_trees))

def add_to_vertical_lines(vertical_lines, line):
    idx = 0
    for char in line:
        vertical_lines[idx].extend(char)
        idx += 1
    return vertical_lines

def total_visible_trees(lines):
    visible_trees = []
    row_idx = 0
    vertical_lines = [[] for x in range(len(lines))]
    for line in lines:
        vertical_lists = add_to_vertical_lines(vertical_lines, line)
        # From the left
        visible_trees = add_visible_trees_row(visible_trees, line, row_idx, "left")
        # From the right
        visible_trees = add_visible_trees_row(visible_trees, line[::-1], row_idx, "right")
        row_idx += 1

    col_idx = 0
    for list in vertical_lines:
        # From top
        visible_trees = add_visible_trees_col(visible_trees, list, col_idx, "down")
        # From bottom
        visible_trees = add_visible_trees_col(visible_trees, list[::-1], col_idx, "up")
        col_idx += 1

    return(unique_visible_trees(visible_trees))

def count_trees_visible(line, idx, treehouse):
    if idx == 0:
        before = ""
    else:
        before = line[0:idx]
    if idx == len(line)-1:
        after = ""
    else:
        after = line[idx+1:len(line)]
    count_before = 0
    count_after = 0
    # get visible before
    for tree in before[::-1]:
        count_before += 1
        if int(tree) >= treehouse:
            break
    # get visible after
    for tree in after:
        count_after += 1
        if int(tree) >= treehouse:
            break
    return count_before * count_after

def highest_scenic_score(lines):
    vertical_lines = [[] for x in range(len(lines))]
    scenic_scores = {}
    row_idx = 0
    # Horizontal search 
    for line in lines:
        col_idx = 0
        vertical_lines = add_to_vertical_lines(vertical_lines, line)
        for tree in line:
            scenic_scores[str(row_idx)+"-"+str(col_idx)] = count_trees_visible(line, col_idx, int(tree))
            col_idx += 1
        row_idx += 1

    # Vertical search
    col_idx = 0
    for line in vertical_lines:
        row_idx = 0
        for tree in line:
            scenic_scores[str(row_idx)+"-"+str(col_idx)] *= count_trees_visible(line, row_idx, int(tree))
            row_idx += 1
        col_idx += 1

    return scenic_scores[max(scenic_scores, key=scenic_scores.get)]

print(total_visible_trees(read_input(filename)))
print(highest_scenic_score(read_input(filename)))