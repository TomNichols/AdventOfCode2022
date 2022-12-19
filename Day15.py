from collections import Counter
import heapq

filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day15\input.txt"
test = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day15\test_input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def get_sensor_and_beacon_coords(line):
    x_s = int(line.split("x=")[1].split(",")[0])
    y_s = int(line.split("y=")[1].split(":")[0])
    x_b = int(line.split("x=")[2].split(",")[0])
    y_b = int(line.split("y=")[2])
    return (x_s,y_s), (x_b,y_b)

def manhattan_dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def count_points(path, y):
    boundary = set()
    beacons = set()
    sensors = set()
    for line in read_input(path):
        sensor_loc, beacon_loc = get_sensor_and_beacon_coords(line)
        sensors.add(sensor_loc)
        beacons.add(beacon_loc)
        dist = manhattan_dist(sensor_loc, beacon_loc)
        if abs(sensor_loc[1] - y) <= dist:
            dx = dist - abs(y - sensor_loc[1])
            boundary |= set(range(sensor_loc[0] - dx, sensor_loc[0] + dx + 1))
    return len(boundary) - sum(1 for beacon in beacons if beacon[1] == y)

def get_points_on_line(a,b):
    if b[1] - a[1] > 0 and b[0] - a[0] > 0:
        return [[a[0]+k, a[1]+k] for k in range(0,abs(b[1]-a[1])+1)]
    if b[1] - a[1] < 0 and b[0] - a[0] < 0:  
        return [[a[0]-k, a[1]-k] for k in range(0,abs(b[1]-a[1])+1)] 
    if b[1] - a[1] > 0 and b[0] - a[0] < 0:
        return [[a[0]-k, a[1]+k] for k in range(0,abs(b[1]-a[1])+1)]
    if b[1] - a[1] < 0 and b[0] - a[0] > 0:  
        return [[a[0]+k, a[1]-k] for k in range(0,abs(b[1]-a[1])+1)]
    
def points_outside(sensor_dict):
    line_points_master = []
    for key in sensor_dict:
        line_points = []
        print(key)
        d = sensor_dict[key]
        vertices = [[key[0] + d + 1, key[1]],[key[0] - d - 1, key[1]],[key[0], key[1] + d + 1],[key[0], key[1] - d - 1]]
        vertex_pairs = [
            [vertices[0],vertices[1]],
            [vertices[1],vertices[2]],
            [vertices[2],vertices[3]],
            [vertices[3],vertices[0]],
            [vertices[0],vertices[2]],
            [vertices[3],vertices[1]]
        ]
        for pair in vertex_pairs:
            if pair[0][0] != pair[1][0] and pair[0][1] != pair[1][1]:
                line_points += get_points_on_line(pair[0],pair[1])
        line_points_master += [list(x) for x in set(tuple(x) for x in line_points)]
    return line_points_master

# Part 1
print(count_points(filename, 2000000))

# Part 2
sensor_dict = {}
for line in read_input(filename):
    sensor_loc, beacon_loc = get_sensor_and_beacon_coords(line)
    sensor_dict[sensor_loc] = manhattan_dist(sensor_loc, beacon_loc)
points = points_outside(sensor_dict)
counts = Counter([tuple(x) for x in points])
distress_beacon = max(counts, key=counts.get)
print(distress_beacon)
print(counts[distress_beacon])
print(int(distress_beacon[0]*4e6 + distress_beacon[1]))