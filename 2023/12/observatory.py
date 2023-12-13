import itertools
test1 = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split("\n")

exp_t1 = "21"

test2 = test1#''''''.split("\n")

exp_t2 = "525152"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]
     
def isvalid(line,groups):
    cur = 0
    seen = []
    for c in line:
        if c == "#":
            cur += 1
        if c == "." and cur > 0:
            seen.append(cur)
            cur = 0
    if cur > 0:
        seen.append(cur)
    if seen==groups:
        return 1 
    else:
        return 0


def collapse(line, i ,groups, curg, cur):
    k = (i, curg, cur)
    if k in store.keys():
        return store[k]
    if i == len(line):
        if curg == len(groups) and cur==0:
            return 1
        elif curg == len(groups)-1 and groups[curg]==cur:
            return 1
        else:
            return 0
    ans = 0
    for c in ["#","."]:
        if line[i] == c or line[i] == "?":
            if c=="." and cur==0:
                ans += collapse(line, i+1, groups, curg, 0)
            elif c=="#":
                ans += collapse(line, i+1, groups, curg, cur+1)
            elif c=="." and cur > 0 and curg<len(groups) and groups[curg]==cur:
                ans += collapse(line,i+1,groups,curg+1,0)
    store[k]=ans
    return ans
            
   

def part_1(input): 
    total = 0
    for line in input:
        store.clear()
        s, groups = line.split()
        groups = [int(g) for g in groups.split(",")]
        options = collapse(s,0,groups,0,0)
        print(line,":   ",options)
        total += options
    return total

def part_2(input):
    total = 0
    for line in input:
        store.clear()
        s, groups = line.split()
        s = "?".join([s]*5)
        groups = ",".join([groups]*5)
        groups = [int(g) for g in groups.split(",")]        
        options = collapse(s,0,groups,0,0)
        print(line,":   ",options)
        total += options
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