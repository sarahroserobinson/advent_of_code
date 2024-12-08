def get_reports():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
    input_as_nums = []
    for line in input:
        nums = list(map(int, line.split())) 
        input_as_nums.append(nums)
    return input_as_nums

reports = get_reports()

def higher_or_lower(row):
    higher = 0
    lower = 0
    for index, value in enumerate(row[:-1]):
        if row[index] > row[index + 1]:
            higher += 1
        elif row[index] < row[index + 1]:
            lower += 1
    if (len(row) - 1) == higher or (len(row) -1) == lower:
        return True
    else:
        return False

def check_adjacent_level(row):
    for index, value in enumerate(row[:-1]):
        difference = abs(value - row[index + 1])
        if difference < 1 or difference > 3:
            return False
    return True

def check_reports(reports):
    safe_reports = 0
    for row in reports:
        trend = higher_or_lower(row)
        adjacent = check_adjacent_level(row)
        if trend and adjacent:
            safe_reports += 1
    return safe_reports
    
    
    

reports = get_reports()
answer = print(check_reports(reports))

