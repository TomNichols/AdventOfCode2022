import time
import itertools

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

# Part 1
print(count_points(filename, 2000000))