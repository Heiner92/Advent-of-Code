test1 = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''


test2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

cases_p1 = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
}
cases_p2 = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
}

def first_digit(s, cases):
    for i in range(len(s)):
        for k in cases.keys():
            if s[i::].startswith(k):
                return cases[k]

def last_digit(s, cases):
    for i in range(len(s)):
        if i==0:
            ss = s[:]
        else:
            ss = s[:-i]
        for k in cases.keys():
            if ss.endswith(k):
                return cases[k]

def calc_calibration(input, cases):
    sum=0
    for line in input:
        d1 = first_digit(line,cases)
        d2 = last_digit(line,cases)    
        #print(line, ": ", d1, ", ", d2)
        sum+=int(f"{d1}{d2}")

    return sum


with open("input.txt", "r") as f:
    input = f.readlines()


testsum1 = calc_calibration(test1.split("\n"), cases_p1)
sum1 = calc_calibration(input, cases_p1)
print("Part 1:")
print("\t Test: ", testsum1)
print("\t Full: ", sum1)

testsum2 = calc_calibration(test2.split("\n"), cases_p2)
sum2 = calc_calibration(input, cases_p2)
print("Part 2:")
print("\t Test: ", testsum2)
print("\t Full: ", sum2)