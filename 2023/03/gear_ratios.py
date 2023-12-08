import copy 
test1 = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split("\n")

exp_t1 = "4361"

test2 = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split("\n")

with open("input.txt", "r") as f:
    input = [l.strip() for l in f.readlines()]


def get_symbols(input):
    symbols=[]
    symbol_pos = []
    gear_pos = []
    altered = copy.deepcopy(input)
    for i, line in enumerate(input):
        symbol_pos.append([])
        gear_pos.append([])
        for c, char in enumerate(line):
            if not char.isnumeric() and char != ".":
                if char not in symbols:
                    symbols.append(char)
                if char == ('*'):
                    gear_pos[i].append(c)
                symbol_pos[i].append(c)  
                altered[i] = altered[i].replace(char,".")
    
    return symbol_pos, altered, gear_pos



def is_adjacent(line, start, end, symbols):
    
    #print(start, "  ", end)
    lb , ub = 0, len(symbols)
    'line above'
    if line-1 >= lb:
        #print(symbols[line-1])
        for s_id, s in enumerate(symbols[line-1]):
            if s >= start-1 and s <= end+1:
                return True, (line-1,s_id) 
    'line below'
    if line+1 < ub:
        #print(symbols[line+1])
        for s_id, s in enumerate(symbols[line+1]):
            if s >= start-1 and s <= end+1:
                return True, (line+1,s_id)
    'before or after'
    #print(symbols[line])
    for s_id, s in enumerate(symbols[line]):
        if s >= start-1 and s <= end+1:
            return True, (line,s_id)
        
    return False, (-1,-1)

def get_adjacent_numbers(input, symbols, org_input):
    numbers = []
    all_numbers = []
    for i, line in enumerate(input):
        n=0
        if i > 0: 
            start = i-1
        else: 
            start=0
        if i==len(input):
            end=len(input)
        else:
            end=i+2
        # print("\n\n")
        # print("".join(org_input[start:end]))
        
        for s in line.split('.'):
            if s == '':
                n += 1
            else:
                num = int(s)
                all_numbers.append(num)
                adj, _ = is_adjacent(i, n, len(s)+n-1, symbols)
                if adj: 
                    numbers.append(num)
                #     print("adj: ",num)
                # else:
                #     print("not adj: ",num)
                    
                n+=len(s)+1

    #print(all_numbers)
    #print(sum(all_numbers))
    return numbers

def get_get_ratios(input, symbols, org_input):
    numbers = {}
    for i, line in enumerate(input):
        n=0
        if i > 0: 
            start = i-1
        else: 
            start=0
        if i==len(input):
            end=len(input)
        else:
            end=i+2
        # print("\n\n")
        # print("".join(org_input[start:end]))
        
        for s in line.split('.'):
            if s == '':
                n += 1
            else:
                num = int(s)
                adj, symbol_index = is_adjacent(i, n, len(s)+n-1, symbols)
                #print(num, ": ", adj, " - ", symbol_index)
                if adj: 
                    if symbol_index not in numbers.keys():
                        numbers[symbol_index]=[num] 
                    else:
                        numbers[symbol_index].append(num)
                n+=len(s)+1

    #print(numbers)
    return numbers     
 
def part_1(input):    
    symbols, altered_input, _ = get_symbols(input)
    adj_num = get_adjacent_numbers(altered_input, symbols, input)
    return sum(adj_num)

def part_2(input):
    _ , altered_input, gears = get_symbols(input)
    adj_num = get_get_ratios(altered_input, gears, input)
    sum=0
    for values in adj_num.values():
        if len(values)==2:
            gear_ratio= values[0]*values[1]
        else:
            gear_ratio=0
        #print(gear_ratio)
        sum+=gear_ratio
    return sum
    

test_res1, test_res2, res1, res2 = "", "", "", ""

test_res1 = part_1(test1)
res1 = part_1(input)
test_res2 = part_2(test2)
res2 = part_2(input)

print("Part 1:")
print("\t Test: ", test_res1, " expected ", exp_t1)
print("\t Full: ", res1)

print("Part 2:")
print("\t Test: ", test_res2, " expected 467835")
print("\t Full: ", res2)