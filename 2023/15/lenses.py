import itertools
import numpy as np
import copy

test1 = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''.split(",")

exp_t1 = "1320"

test2 = test1#''''''.split("\n")

exp_t2 = "145"

with open("input.txt", "r") as f:
    input = [l.split(",") for l in f.readlines()][0]  

def HASH(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    return val

def HASHMAP(boxes, instruction):
    if instruction[-1].isnumeric():
        label = instruction[:-2]
        mode = instruction[-2]
    else:
        label = instruction[:-1]
        mode = instruction[-1]
    box = HASH(label)
    if mode == "-":
        newboxlenses = []
        for lens in boxes[box]:
            if lens[0] != label:
                newboxlenses.append(lens)
        boxes[box] = newboxlenses
    elif mode == "=":
        strength = int(instruction[-1])
        newboxlenses = []
        insertlens = (label, strength)
        inserted=False
        for lens in boxes[box]:
            if lens[0] != label:
                newboxlenses.append(lens)
            else:
                newboxlenses.append(insertlens)
                inserted=True
        if not inserted:
            newboxlenses.append(insertlens)
        boxes[box] = newboxlenses
    
    return boxes

def focusing_power(boxes):
    power = 0
    for b, box in enumerate(boxes):
        for l, lens in enumerate(box):
            lenspower = (1+b)*(1+l)*lens[1]
            power += lenspower
    return power

def part_1(input): 
    total = 0
    for instruction in input:
        total += HASH(instruction)        
    return total

def part_2(input):
    boxes = [[]]*256
    for instruction in input:
        boxes = HASHMAP(boxes, instruction)
    total = focusing_power(boxes)
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