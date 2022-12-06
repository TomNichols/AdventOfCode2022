filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day6\input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def is_marker(char_list, num_char):
    return len(set(char_list)) == num_char

def get_character_number(line, num_char):
    last_four_chars = []
    idx = 0
    for char in line:
        if len(last_four_chars) == num_char:
            if is_marker(last_four_chars, num_char):
                return idx
            else:
                last_four_chars.pop(0)
                last_four_chars.append(char)
        else:
            last_four_chars.append(char)
        idx += 1

print(get_character_number(read_input(filename)[0], 4))
print(get_character_number(read_input(filename)[0], 14))