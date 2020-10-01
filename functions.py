def word_random():
    words_array = []
    with open("words.txt", "r") as file:
        word = file.readlines()
        words_array.append(word)
    
    print(words_array)


word_random()