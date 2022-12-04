filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day4\input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def get_sections_list(assignment):
    min = int(assignment.split("-")[0])
    max = int(assignment.split("-")[1])+1
    return list(range(min, max))

def is_a_subset(list1, list2):
    check1 = all(item in list1 for item in list2)
    check2 = all(item in list2 for item in list1)
    if check1 == True:
        return True
    elif check2 == True:
        return True
    else:
        return False
    
def has_overlap(list1, list2):
    if True in [item in list1 for item in list2]:
        return True
    else:
        return False

def count_subsets(lines):
    count = 0
    for line in lines:
        sections_list_1 = get_sections_list(line.split(",")[0])
        sections_list_2 = get_sections_list(line.split(",")[1])
        if is_a_subset(sections_list_1, sections_list_2):
            count += 1
    return count
        
def count_overlaps(lines):
    count = 0
    for line in lines:
        sections_list_1 = get_sections_list(line.split(",")[0])
        sections_list_2 = get_sections_list(line.split(",")[1])
        if has_overlap(sections_list_1, sections_list_2):
            count += 1
    return count
        
print(count_subsets(read_input(filename)))
print(count_overlaps(read_input(filename)))