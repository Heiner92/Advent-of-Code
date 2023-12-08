test1 = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.split("\n")

test2 = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.split("\n")

with open("input.txt", "r") as f:
    input = f.readlines()

config_1 = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def part_1(input, config):
    possible_games = 0
    for game in input:
        possible = True
        hd, tail = game.split(":")
        id = int(hd[5:])
        for set in tail.strip().split(";"):
            for cubes in set.strip().split(","):
                count, color = cubes.strip().split(" ")
                if config[color] < int(count):
                    possible = False
                    break
            if not possible:
                break
        if possible:
            possible_games += id       
    return possible_games                 

def part_2(input):
    
    total_power = 0 
    for game in input:
        min_config = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }       
        hd, tail = game.split(":")
        id = int(hd[5:])
        for set in tail.strip().split(";"):
            set_min_config = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for cubes in set.strip().split(","):
                count, color = cubes.strip().split(" ")
                if set_min_config[color] > int(count) or set_min_config[color]==0:
                    set_min_config[color] = int(count)

            for color in min_config.keys():
                if set_min_config[color] > min_config[color]:
                    min_config[color] = set_min_config[color]
        power = 1
        for val in min_config.values():
            power *= val
        #print(min_config.values(), " --> ", power)
        total_power += power
                       
    return total_power   

test_res1, test_res2, res1, res2 = "", "", "", ""

test_res1 = part_1(test1, config_1)
res1 = part_1(input, config_1)
test_res2 = part_2(test2)
res2 = part_2(input)

print("Part 1:")
print("\t Test: ", test_res1, " expected 8")
print("\t Full: ", res1)

print("Part 2:")
print("\t Test: ", test_res2, " expected 2286")
print("\t Full: ", res2)