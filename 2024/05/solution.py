test1 = '''\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
p1_exp = '143'

test2 = test1
p2_exp = '123'

with open("input.txt", "r") as f:
    input = f.read().strip().split("\n")



def valid_middle_page(update, rules):
    pages = [int(p) for p in update.split(",")]
    for i, p in enumerate(pages):
        before = pages[:i]
        if i == len(pages)-1:
            after = []
        else: 
            after = pages[i+1:]
        for b in before:
            if b in rules[p]["before"]:
                return 0
        for a in after:
            if a in rules[p]["after"]:
                return 0    
    return pages[int((len(pages)-1)/2)]

def sort_invalid_update(update, rules):
    pages = [int(p) for p in update.split(",")]
    res = []
    for i, p in enumerate(pages):
        if i==0:
            res.append(p)
        else:
            a=0
            for n, x in enumerate(res):
                if x in rules[p]["before"]:
                    a=max(a,n+1)

            res = res[:a]+[p]+res[a:]
    return res[int((len(res)-1)/2)]

def solve_p1(input):
    ans = 0
    idx = input.index("")
    rules = {}
    for r in input[:idx]:
        a,b = r.split("|")
        if int(a) not in rules.keys():
            rules[int(a)] = {'before': [], 'after': []}
        if int(b) not in rules.keys():
            rules[int(b)] = {'before': [], 'after': []}
        rules[int(a)]["before"].append(int(b))
        rules[int(b)]["after"].append(int(a)) 
    # updates
    for u in input[idx+1:]:
        ans += valid_middle_page(u, rules)

    return ans

def solve_p2(input):
    ans = 0
    idx = input.index("")
    rules = {}
    for r in input[:idx]:
        a,b = r.split("|")
        if int(a) not in rules.keys():
            rules[int(a)] = {'before': [], 'after': []}
        if int(b) not in rules.keys():
            rules[int(b)] = {'before': [], 'after': []}
        rules[int(a)]["before"].append(int(b))
        rules[int(b)]["after"].append(int(a)) 
    # updates
    for u in input[idx+1:]:
        if valid_middle_page(u, rules) == 0:
            ans += sort_invalid_update(u, rules)

    return ans

p1_test = solve_p1(test1.strip().split("\n"))
p1_ans = solve_p1(input)
print("Part 1:")
print("\t Test: ", p1_test, " expected: ", p1_exp)
print("\t Full: ", p1_ans)

p2_test = solve_p2(test2.strip().split("\n"))
p2_ans = solve_p2(input)
print("Part 2:")
print("\t Test: ", p2_test, " expected: ", p2_exp)
print("\t Full: ", p2_ans)