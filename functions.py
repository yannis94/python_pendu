import random

def word_random(filepath):
    words_array = []
    with open(filepath, "r") as file:
        word = file.readlines()
    
    for w in word:
        words_array.append(w.rstrip("\n"))

    nbr = random.randint(0, len(words_array)-1)
    return words_array[nbr]

def show_word(dict, array, input, point):
    good_choice = False
    for i in dict:
        if input == dict[i]:
            array[i] = True
            good_choice = True
        else:
            continue
    
    if good_choice is False:
        point -= 1
    elif good_choice is True:
        point = point
    
    return array, point

def is_complet(array):
    for bol in array:
        if bol:
            continue
        else:
            return False
    return True