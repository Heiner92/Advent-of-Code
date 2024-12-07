test1 = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
p1_exp = '18'

test2 = test1
p2_exp = '9'

with open("input.txt", "r") as f:
    input = f.readlines()

dirs = {
    "LR": (1, 0),
    "RL": (-1, 0),
    "TB": (0, 1),
    "BT": (0, -1),
    "TLBR": (1, 1),
    "TRBL": (-1, 1),
    "BLTR": (1, -1),
    "BRTL": (-1, -1)
}
def to_grid(input):
    grid = []
    for line in input:
        grid.append([c for c in line.strip()])
    return grid


def check_all_dirs(grid,nx,ny,xs,ys):
    ans = 0
    for thisdir, delta in dirs.items():
        dx, dy = delta
        res = "X"
        i=0
        x = xs
        y = ys
        while x+dx<nx and y+dy<ny and x+dx>=0 and y+dy>=0 and i<3:
            i+=1
            x+=dx
            y+=dy
            res+=grid[y][x]
        if res == "XMAS":
            ans += 1
            print(thisdir, ys+1, xs+1)
    return ans

def solve_p1(input):
    ans = 0
    grid = to_grid(input)
    ny, nx = len(grid), len(grid[0])
    for y in range(ny):
        for x in range(nx):
            if grid[y][x]=="X":
                ans += check_all_dirs(grid,nx,ny,x,y)
    return ans

def solve_p2(input):
    ans = 0
    grid = to_grid(input)
    ny, nx = len(grid), len(grid[0])
    for y in range(1,ny-1):
        for x in range(1,nx-1):
            if grid[y][x]=="A":
                word1 = grid[y-1][x-1]+"A"+grid[y+1][x+1]
                word2 = grid[y+1][x-1]+"A"+grid[y-1][x+1]
                if word1 in ["MAS","SAM"] and word2 in ["MAS","SAM"]:
                    ans+=1
                 
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