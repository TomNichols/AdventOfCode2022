filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day1\input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines
    
def get_elf_calories(lines):

    elf_calories_list = []
    elf_calories = 0
    for line in lines:
        if line == "":
            elf_calories_list += [elf_calories]
            elf_calories = 0
        else:
            elf_calories += int(line)
    elf_calories_list += [elf_calories]
    return elf_calories_list

calories_list = get_elf_calories(read_input(filename))
print(max(calories_list))
calories_list.sort()
print(sum(calories_list[-3:]))