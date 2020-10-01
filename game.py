import functions

"""
recup word
dictionnaire letter - bol
    if true -> show_lettre
    else show *
input user letter
    check if letter and not try
"""

word = functions.word_random("words.txt")
word_dic = {}
word_mask = []

for i in range(len(word)):
    letter = word[i]
    word_dic[i] = letter
    word_mask.append(False)

print(word)
print(word_dic)
print(word_mask)

input_j = input("enter letter : ")
input_result = functions.show_word(word_dic, word_mask, input_j)

test = ""
for j in range(len(input_result)):
    if input_result[j] is True:
        test += word_dic[j]
    else:
        test += "*"

print(test)