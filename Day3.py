import string
filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day3\input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines
    
def get_compartment_contents(rucksack):
    compartment1 = slice(0, len(rucksack)//2)
    compartment2 = slice(len(rucksack)//2, len(rucksack))
    return [rucksack[compartment1], rucksack[compartment2]]

def get_shared_item(strings):
    sets = []
    for string in strings:
        sets += [set(string)]
    first = sets[0]
    others = sets[1:]
    return "".join(set(first).intersection(*others))

def get_item_priority(item):
    alphabet = string.ascii_lowercase
    if item in alphabet:
        return alphabet.index(item) + 1
    else:
        return alphabet.index(item.lower()) + 27
    
def get_total_priority(lines):
    total_priority = 0
    for rucksack in lines:
        compartments = get_compartment_contents(rucksack)
        shared_item = get_shared_item(compartments)
        total_priority += get_item_priority(shared_item)
    return total_priority

def get_elf_groups(lines):
    group_size = 0
    groups = []
    group = []
    for line in lines:
        group += [line]
        group_size += 1
        if group_size == 3:
            groups += [group]
            group = []
            group_size = 0
    return groups

def get_total_priority_badge(lines):
    groups = get_elf_groups(lines)
    total_priority = 0
    for group in groups:
        shared_item = get_shared_item(group)
        total_priority += get_item_priority(shared_item)
    return total_priority

print(get_total_priority(read_input(filename)))
print(get_total_priority_badge(read_input(filename)))