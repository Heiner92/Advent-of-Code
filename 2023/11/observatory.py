import numpy as np
import itertools
test1 = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''.split("\n")

exp_t1 = "374"

test2 = test1#''''''.split("\n")

exp_t2 = "0"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]

def expand(input, expansion=1):
    expanded = []
    row_expansions = []
    col_expansions = []
    for row in input:
        if "#" not in row:
            if expansion == 1:
                expanded.append("*"*len(row))
            else:
                #row_expansions.append(-1)
                row_expansions.append(expansion-1)
        else:
            row_expansions.append(0)
        expanded.append(row)
    
    added = 0
    for i in range(len(input[0])):
        has_galaxy=False
        for r in input:
            if r[i]=="#":
                has_galaxy = True
                break 
        if not has_galaxy:
            if expansion == 1:
                for r in range(len(expanded)):
                    expanded[r] = expanded[r][:i+added]+"*"+expanded[r][i+added:]
                added+=1
            else:
                #col_expansions.append(-1)
                col_expansions.append(expansion-1)
        else:
            col_expansions.append(0)
    #print(row_expansions)
    #print(col_expansions)
    return expanded, row_expansions, col_expansions
     
def part_1(input): 
    
    #print("\n".join(input))
    expanded, _, _ = expand(input)
    #print("\n")
    #print("\n".join(expanded))

    galaxies = []
    for x, row in enumerate(expanded):
        for y, c in enumerate(row):
            if c=="#":
                galaxies.append([x,y,len(galaxies)+1])

    total = 0
    for combo in itertools.combinations(galaxies, 2):
        xdiff = combo[0][0]-combo[1][0]
        ydiff = combo[0][1]-combo[1][1]
        total += abs(xdiff)+abs(ydiff)
    return total

def part_2(input,expansion=1000000):
    #print("\n".join(input))
    expanded, _, _ = expand(input)
    #print("\n".join(expanded))
    expanded, row_expansions, col_expansions = expand(input, expansion)
    #print("\n")

    galaxies = []
    for x, row in enumerate(expanded):
        for y, c in enumerate(row):
            if c=="#":
                galaxies.append([x,y,len(galaxies)+1])

    total = 0
    for combo in itertools.combinations(galaxies, 2):
        x1, x2 = sorted([combo[0][0],combo[1][0]])
        y1, y2 = sorted([combo[0][1],combo[1][1]])
        xdiff = x2-x1
        ydiff = y2-y1
        total += xdiff+ydiff+sum(col_expansions[y1:y2])+sum(row_expansions[x1:x2])
        #print(combo[0][2], "-", combo[1][2],": ", xdiff+ydiff, "\t", sum(row_expansions[x1:x2]),"\t",sum(col_expansions[y1:y2]))
    return total



test_res1 = part_1(test1)
res1 = part_1(input)
test_res2 = part_2(test2,10)
test_res22 = part_2(test2,100)
res2 = part_2(input)


print("Part 1:")
print("\t Test: ", test_res1, " expected ", exp_t1)
print("\t Full: ", res1)

print("Part 2:")
print("\t Test: ", test_res2, " expected ", "1030")
print("\t Test: ", test_res22, " expected ", "8410")
print("\t Full: ", res2)