import itertools
import numpy as np
import copy
import heapq

test1 = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''.split("\n")

exp_t1 = "102"

test2 = test1#''''''.split("\n")

exp_t2 = "94"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]  


dirs = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}
dir_opts = {
    dirs['UP']: [dirs['UP'],dirs['LEFT'],dirs['RIGHT']],
    dirs['DOWN']: [dirs['DOWN'],dirs['LEFT'],dirs['RIGHT']],
    dirs['LEFT']: [dirs['UP'],dirs['DOWN'],dirs['LEFT']],
    dirs['RIGHT']: [dirs['UP'],dirs['DOWN'],dirs['RIGHT']],
    (0,0): [dirs['RIGHT'],dirs['DOWN']],
}   
    

def part_1(input): 
    rows = len(input)
    cols = len(input[0])

    visited = {}
    # cost, row, col, dir, dircount
    Q = [(0, 0, 0, (0,0), 0)]
    while Q:
        cost, r, c, dir, dircount = heapq.heappop(Q)
        k = (r, c, dir, dircount)
        if k in visited.keys():
            continue
        else:
            visited[k] = cost
       
        for d in dir_opts[dir]:
            if dir==d:
                dirc=dircount+1
            else:
                dirc=1
            rr = r + d[0]
            cc = c + d[1]
            if 0<=rr<rows and 0<=cc<cols and dirc<4:
                thiscost = int(input[rr][cc])
                heapq.heappush(Q,(cost+thiscost,rr,cc,d,dirc))

    total = 1e10
    for (r, c, dir, dircount), cost in visited.items():
        if r==rows-1 and c==cols-1:
            total = min(total, cost)
    return total

def part_2(input):
    rows = len(input)
    cols = len(input[0])

    visited = {}
    # cost, row, col, dir, dircount
    Q = [(0, 0, 0, (0,0), 0)]
    while Q:
        cost, r, c, dir, dircount = heapq.heappop(Q)
        k = (r, c, dir, dircount)
        if k in visited.keys():
            continue
        else:
            visited[k] = cost
       
        for d in dir_opts[dir]:
            if dir==d:
                dirc=dircount+1
                if dirc > 10:
                    continue
            else:
                if dircount < 4 and dir != (0,0):
                    continue
                dirc=1
            rr = r + d[0]
            cc = c + d[1]
            if 0<=rr<rows and 0<=cc<cols:
                thiscost = int(input[rr][cc])
                heapq.heappush(Q,(cost+thiscost,rr,cc,d,dirc))

    total = 1e10
    for (r, c, dir, dircount), cost in visited.items():
        if r==rows-1 and c==cols-1:
            total = min(total, cost)
    return total



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