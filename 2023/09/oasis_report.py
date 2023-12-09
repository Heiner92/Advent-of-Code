import numpy as np
test1 = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.split("\n")

exp_t1 = "114"

test2 = test1#''''''.split("\n")

exp_t2 = "2"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]

def next_val(vals):
    diff = np.diff(vals)
    if np.all(diff == 0):
        return 0
    else:
        return diff[-1]+next_val(diff)
    
def prev_val(vals):
    diff = np.diff(vals)
    if np.all(diff == 0):
        return 0
    else:
        return diff[0]-prev_val(diff)
     
def part_1(input): 
    total = 0
    for seq in input:
        vals = np.array([int(x) for x in seq.split()])
        nextval = next_val(vals)
        total += vals[-1]+nextval
    return total

def part_2(input):
    total = 0
    for seq in input:
        vals = np.array([int(x) for x in seq.split()])
        prevval = prev_val(vals)
        total += vals[0]-prevval
    return total


test_res1 = part_1(test1)
res1 = part_1(input)
test_res2 = part_2(test2)
res2 = part_2(input)


print("Part 1:")
print("\t Test: ", test_res1, " expected ", exp_t1)
print("\t Full: ", res1)

print("Part 2:")
print("\t Test: ", test_res2, " expected ", exp_t2)
print("\t Full: ", res2)