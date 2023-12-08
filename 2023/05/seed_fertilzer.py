test1 = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''.split("\n")

exp_t1 = "35"

test2 = test1#''''''.split("\n")

exp_t2 = "46"

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]


def make_mappings(input):
    mappings = {}
    for line in input:
        if line=="":
            continue
        elif line.endswith("map:"):
            s = line.split("-")
            source = s[0].strip()
            if source not in mappings.keys():
                mappings[source]={}
            dest = s[2].strip().split(" ")[0]
            mappings[source][dest] = []
        else:
            t = [int(x) for x in line.split()]
            mappings[source][dest].append(t)
    return mappings

def fill_mappings(mappings):
    newmappings={}
    for key1, map in mappings.items():
        newmappings[key1]={}
        for key2, vals in map.items():
            vals.sort(key=lambda x: x[1])
            newmappings[key1][key2]=[]
            if vals[0][1]>0:
                newmappings[key1][key2].append([0,0,vals[0][1]])
            for i in range(len(vals)-1):
                dest=vals[i][0]
                src=vals[i][1]
                l=vals[i][2]
                newmappings[key1][key2].append(vals[i])
                if src+l < vals[i+1][1]:
                    newmappings[key1][key2].append([src+l,src+l,vals[i+1][1]-src-l])
            newmappings[key1][key2].append(vals[i+1])
            newmappings[key1][key2].append([vals[i+1][1]+1,vals[i+1][1]+1,int(1e10)])  
    return newmappings

def find_num(number, maps):
    'dest, src, range'
    num = number
    for m in maps:
        dest_start = m[0]
        src_start = m[1]
        rng = m[2]
        if number >= src_start and number <= src_start+rng-1:
            diff = number - src_start
            num = dest_start + diff
    return num
 
def find_nums_as_ranges(number_ranges,maps):
    num_ranges=list()
    for r in number_ranges:
        r_start = int(r[0])
        r_len = int(r[1])
        for m in maps:
            dest_start = m[0]
            src_start = m[1]
            rng = m[2]
            src_end = src_start + rng 
            if r_start >= src_start and r_start <= src_end-1:
                diff = r_start - src_start
                num = dest_start + diff
                num_len = src_end - r_start
                if num_len < r_len:
                    num_ranges.append([num, num_len])
                    num_ranges+=find_nums_as_ranges([[r_start+num_len,r_len-num_len]],maps)
                else:
                    num_ranges.append([num, r_len])
                break

    return num_ranges

def walk_map(mappings, targetkind, thiskind, number):
    if thiskind == targetkind:
        return number
    for nextkind, maps in mappings[thiskind].items():
        number = find_num(number,maps)    
        return walk_map(mappings, targetkind, nextkind, number)


def walk_map_ranged(mappings, targetkind, thiskind, number_ranges):
    if thiskind == targetkind:
        return number_ranges
    for nextkind, maps in mappings[thiskind].items():
        n_count=sum([x[1] for x in number_ranges])
        print()
        print(f"{thiskind:15} ({n_count}): ", number_ranges)
        number_ranges = find_nums_as_ranges(number_ranges,maps)
        new_ = []
        for elem in number_ranges:
            if elem not in new_:
                new_.append(elem)
        number_ranges = new_
        n_count=sum([x[1] for x in number_ranges])
        print(f"{nextkind:15} ({n_count}): ", number_ranges)
        return walk_map_ranged(mappings, targetkind, nextkind, number_ranges)


def part_1(input): 
    seeds = input[0].split(": ")[-1].split()
    mappings = make_mappings(input[1:]) 
    locations=[]
    for s in seeds:  
        locations.append(walk_map(mappings, "location", "seed", int(s)))
    res=min(locations)
       
    return res

def part_2(input):
    seeds = input[0].split(": ")[-1].split()
    seed_ranges = [[int(seeds[i]),int(seeds[i+1])] for i in range(0,len(seeds),2)]
    seed_ranges.sort(key=lambda x: x[0])
    mappings_ = make_mappings(input[1:]) 
    mappings = fill_mappings(mappings_)
    thiskind = "seed"
    locations=walk_map_ranged(mappings, "location", thiskind, seed_ranges)
    res=min([x[0] for x in locations])
       
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