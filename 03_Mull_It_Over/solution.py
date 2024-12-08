import re

def get_input():
    with open('input.txt', 'r') as file:
        input = file.read()
    return input

data = get_input()

def find_uncorrupted_muls(data):
    accepted_mul = []
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    accepted_mul.extend(matches)
    return accepted_mul

def do_math(uncorrupted_muls):
    count = 0
    for item in uncorrupted_muls:
        nums_as_str = item[4:-1].split(',')
        a = int(nums_as_str[0])
        b = int(nums_as_str[1])
        count += a * b
    return count   

uncorrupted_muls = find_uncorrupted_muls(data)
answer = print(do_math(uncorrupted_muls))

    