import itertools
import numpy as np
import copy

test1 = '''\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''.split("\n")

exp_t1 = "136"

test2 = test1#''''''.split("\n")

exp_t2 = "64"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]  

grid2stone = {
    0: ".",
    1: "#",
    2: "O",
}
stone2grid = {
    ".": 0,
    "#": 1,
    "O": 2,
}

def part_1(input): 
    total = 0
    rows = len(input)
    cols = len(input[0])
    grid = np.zeros((rows, cols))
    for c in range(cols):
        r = 0
        top = rows
        while r < rows:
            if input[r][c] == "O":
                grid[r,c] = top
                total += top
                top -= 1
            elif input[r][c] == "#":
                top = rows-r-1
            r += 1
         
    #print(grid)
    return total

def cycle(grid, p=False):
    rows = grid.shape[0]
    cols = grid.shape[1]
    
    if p:
        print(grid)
    '''NORTH'''
    newgrid = np.zeros((rows,cols))
    for c in range(cols):
        r = 0
        top = 0
        while r < rows:
            if grid[r,c] == 2:
                newgrid[top,c] = 2
                top += 1
            elif grid[r,c] == 1:
                top = r+1
                newgrid[r,c] = 1
            r += 1
    grid = newgrid
    if p:
        print(grid)

    '''WEST'''
    newgrid = np.zeros((rows,cols))
    for r in range(rows):
        c = 0
        left = 0
        while c < cols:
            if grid[r,c] == 2:
                newgrid[r,left] = 2
                left += 1
            elif grid[r,c] == 1:
                left = c+1
                newgrid[r,c] = 1
            c += 1
    grid = newgrid
    if p:
        print(grid)

    '''SOUTH'''
    newgrid = np.zeros((rows,cols))
    for c in range(cols):
        r = rows-1
        bottom = rows-1
        while r >= 0:
            if grid[r,c] == 2:
                newgrid[bottom,c] = 2
                bottom -= 1
            elif grid[r,c] == 1:
                bottom = r-1
                newgrid[r,c] = 1
            r -= 1
    grid = newgrid
    if p:
        print(grid)

    '''EAST'''
    newgrid = np.zeros((rows,cols))
    for r in range(rows):
        c = cols-1
        right = cols-1
        while c >= 0:
            if grid[r,c] == 2:
                newgrid[r,right] = 2
                right -= 1
            elif grid[r,c] == 1:
                right = c-1
                newgrid[r,c] = 1
            c -= 1
    grid = newgrid
    if p:
        print(grid)

    return grid
    

def part_2(input):
    store = {}
    rows = len(input)
    cols = len(input[0])
    grid = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            grid[r,c] = stone2grid[input[r][c]]
    
    cyc=0
    target = 10**9
    while cyc < target:
        cyc+=1 
        k = grid.tobytes()
        if k in store.keys():
            newgrid, total, t = store[k]      
            print(cyc,total, t)
            cyclen = cyc-t
            cyc += ((target-cyc) // cyclen) * cyclen    
        else:
            newgrid = cycle(copy.deepcopy(grid), p=cyc==0)
            total = 0
            for r in range(rows):
                for c in range(cols):
                    if newgrid[r,c]==2:
                        total += rows-r
            store[k] = [newgrid, total, cyc]
        grid = newgrid
            
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