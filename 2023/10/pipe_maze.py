import numpy as np
from shapely.geometry import Point, Polygon

test1 = '''.....
.S-7.
.|.|.
.L-J.
.....'''.split("\n")

test12 = '''-L|F7
7S-7|
L|7||
-L-J|
L|-JF'''.split("\n")

test13 = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...'''.split("\n")

test14 = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''.split("\n")


exp_t1 = "4"
exp_t12 = "4"
exp_t13 = "8"
exp_t14 = "8"

test2 = '''...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........'''.split("\n")

exp_t2 = "4"

test22 = '''.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...'''.split("\n")

exp_t22 = "8"

test23 = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L'''.split("\n")

exp_t23 = "10"

pipes = {
    #    (N,E,S,W)
    "|": (1,0,1,0), 
    "-": (0,1,0,1),
    "L": (1,1,0,0),
    "J": (1,0,0,1),
    "7": (0,0,1,1),
    "F": (0,1,1,0),
    "S": (0,0,0,0)

    # "|": "NS", 
    # "-": "EW",
    # "L": "NE",
    # "J": (1,0,0,1),
    # "7": (0,0,1,1),
    # "F": (0,1,1,0),
    # "S": (0,0,0,0)
}

pos={
    "N": "|7F",
    "E": "-J7",
    "S": "|LJ",
    "W": "-FL"
}
class Pipe:
    def __init__(self, x,y,type):
        self.x = x
        self.y = y
        self.connecting = pipes[type]
        self.prev = None
        self.next = None

    def dir_prev(self):
        cx = self.prev.x - self.x
        if cx == 1:
            return (0,1,0,0)
        elif cx == -1:
            return (0,0,0,1)
        else:
            cy = self.prev.y - self.y
            if cy == 1:
                return (0,0,1,0)
            elif cy == -1:
                return (1,0,0,0)

        print(cx, cy)  
        raise ValueError("unknown previous origin")

    def find_next_pipe(self):
        n,e,s,w = np.subtract(self.connecting, self.dir_prev())
        y = self.y-n+s
        x = self.x+e-w
        return x,y 


with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]

    

    

def part_1(input): 
    startpipe = None   
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "S":
                startpipe = Pipe(x,y,c)
                for dir,x,y in [("W",-1,0),("E",1,0),("S",0,-1),("N",0,1)]:
                    check_x = startpipe.x+x
                    check_y = startpipe.y+y
                    if check_y >= 0 and check_y < len(input):
                        line = input[check_y]
                        if check_x >=0 and check_x < len(line):
                            c = input[check_y][check_x]
                            if c in pos[dir]:
                                newpipe = Pipe(check_x,check_y,c)
                                newpipe.prev=startpipe
                                if startpipe.next == None:
                                    startpipe.next = newpipe
                                elif startpipe.prev==None:
                                    pass
                                    #startpipe.prev = newpipe
                                else:
                                    raise ValueError("Too many Pipes around Start!")        
            if startpipe != None:
                break
        if startpipe != None:
            break
        
    i = 1
    nextpipe = startpipe.next
    while True: 
        i += 1   
        #print(nextpipe.y,nextpipe.x)      
        x,y = nextpipe.find_next_pipe()
        if x == startpipe.x and y==startpipe.y:
            break
        else:
            pipe = Pipe(x,y,input[y][x])
            nextpipe.next = pipe
            pipe.prev = nextpipe
            nextpipe=pipe
        
    
    return int(i/2)

def part_2(input):
    startpipe = None   
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "S":
                startpipe = Pipe(x,y,c)
                for dir,x,y in [("W",-1,0),("E",1,0),("S",0,-1),("N",0,1)]:
                    check_x = startpipe.x+x
                    check_y = startpipe.y+y
                    if check_y >= 0 and check_y < len(input):
                        line = input[check_y]
                        if check_x >=0 and check_x < len(line):
                            c = input[check_y][check_x]
                            if c in pos[dir]:
                                newpipe = Pipe(check_x,check_y,c)
                                newpipe.prev=startpipe
                                if startpipe.next == None:
                                    startpipe.next = newpipe
                                elif startpipe.prev==None:
                                    pass
                                    #startpipe.prev = newpipe
                                else:
                                    raise ValueError("Too many Pipes around Start!")        
            if startpipe != None:
                break
        if startpipe != None:
            break
        
    pipepoints=[[startpipe.x,startpipe.y]]
    nextpipe = startpipe.next
    while True:       
        #print(nextpipe.y,nextpipe.x) 
        pipepoints.append([nextpipe.x,nextpipe.y])
        x,y = nextpipe.find_next_pipe()
        if x == startpipe.x and y==startpipe.y:
            pipepoints.append([x,y])
            break
        else:
            pipe = Pipe(x,y,input[y][x])
            nextpipe.next = pipe
            pipe.prev = nextpipe
            nextpipe=pipe

    from shapely.prepared import prep

    shape = Polygon(pipepoints)
    prep_polygon = prep(shape)

    
    points=[]
    for y in range(len(input)):
        for x in range(len(input[0])):
            p = Point(x,y)
            points.append(p)

    valid_points=[]
    valid_points.extend(filter(prep_polygon.contains, points))

    return len(valid_points)
    
    


print("Part 1:")
test_res1 = part_1(test1)
print("\t Test: ", test_res1, " expected ", exp_t1)
test_res12 = part_1(test12)
print("\t Test 2: ", test_res12, " expected ", exp_t12)
test_res13 = part_1(test13)
print("\t Test 3: ", test_res13, " expected ", exp_t13)
test_res14 = part_1(test14)
print("\t Test 4: ", test_res14, " expected ", exp_t14)

res1 = part_1(input)
print("\t Full: ", res1)


print("Part 2:")
test_res2 = part_2(test2)
print("\t Test: ", test_res2, " expected ", exp_t2)
test_res22 = part_2(test22)
print("\t Test 2: ", test_res22, " expected ", exp_t22)
test_res23 = part_2(test23)
print("\t Test 3: ", test_res23, " expected ", exp_t23)

res2 = part_2(input)
print("\t Full: ", res2)