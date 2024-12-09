def get_input():
    with open('input.txt', 'r') as file:
        input = file.read().split()
        return input
    
def make_word_search(input):
    word_search = []
    for line in input:
        word_search += list(line)
    print(word_search)
    

input = get_input()
make_word_search(input)