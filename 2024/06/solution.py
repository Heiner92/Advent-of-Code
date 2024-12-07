test1 = '''\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''
p1_exp = '41'

test2 = test1
p2_exp = '6'

import copy

with open("input.txt", "r") as f:
    input = f.read()
    input = input.strip().split("\n")

m = {
    '.':0,
    '#':-1,
    '^':1
}

def rotate_90(dx, dy):
    if (dx, dy) == (1, 0):
        return 0, 1
    
    elif (dx, dy) == (0, 1):
        return -1, 0
    
    elif (dx, dy) == (-1, 0):
        return 0, -1
    
    elif (dx, dy) == (0, -1):
        return 1, 0
    
def solve_p1(input):
    grid = []
    for y, line in enumerate(input):
        grid.append([c for c in line])
        for x, c in enumerate(line):
            if c=="^":
                startpos = (x,y) 
                grid[y][x]="X"            

    ny = len(grid)
    nx = len(grid[0])
    dx, dy = 0, -1
    x, y = startpos
    while x+dx < nx and x+dx >= 0 and y+dy < ny and y+dy >= 0:
        if grid[y+dy][x+dx] == "#":
            dx, dy = rotate_90(dx, dy)    
        x += dx
        y += dy
        grid[y][x] = "X"
        
    ans = 0
    for line in grid:
        #print("".join(line))
        for c in line:
            if c == "X":
                ans+=1
    
    return ans, grid

def check_for_loop(grid, startpos, max_steps):
    ny = len(grid)
    nx = len(grid[0])
    dx, dy = 0, -1
    x, y = startpos

    seen = {(x,y):[(dx,dy)]}
    while x+dx < nx and x+dx >= 0 and y+dy < ny and y+dy >= 0:
        if grid[y+dy][x+dx] == "#":
            dx, dy = rotate_90(dx, dy)    
        x += dx
        y += dy
        k = (x,y)        
        v = (dx, dy)
        if k not in seen.keys():
            seen[k]=[]
            
        if v in seen[k]:
            return 1
        else:
            seen[k].append(v)
    return 0

def solve_p2(input):
    ans = 0
    steps, solved_grid = solve_p1(input)
    
    fakerow = ['.']*(len(solved_grid[0])+2)
    expanded = [fakerow]
    for line in solved_grid:
        expanded.append(["."]+line+["."])
    expanded.append(fakerow)

    grid = []
    for y, line in enumerate(input):
        grid.append([c for c in line])
        for x, c in enumerate(line):
            if c=="^":
                startpos = (x,y) 
                grid[y][x]="X"            

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            thisgrid = copy.deepcopy(grid)
            if thisgrid[y][x] == ".":
                if expanded[y+1][x+1] == "X" or \
                   expanded[y+2][x+1] == "X" or \
                   expanded[y][x+1] == "X" or \
                   expanded[y+1][x+2] == "X" or \
                   expanded[y+1][x] == "X":
                    thisgrid[y][x] = "#"
                    ans += check_for_loop(thisgrid, startpos, steps)
    return ans

p1_test, _ = solve_p1(test1.strip().split("\n"))
p1_ans, _ = solve_p1(input)
print("Part 1:")
print("\t Test: ", p1_test, " expected: ", p1_exp)
print("\t Full: ", p1_ans)

p2_test = solve_p2(test2.strip().split("\n"))
p2_ans = solve_p2(input)
print("Part 2:")
print("\t Test: ", p2_test, " expected: ", p2_exp)
print("\t Full: ", p2_ans)