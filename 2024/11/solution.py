test1 = '''\
'''
p1_exp = ''

test2 = '''\
'''
p2_exp = ''

with open("input.txt", "r") as f:
    input = f.readlines()

def solve_p1(input):
    ans = ""
    return ans

def solve_p2(input):
    ans = ""
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