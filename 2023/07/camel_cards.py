import numpy as np
test1 = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''.split("\n")

powers = {
    "5ling": 120e11,
    "4ling": 100e11,
    "fullhouse": 80e11,
    "3ling": 60e11,
    "2pairs": 40e11,
    "pair": 20e11,
    "card": 0
}

exp_t1 = "6440"

test2 = test1#''''''.split("\n")

exp_t2 = "5905"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]

def power_of_hand(hand):
    cards = {
        "A":"13", 
        "K":"12", 
        "Q":"11", 
        "J":"10", 
        "T":"09", 
        "9":"08", 
        "8":"07", 
        "7":"06", 
        "6":"05", 
        "5":"04", 
        "4":"03", 
        "3":"02", 
        "2":"01"
    }
    power=""
    occ = {k:0 for k in cards.keys()}
    for i, c in enumerate(hand[::-1]):
        power = f"{cards[c]}{power}"
        occ[c]+=1
    power = int(power)
    nums = sorted(list(occ.values()),reverse=True)
    if nums[0] == 5:
        power += powers["5ling"]
    elif nums[0] == 4:
        power += powers["4ling"]
    elif nums[0] == 3:
        if nums[1] == 2:
            power += powers["fullhouse"]
        else:
            power += powers["3ling"]
    elif nums[0] == 2:
        if nums[1] == 2:
            power += powers["2pairs"]
        else:
            power += powers["pair"]
    return power

def power_of_hand_2(hand):
    cards = {
        "A":"13", 
        "K":"12", 
        "Q":"11", 
        "J":"00", 
        "T":"09", 
        "9":"08", 
        "8":"07", 
        "7":"06", 
        "6":"05", 
        "5":"04", 
        "4":"03", 
        "3":"02", 
        "2":"01"
    }
    power=""
    occ = {k:0 for k in cards.keys()}
    for i, c in enumerate(hand[::-1]):
        power = f"{cards[c]}{power}"
        occ[c]+=1
    power = int(power)
    jokers = occ.pop("J")
    nums = sorted(list(occ.values()),reverse=True)
    nums[0]+=jokers
    if nums[0] == 5:
        power += powers["5ling"]
    elif nums[0] == 4:
        power += powers["4ling"]
    elif nums[0] == 3:
        if nums[1] == 2:
            power += powers["fullhouse"]
        else:
            power += powers["3ling"]
    elif nums[0] == 2:
        if nums[1] == 2:
            power += powers["2pairs"]
        else:
            power += powers["pair"]

    return power


def part_1(input): 
    total = 0
    h  = []
    for game in input:
        hand, bid = game.strip().split()
        power = power_of_hand(hand)
        h.append([power, int(bid), hand])
    sortgames = sorted(h,key=lambda x: x[0])
    for g, game in enumerate(sortgames,1):
        #print(g,": ",game[1], "\t", game[2], "\t", game[0])
        total += g*game[1]
    return total

def part_2(input):
    total = 0
    h  = []
    for game in input:
        hand, bid = game.strip().split()
        power = power_of_hand_2(hand)
        h.append([power, int(bid), hand])
    sortgames = sorted(h,key=lambda x: x[0])
    for g, game in enumerate(sortgames,1):
        #print(g,": ",game[1], "\t", game[2], "\t", game[0])
        total += g*game[1]
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