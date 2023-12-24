import itertools
import numpy as np
from shapely.geometry import Point, Polygon, LineString
import matplotlib.pyplot as plt
import copy
import heapq

test1 = '''\
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''.split("\n")

exp_t1 = "62"

test2 = test1#''''''.split("\n")

exp_t2 = ""

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]  


dirs = {
    'D': (-1, 0),
    'U': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}
int2dir = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U',
}

def part_1(input): 
    cur_x, cur_y = 1000, 1000
    points = []
    trenches = []
    fig, axes = plt.subplots(1,2)
    for dig in input: 
        dir, length, col = dig.split()
        col = col[1:-1] 
        new_y = cur_y + dirs[dir][0] * int(length)
        new_x = cur_x + dirs[dir][1] * int(length) 
        t = LineString([[cur_x, cur_y],[new_x, new_y]])
        trenches.append(t)
        axes[0].plot(*t.xy, color=col)
        cur_x, cur_y = new_x, new_y
        points.append(Point(cur_x, cur_y))

    lake = Polygon(points)
    x,y = lake.exterior.xy
    axes[1].plot(x,y)
    return lake.area + lake.boundary.length/2 + 1

def part_2(input):
    cur_x, cur_y = 1000, 1000
    points = []
    fig, ax = plt.subplots(1,1)
    for dig in input: 
        _, _, col = dig.split()
        hexlen = col[2:-2]
        dir = int2dir[col[-2]] 
        length = int(hexlen, 16)
        new_y = cur_y + dirs[dir][0] * int(length)
        new_x = cur_x + dirs[dir][1] * int(length) 
        cur_x, cur_y = new_x, new_y
        points.append(Point(cur_x, cur_y))

    lake = Polygon(points)
    x,y = lake.exterior.xy
    ax.plot(x,y)
    return lake.area + lake.boundary.length/2 + 1



store = {}
print("Part 1:")
test_res1 = part_1(test1)
print("\t Test: ", test_res1, " expected ", exp_t1)
res1 = part_1(input)
print("\t Full: ", res1)

print("Part 2:")
test_res2 = part_2(test2)
print("\t Test: ", test_res2, " expected ", exp_t2)
res2 = part_2(input)
print("\t Full: ", res2)