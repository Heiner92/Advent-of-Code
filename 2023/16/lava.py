import itertools
import numpy as np
import copy

test1 = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''.replace("\\","x").split("\n")

exp_t1 = "46"

test2 = test1#''''''.split("\n")

exp_t2 = "51"

with open("input.txt", "r") as f:
    input = [l.strip().replace("\\","x") for l in f.readlines()]  


dirs = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}


def energized(grid):
    total = 0
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r,c] > 0:
                total += 1
    return total

def follow_grid(input, startpos):
    rows = len(input)
    cols = len(input[0])
    grid = np.zeros((rows,cols))
    
    positions = [startpos]
    seen_pos = []
    while len(positions) > 0:
        newpositions = []
        for pos in positions:
            k = tuple(pos)
            if k in seen_pos:
                continue 
            else:
                seen_pos.append(k)
            grid[pos[0],pos[1]] += 1
            
            tile = input[pos[0]][pos[1]]
            if tile == "/":
                if pos[2] == dirs["UP"]:
                    pos[2] = dirs["RIGHT"]
                elif pos[2] == dirs["RIGHT"]:
                    pos[2] = dirs["UP"]
                elif pos[2] == dirs["LEFT"]:
                    pos[2] = dirs["DOWN"]
                elif pos[2] == dirs["DOWN"]:
                    pos[2] = dirs["LEFT"]
            elif tile == "x": # \
                if pos[2] == dirs["UP"]:
                    pos[2] = dirs["LEFT"]
                elif pos[2] == dirs["RIGHT"]:
                    pos[2] = dirs["DOWN"]
                elif pos[2] == dirs["LEFT"]:
                    pos[2] = dirs["UP"]
                elif pos[2] == dirs["DOWN"]:
                    pos[2] = dirs["RIGHT"]
            elif tile == "|":
                if pos[2] == dirs["RIGHT"] or pos[2] == dirs["LEFT"]:
                    pos[2] = dirs["UP"]
                    
                    rr = pos[0]+dirs["DOWN"][0]
                    cc = pos[1]+dirs["DOWN"][1]
                    if rr < rows and rr >= 0 and cc >= 0 and cc < cols:
                        thisk = tuple([rr,cc,dirs["DOWN"]])
                        if thisk not in seen_pos:
                            newpositions.append([rr,cc,dirs["DOWN"]])
            elif tile == "-":
                if pos[2] == dirs["UP"] or pos[2] == dirs["DOWN"]:
                    pos[2] = dirs["LEFT"]

                    rr = pos[0]+dirs["RIGHT"][0]
                    cc = pos[1]+dirs["RIGHT"][1]
                    if rr < rows and rr >= 0 and cc >= 0 and cc < cols:
                        thisk = tuple([rr,cc,dirs["RIGHT"]])
                        if thisk not in seen_pos:
                            newpositions.append([rr,cc,dirs["RIGHT"]])
            
            pos[0] += pos[2][0]
            pos[1] += pos[2][1]
            if pos[0] < rows and pos[0] >= 0 and pos[1] >= 0 and pos[1] < cols:
                newpositions.append(pos)
                
        positions = newpositions
        
    return energized(grid)


def part_1(input):
    total = follow_grid(input, [0,0,dirs["RIGHT"]])
    return total

def part_2(input):
    rows = len(input)
    cols = len(input[0])

    startpos=[]
    for c in range(cols):
        startpos.append([0,c,dirs["DOWN"]])
        startpos.append([rows-1,c,dirs["UP"]])
    for r in range(rows):
        startpos.append([r,0,dirs["RIGHT"]])
        startpos.append([r,cols-1,dirs["LEFT"]])

    maxe = 0
    for n, pos in enumerate(startpos):
        print(n/len(startpos)*100)
        maxe = max(maxe, follow_grid(input, pos))    
    return maxe


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