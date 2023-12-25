import itertools
import numpy as np
from shapely.geometry import Point, Polygon, LineString
import matplotlib.pyplot as plt
import copy
import heapq
import json

test1 = '''\
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''.split("\n")

exp_t1 = "19114"

test2 = test1#''''''.split("\n")

exp_t2 = "167409079868000"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]  


workflows = {}
valids = []


def check_wf(p, wf):
    global workflows
    if wf == "A":
        return True
    elif wf == "R":
        return False

    x = p["x"]
    m = p["m"]
    a = p["a"]
    s = p["s"]
    for con, nextwf in workflows[wf]:
        if eval(con):
            return check_wf(p,nextwf)
        
    assert False


def find_valid_wfs(wf,cons):
    global workflows
    global valids
    if wf == "A":
        valids.append(copy.deepcopy(cons))
        return
    if wf == "R":
        return
    
    
    for con, nextwf in workflows[wf]:
        if con!="True":
            newcons = copy.deepcopy(cons)

            for s in "xmas":
                if con.startswith(s):
                    op = con[1]
                    num = int(con[2:])
                    if op==">":
                        newcons[s][0] = max(cons[s][0], num+1)
                        cons[s][1] = min(cons[s][1], num)
                    elif op=="<": 
                        newcons[s][1] = min(cons[s][1], num-1)
                        cons[s][0] = max(cons[s][0], num)
            find_valid_wfs(nextwf,newcons)

        else:
            find_valid_wfs(nextwf,cons)
            break

        
        

def part_1(input):
    total = 0
    global workflows
    workflows = {}

    for i, line in enumerate(input):
        if line.strip() == "":
            break
        wfn, steps = line.strip().split("{")
        steps=steps[:-1].split(",")
        workflows[wfn] = []
        for step in steps:
            if ":" in step:
                con, wf = step.split(":")
                workflows[wfn].append((con, wf))
            else:
                workflows[wfn].append(("True", step))
    
    for line in input[i+1:]:
        p={}
        for val in line.strip()[1:-1].split(","):
            k,v = val.split("=")
            p[k]=int(v) 
        accepted = False
        accepted = check_wf(p,"in")
        if accepted:
            total += p["x"]+p["m"]+p["a"]+p["s"]
        
    return total

def part_2(input):
    
    global workflows
    global valids
    workflows = {}
    valids = []
    for i, line in enumerate(input):
        if line.strip() == "":
            break
        wfn, steps = line.strip().split("{")
        steps=steps[:-1].split(",")
        workflows[wfn] = []
        for step in steps:
            if ":" in step:
                con, wf = step.split(":")
                workflows[wfn].append((con, wf))
            else:
                workflows[wfn].append(("True", step))
                

    startcon = {
        "x":[1,4000],
        "m":[1,4000],
        "a":[1,4000],
        "s":[1,4000]
    }
    find_valid_wfs("in",startcon)

    total = 0
    for v in valids:
        pos = 1
        for t, s in enumerate("xmas"):
            pos *= v[s][1]-v[s][0]+1        
        total += pos 
    
    return total

print("Part 1:")
test_res1 = part_1(test1)
print("\t Test: ", test_res1, " expected: ", exp_t1)
res1 = part_1(input)
print("\t Full: ", res1)

print("Part 2:")
test_res2 = part_2(test2)
print("\t Test: ", test_res2, "expected: ", exp_t2)
res2 = part_2(input)
print("\t Full: ", res2)