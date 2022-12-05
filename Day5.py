filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day5\input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def initial_state():
    return {
        1:['D','T','W','F','J','S','H','N'],
        2:['H','R','P','Q','T','N','B','G'],
        3:['L','Q','V'],
        4:['N','B','S','W','R','Q'],
        5:['N','D','F','T','V','M','B'],
        6:['M','D','B','V','H','T','R'],
        7:['D','B','Q','J'],
        8:['D','N','J','V','R','Z','H','Q'],
        9:['B','N','H','M','S']
    }

def num_to_move(line):
    return int(line.split(" ")[1])

def source_pile(line):
    return int(line.split(" ")[3])

def dest_pile(line):
    return int(line.split(" ")[5])

def score(state):
    code = ''
    for key in state:
        code += state[key][-1]
    return code

def rearrangement(lines):
    state = initial_state()
    for line in lines:
        n = num_to_move(line)
        source_id = source_pile(line)
        dest_id = dest_pile(line)
        source_list = state[source_id]
        new_source_list = source_list[0:len(source_list) - n]
        move_list = source_list[-n:][::-1]
        state[dest_id].extend(move_list)
        state[source_id] = new_source_list
    return score(state)

def rearrangement_2(lines):
    state = initial_state()
    for line in lines:
        n = num_to_move(line)
        source_id = source_pile(line)
        dest_id = dest_pile(line)
        source_list = state[source_id]
        new_source_list = source_list[0:len(source_list) - n]
        move_list = source_list[-n:]
        state[dest_id].extend(move_list)
        state[source_id] = new_source_list
    return score(state)

print(rearrangement(read_input(filename)))
print(rearrangement_2(read_input(filename)))