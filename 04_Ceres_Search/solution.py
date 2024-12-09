def get_input():
    with open('input.txt', 'r') as file:
        input = file.read().split('\n')
        return input
    
def make_word_search(input):
    word_search = []
    for line in input:
        word_search.append(list(line))
    return word_search
    
def display_word_search(word_search):
    for line in word_search:
        print(" ".join(line))
    
input = get_input()
word_search = make_word_search(input)
display_word_search(word_search)

