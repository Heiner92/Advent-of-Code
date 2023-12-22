import itertools
import numpy as np
import copy

test1 = '''\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''.split("\n")

exp_t1 = "405"

test2 = test1#''''''.split("\n")

exp_t2 = "400"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]  

def preprocess(input):
    grids = []
    thisgrid = []
    for i, l in enumerate(input):
        if l == "" or i+1==len(input):
            grids.append(thisgrid)
            thisgrid=[]
        else:
            thisgrid.append(l)    
    return grids 

def part_1(input): 
    total = 0
    grids = preprocess(input)
    
    mirrors = []
    for g in grids:
        grid = np.zeros((len(g),len(g[0])))
        for l, line in enumerate(g):
            for c, char in enumerate(line):
                if char == "#":
                    grid[l,c]=1
            
        cols = grid.shape[1]
        col_mirror = 0
        col = 1
        while col < cols:
            if col == cols/2:
                #print(col, "==")
                left = grid[:,:col]
                right = grid[:,col:]    
            elif col < cols/2:
                #print(col, "<")
                left = grid[:,:col]
                right = grid[:,col:col*2]
            else:
                #print(col, ">")
                left = grid[:, col-(cols-col):col]
                right = grid[:,col:]
            
            #print(left, "\n--\n", right[:,::-1])
            #print("")
            assert left.shape==right.shape
            if np.all(left == right[:,::-1]):
                col_mirror = col
                break
            else:
                col += 1
        
        rows = grid.shape[0]
        row_mirror = 0
        row = 1    
        while row < rows:
            if row == rows:
                up = grid[:row,:]
                down = grid[row:,:]    
            elif row < rows/2:
                up = grid[:row,:]
                down = grid[row:row*2,:]
            else:
                up = grid[row-(rows-row):row,:]
                down = grid[row:,:]
            assert up.shape==down.shape
            if np.all(up == down[::-1,:]):
                row_mirror = row * 100
                break
            else:
                row += 1
        #print(row_mirror + col_mirror)
        total += row_mirror + col_mirror
        mirrors.append((int(row_mirror/100),col_mirror))
    return total, mirrors

def part_2(input, mirrors):
    total = 0
    grids = preprocess(input)
    
    
    for n, g in enumerate(grids):
        orggrid = np.zeros((len(g),len(g[0])))
        for l, line in enumerate(g):
            for c, char in enumerate(line):
                if char == "#":
                    orggrid[l,c]=1
            
        
        cols = orggrid.shape[1]
        rows = orggrid.shape[0]
        for fixrow, fixcol in itertools.product(range(rows),range(cols)):
            grid = copy.deepcopy(orggrid)
            if grid[fixrow, fixcol] == 0:
                grid[fixrow, fixcol] = 1
            else:
                grid[fixrow, fixcol] = 0
            col_mirror = 0
            col = 1
            while col < cols:
                if col == cols/2:
                    #print(col, "==")
                    left = grid[:,:col]
                    right = grid[:,col:]    
                elif col < cols/2:
                    #print(col, "<")
                    left = grid[:,:col]
                    right = grid[:,col:col*2]
                else:
                    #print(col, ">")
                    left = grid[:, col-(cols-col):col]
                    right = grid[:,col:]
                
                #print(left, "\n--\n", right[:,::-1])
                #print("")
                assert left.shape==right.shape
                if np.all(left == right[:,::-1]) and col != mirrors[n][1]:
                    col_mirror = col
                    break
                else:
                    col += 1
            
            
            row_mirror = 0
            row = 1    
            while row < rows:
                if row == rows:
                    up = grid[:row,:]
                    down = grid[row:,:]    
                elif row < rows/2:
                    up = grid[:row,:]
                    down = grid[row:row*2,:]
                else:
                    up = grid[row-(rows-row):row,:]
                    down = grid[row:,:]
                assert up.shape==down.shape
                if np.all(up == down[::-1,:]) and row != mirrors[n][0]:
                    row_mirror = row * 100
                    break
                else:
                    row += 1
            mirror_val = row_mirror + col_mirror
            if mirror_val > 0:
                print(mirror_val)
                total += row_mirror + col_mirror
                break
    return total


store = {}
print("Part 1:")
test_res1, mirrors_t1 = part_1(test1)
print("\t Test: ", test_res1, " expected ", exp_t1)
res1, mirrors = part_1(input)
print("\t Full: ", res1)

print("Part 2:")
test_res2 = part_2(test2, mirrors_t1)
print("\t Test: ", test_res2, " expected ", exp_t2)
res2 = part_2(input, mirrors)
print("\t Full: ", res2)