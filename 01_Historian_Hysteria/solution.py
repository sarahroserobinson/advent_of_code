def get_input():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()

    list1 = []
    list2 = []
    for line in input:
        left, right = map(int, line.split())  
        list1.append(left)
        list2.append(right)
    lists = list1, list2
    return lists
   

def get_list_difference(lists):
    list1 = sorted(lists[0])
    list2 = sorted(lists[1])
    distanceTotal = 0
    
    for num1, num2 in zip(list1, list2):
        if num1 > num2:
          distanceTotal += num1 - num2
        elif num2 > num1:
          distanceTotal += num2 - num1

    return distanceTotal

input = get_input()
list_difference = get_list_difference(input)

print(f"The difference between the lists is {list_difference}")


