# Count how many rows are safe. The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

def get_reports():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
    input_as_nums = []
    for line in input:
        nums = list(map(int, line.split())) 
        input_as_nums.append(nums)
    return input_as_nums

reports = get_reports()

def check_reports(reports):
    safe_reports = 0
    print(reports)
    

check_reports(reports)