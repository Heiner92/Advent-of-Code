import numpy as np
test1 = '''Time:      7  15   30
Distance:  9  40  200'''.split("\n")

exp_t1 = "288"

test2 = test1#''''''.split("\n")

exp_t2 = "71503"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]

def part_1(input): 
    winnings=1
    times = input[0].split(":")[-1].strip().split()
    dists = input[1].split(":")[-1].strip().split()
    num_games = len(times)
    for g in range(num_games):
        time = int(times[g])
        maxdist = int(dists[g])
        def dist_func(t):
            return t*(time-t)
        pos = list(range(time+1))
        res = list(map(dist_func, pos)) 
        r=np.array(res)
        thiswins = r[r > maxdist]
        winnings *= thiswins.shape[0] 
    return winnings

def part_2(input):
    time = int("".join(input[0].split(":")[-1].strip().split()))
    maxdist = int("".join(input[1].split(":")[-1].strip().split()))
    def dist_func(t):
        return t*(time-t)
    pos = list(range(time+1))
    for i, p in enumerate(pos):
        res = dist_func(p)
        if res > maxdist:
            break
    winnings = time+1-2*i 
    return winnings


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