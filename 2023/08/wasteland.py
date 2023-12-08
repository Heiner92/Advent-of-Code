import math
test1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''.split("\n")

test12 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''.split("\n")

exp_t1 = "2"
exp_t12 = "6"

test2 = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''.split("\n")

exp_t2 = "6"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]


def part_1(input): 
    steps = 0
    instructions= input[0].strip()
    nodes={}
    for n in input[2:]:
        nodes[n.split("=")[0].strip()]=n.split("=")[1].strip()[1:-1].split(", ") 
    
    LR={"L":0,"R":1}
    current = "AAA"
    goal = "ZZZ"
    while current != goal:
        for lr in instructions:
            current = nodes[current][LR[lr]]
            steps += 1
    return steps


def part_2(input):
    steps = 0
    instructions= input[0].strip()
    nodes={}
    currents = []
    for n in input[2:]:
        thisnode = n.split("=")[0].strip()
        nodes[thisnode]=n.split("=")[1].strip()[1:-1].split(", ") 
        if thisnode.endswith("A") and thisnode not in currents:
            currents.append(thisnode)   
    LR={"L":0,"R":1}
    
    '''takes too long!!!'''
    # found=False
    # while not found:
    #     for lr in instructions:
    #         steps += 1
    #         for c in range(len(currents)):
    #             currents[c] = nodes[currents[c]][LR[lr]]
    #         if all([cur.endswith('Z') for cur in currents]):
    #             found=True
    #             break

    allsteps = [0]*len(currents)
    for c in range(len(currents)):
        steps=0
        found=False
        while not found:
            for lr in instructions:
                steps += 1
                currents[c] = nodes[currents[c]][LR[lr]]
                print(steps,"  ",currents[c])
                if currents[c].endswith('Z'):
                    allsteps[c] = steps
                    found=True
                    break
    
    steps = math.lcm(*allsteps)
                        
    return steps

test_res1 = part_1(test1)
test_res12 = part_1(test12)
res1 = part_1(input)
test_res2 = part_2(test2)
res2 = part_2(input)


print("Part 1:")
print("\t Test: ", test_res1, " expected ", exp_t1)
print("\t Test 2: ", test_res12, " expected ", exp_t12)
print("\t Full: ", res1)

print("Part 2:")
print("\t Test: ", test_res2, " expected ", exp_t2)
print("\t Full: ", res2)