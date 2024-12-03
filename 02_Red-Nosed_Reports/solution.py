# Count how many rows are safe. The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

def get_input():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
    input_as_nums = []
    for line in input:
        nums = list(map(int, line.split())) 
        input_as_nums.append(nums)
    return input_as_nums

print(get_input())

