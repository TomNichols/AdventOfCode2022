import os

filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day7\input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def is_command(line):
    return line.split(" ")[0] == "$"

def is_dir(line):
    return line.split(" ")[0] == "dir" 

def file_size(line):
    return int(line.split(" ")[0])

def create_directory_map(lines):
    directory_map = {}
    current_path = "\\"
    last_type = ""
    contents = []
    lines = ["dir \\"] + lines
    for line in lines:
        properties = {}
        if is_command(line):
            line_type = "command"
            if last_type == "file" or last_type == "dir":
                directory_map[current_path]["content"] = contents
            if line.split(" ")[1] == "cd":
                if line.split(" ")[2] == "..":
                    current_path = os.path.split(current_path)[0]
                else:
                    if line.split(" ")[2] != "/":
                        current_path = os.path.join(current_path, line.split(" ")[2])
                    contents = []
        else:
            if is_dir(line):
                line_type = "dir"
                properties["type"] = "dir"
                properties["size"] = 0
                contents += [os.path.join(current_path, line.split(" ")[1])]
                properties["content"] = []
            else:
                line_type = "file"
                properties["type"] = "file"
                properties["size"] = file_size(line)
                properties["content"] = None
                contents += [os.path.join(current_path, line.split(" ")[1])]

            directory_map[os.path.join(current_path, line.split(" ")[1])] = properties
        last_type = line_type

    return directory_map

def recursive_size(node, dir_map, size):
    total_size = 0
    for child in dir_map[node]["content"]:
        # If node contains a dir, need to get the size of that dir and so on
        if dir_map[child]["type"] == "dir":
            total_size += recursive_size(child, dir_map, size)
        else:
            total_size += dir_map[child]["size"]
    return total_size

def get_dir_sizes(lines):
    dir_map = create_directory_map(lines)
    for node in dir_map:
        size = 0
        if dir_map[node]["type"] == "dir":
            dir_map[node]["size"] = recursive_size(node, dir_map, size)
    return dir_map

def get_size_of_main_folder(lines):
    total_size = 0
    for line in lines:
        try:
            total_size += int(line.split(" ")[0])
        except:
            pass
    return total_size 

def sum_dirs_less_than_100k(dir_map):
    return sum([dir_map[key]["size"]for key in dir_map if dir_map[key]["size"] < 1e5 and dir_map[key]["type"] == "dir"])

# The below doesn't work as root dir size is wrong, don't know why or how part 1 worked (and child dirs seem to be correct)
def size_of_deleted_folder(dir_map, space_required, total_space):
    return min([dir_map[key]["size"] for key in dir_map if dir_map[key]["size"] > space_required - total_space + dir_map["\\"]["size"]])

# As a workaround just feed in the calculated root dir size
def size_of_deleted_folder_hack(dir_map, space_required, total_space, root_dir_size):
    return min([dir_map[key]["size"] for key in dir_map if dir_map[key]["size"] > space_required - total_space + root_dir_size])

dir_size_map = get_dir_sizes(read_input(filename))
print(sum_dirs_less_than_100k(dir_size_map))
print(size_of_deleted_folder(dir_size_map, 3e7, 7e7))
print(size_of_deleted_folder_hack(dir_size_map, 3e7, 7e7, get_size_of_main_folder(read_input(filename))))