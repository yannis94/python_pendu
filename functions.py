import random

def word_random(filepath):
    words_array = []
    with open(filepath, "r") as file:
        word = file.readlines()
    
    for w in word:
        words_array.append(w.rstrip("\n"))

    nbr = random.randint(0, len(words_array)-1)
    return words_array[nbr]

def show_word(dict, array, input):
    
    for i in dict:
        if input == dict[i]:
            array[i] = True
        else:
            continue
    
    return array
