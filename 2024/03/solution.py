import re

test1 = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
p1_exp = '161'

test2 = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
p2_exp = '48'

with open("input.txt", "r") as f:
    input = f.read()

def mul(a,b):
    return a*b

def solve_p1(input):
    ans = 0
    for m in re.findall(r"(mul\(\d+,\d+\))", input):
        ans+=eval(m)
    return ans

def solve_p2(input):
    ans = 0
    input="do()"+input+"don't()"
    regex_valid = r"do\(\)(?:(.*?))don't\(\)"
    #regex_mul = r"do\(\).*(mul\(\d+,\d+\)).*don't\(\)"
    
    for valid in re.findall(regex_valid, input):
        ans += solve_p1(valid)
    # s = input.split("do()")
    # ans = solve_p1(s[0])
    # ss = s.split("don't()")
    # ans += solve_p1(s[0])

    return ans

p1_test = solve_p1(test1)
p1_ans = solve_p1(input)
print("Part 1:")
print("\t Test: ", p1_test, " expected: ", p1_exp)
print("\t Full: ", p1_ans)

p2_test = solve_p2(test2)
p2_ans = solve_p2(input)
print("Part 2:")
print("\t Test: ", p2_test, " expected: ", p2_exp)
print("\t Full: ", p2_ans)