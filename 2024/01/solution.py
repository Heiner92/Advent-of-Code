test1 = '''\
3   4
4   3
2   5
1   3
3   9
3   3'''
p1_exp = '11'

test2=test1
p2_exp = '31'

with open("input.txt", "r") as f:
    input = f.readlines()

def solve_p1(input):
    l1 = []
    l2 = []
    for line in input:
        l, r = line.strip().split("   ")
        l1.append(l)
        l2.append(r)
    l1 = sorted(l1)
    l2 = sorted(l2)
    diff = 0
    for i in range(len(l1)):
        diff += abs(int(l1[i]) - int(l2[i]))
    return diff

def solve_p2(input):
    l1 = []
    l2 = []
    for line in input:
        l, r = line.strip().split("   ")
        l1.append(int(l))
        l2.append(int(r))
    ans = 0
    for n in l1:
        c = l2.count(n)
        ans+=c*n
    return ans

p1_test = solve_p1(test1.split("\n"))
p1_ans = solve_p1(input)
print("Part 1:")
print("\t Test: ", p1_test, " expected: ", p1_exp)
print("\t Full: ", p1_ans)

p2_test = solve_p2(test2.split("\n"))
p2_ans = solve_p2(input)
print("Part 2:")
print("\t Test: ", p2_test, " expected: ", p2_exp)
print("\t Full: ", p2_ans)