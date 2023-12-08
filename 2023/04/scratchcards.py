import copy 
test1 = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split("\n")

exp_t1 = "13"

test2 = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split("\n")

exp_t2 = "30"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]

 
def part_1(input):    
    res=0
    for card in input:
        wins = 0
        s = card.split(":")
        card_num = int(s[0].strip().split(" ")[-1])
        s2 = s[1].strip().split("|")
        winning_nums = s2[0].strip().split() 
        nums = s2[1].strip().split()
        for num in nums:
            if num in winning_nums:
                wins+=1
        if wins > 0:
            res += 2**(max(0,wins-1))       
    return res

def part_2(input):
    res=0
    cards = [[0, 0] for n in range(len(input))]
    for i, card in enumerate(input):
        wins = 0
        s = card.split(":")
        card_num = int(s[0].strip().split(" ")[-1])
        s2 = s[1].strip().split("|")
        winning_nums = s2[0].strip().split() 
        nums = s2[1].strip().split()
        for num in nums:
            if num in winning_nums:
                wins+=1
        cardval = 0
        if wins > 0:
            cardval = 2**(max(0,wins-1))    

        cards[i][0] = cardval,
        cards[i][1] += 1 #int(bool(wins))
        for w in range(wins):
            cards[i+1+w][1]+=cards[i][1]

    for c in cards:
        res+=c[1]   
    return res
    

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