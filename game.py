import functions

"""
! ToDo
    - test user's input (if not letter etc... / regex ?)
    - gameplay ++ (try again, score board etc...)
"""
#start round / set variable
life = 3
word = functions.word_random("words.txt")
word_dic = {}
word_mask = []
completed = False

for i in range(len(word)):
    letter = word[i]
    word_dic[i] = letter
    word_mask.append(False)

#try player
while life > 0 and completed is False:
    word_result = ""
    print("life : " + str(life))

    input_j = input("enter letter : ")
    input_test, life = functions.show_word(word_dic, word_mask, input_j, life)

    for j in range(len(input_test)):
        if input_test[j] is True:
            word_result += word_dic[j]
        else:
            word_result += "*"

    print(word_result)
    completed = functions.is_complet(word_mask)

print("End")