test1 = '''\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''
p1_exp = '3749'

test2 = test1
p2_exp = '11387'

with open("input.txt", "r") as f:
    input = f.read().strip().split("\n")

def isvalid(expected_res,operands,cur_res,operators=["+","*"]):
    if len(operands)==0:
        return expected_res==cur_res
    elif cur_res > expected_res:
        return False
    else:
        answers = []
        for op in operators:
            if op == "||":
                new_res = int(f"{cur_res}{operands[0]}")
            else:
                new_res = eval(str(cur_res)+op+str(operands[0]))
            answers.append(isvalid(expected_res,operands[1:],cur_res=new_res,operators=operators))
        return any(answers)
    
def solve_p1(input):
    ans = 0
    for i, line in enumerate(input):
        #print(i+1, "/", len(input))
        expected_res, rest = line.split(":")
        operands = [int(n) for n in rest.strip().split(" ")]
        if isvalid(int(expected_res),operands,cur_res=0,operators=["+","*"]):
            ans+=int(expected_res)
    return ans

def solve_p2(input):
    ans = 0
    for i, line in enumerate(input):
        #print(i+1, "/", len(input))
        expected_res, rest = line.split(":")
        operands = [int(n) for n in rest.strip().split(" ")]
        if isvalid(int(expected_res),operands,cur_res=0,operators=["+","*","||"]):
            ans+=int(expected_res)
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