import ast
from functools import cmp_to_key

filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day13\input.txt"
test = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day13\test_input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def read_packets(path):
    packets = []
    packet = {}
    for line in read_input(path):
        if line == "":
            pass
        else:
            l = ast.literal_eval(line)
            if len(packet) == 0:
                packet["list1"] = l
            else:
                packet["list2"] = l
                packets += [packet]
                packet = {}
    return packets

def compare(left, right):
    for idx in range(max(len(left), len(right))):

        # Parse elements in list 
        try:
            l = left[idx]
        except:
            return 1
        try:
            r = right[idx]
        except:
            return -1
        
        # Check if elements are mis-matched
        if type(l) == int and type(r) == list:
            l = [l]
        if type(r) == int and type(l) == list:
            r = [r]

        # Compare int elements
        if type(l) == int and type(r) == int:
            if l > r:
                return -1
            if r > l:
                return 1

        # Compare list elements
        if type(l) == list and type(r) == list:
            comp = compare(l, r)
            if comp == 1 or comp == -1: # Make sure we return a result if there is one 
                return comp

def eval_packets(packets):
    eval_packets = []
    for packet in packets:
        eval_packet = packet
        eval_packet["test"] = compare(packet["list1"], packet["list2"])
        eval_packets += [eval_packet]
    return eval_packets

def read_packets_2(path):
    packets = []
    for line in read_input(path):
        if line != "":
            packets += [ast.literal_eval(line)]
    return packets

def sort_packets(packets):
    return sorted(packets, key=cmp_to_key(compare), reverse=True)

def get_key(packets):
    idx = 1
    for packet in packets:
        if packet == [[2]]:
            pos1 = idx
        elif packet == [[6]]:
            pos2 = idx
        idx+=1
    return pos1 * pos2
        
def solve_part1(file_path):
    packets = read_packets(file_path)
    packets = eval_packets(packets)
    idx = 1
    ans = 0
    for packet in packets:
        if packet["test"] == 1:
            ans += idx
        idx += 1
    return ans

def solve_part2(file_path):
    packets = read_packets_2(file_path)
    packets.extend([[[2]],[[6]]])
    sorted_packets = sort_packets(packets)
    decoder_key = get_key(sorted_packets)
    return decoder_key

print(solve_part1(filename))
print(solve_part2(filename))