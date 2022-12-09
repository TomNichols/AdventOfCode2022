filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day9\input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def move_head(pos, dir):
    if dir == "R":
        new_pos = [pos[0] + 1, pos[1]]
    elif dir == "L":
        new_pos = [pos[0] - 1, pos[1]]
    elif dir == "U":
        new_pos = [pos[0], pos[1] + 1]
    else:  
        new_pos = [pos[0], pos[1] - 1]
    return new_pos 

def string_vector(head_pos, tail_pos):
    return [a - b for a, b in zip(head_pos, tail_pos)]

def sign(x):
    return x/abs(x) if x != 0 else x

def move_tail(head_pos, tail_pos):

    vector = string_vector(head_pos, tail_pos)

    # If head and tail are touching
    if vector[0]**2 + vector[1]**2 <= 2:
        return tail_pos

    # If head and tails are apart
    else:
        return [int(tail_pos[0] + sign(vector[0])), int(tail_pos[1] + sign(vector[1]))]

def move_string(lines):
    head_pos, tail_pos = [0,0] , [0,0]
    tail_pos_list = []
    for line in lines:
        dir = line.split(" ")[0]
        steps = int(line.split(" ")[1])
        for i in range(steps):
            head_pos = move_head(head_pos, dir)
            tail_pos = move_tail(head_pos, tail_pos)
            tail_pos_list += [tail_pos]
    return len(set([tuple(i) for i in tail_pos_list]))

def move_rope(lines):
    rope_length = 10
    pos = [[0,0] for i in range(rope_length)] 
    tail_pos_list = []
    for line in lines:
        dir = line.split(" ")[0]
        steps = int(line.split(" ")[1])
        for i in range(steps):
            for j in range(rope_length):
                if j == 0:
                    pos[j] = move_head(pos[j], dir)
                else:
                    pos[j] = move_tail(pos[j-1], pos[j])
            tail_pos_list += [pos[9]]
    return len(set([tuple(i) for i in tail_pos_list]))

print(move_string(read_input(filename)))
print(move_rope(read_input(filename)))