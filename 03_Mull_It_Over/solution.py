# correct format is mul(x, y)
import re

def get_input():
    with open('input.txt', 'r') as file:
        input = file.read()
    return input

data = get_input()

def find_uncorrupted_muls(data):
    accepted_mul = []
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    print(matches)
    accepted_mul.extend(matches)
    return accepted_mul

print(find_uncorrupted_muls(data))
    