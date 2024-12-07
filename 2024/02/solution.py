test1 = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
p1_exp = '2'

test2 = test1
p2_exp = '4'

with open("input.txt", "r") as f:
    input = f.readlines()

def issave(mi, ma):
    if abs(ma) <= 3 and abs(mi) <= 3:
        if (ma < 0 and mi < 0) or (ma > 0 and mi > 0):
            return 1  
    return 0
    

def solve_p1(input):
    ans = 0
    for report in input:
        levels = report.strip().split(" ")
        diffs = []
        for i in range(len(levels)-1):
            diffs.append(int(levels[i])-int(levels[i+1]))
        ma = max(diffs)
        mi = min(diffs)
        ans += issave(mi,ma)
        
    return ans

def solve_p2(input):
    ans = 0
    for report in input:
        orglevels = report.strip().split(" ")
        nlevels = len(orglevels)
        diffs = []
        for i in range(nlevels-1):
            diffs.append(int(orglevels[i])-int(orglevels[i+1]))
        ma = max(diffs)
        mi = min(diffs)
        if issave(mi,ma):
            ans += 1
        else:
            for k in range(nlevels):
                levels = orglevels[:k]+orglevels[k+1:]
                diffs = []
                for i in range(len(levels)-1):
                    diffs.append(int(levels[i])-int(levels[i+1]))
                ma = max(diffs)
                mi = min(diffs)
                if issave(mi,ma):
                    ans += 1
                    break
        
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