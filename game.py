import functions

def round(pseudo):

    def user_input(bol, answer):
        while bol is False:
            print("Invalid, you have to enter only one letter.")
            answer = input("enter letter : ")
            bol = functions.regex(answer)
        
        return answer


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

        round_try = input("enter letter : ")
        test = functions.regex(round_try)
        input_j = user_input(test, round_try)
        input_test, life = functions.show_word(word_dic, word_mask, input_j, life)

        for j in range(len(input_test)):
            if input_test[j] is True:
                word_result += word_dic[j]
            else:
                word_result += "*"

        print(word_result)
        completed = functions.is_complet(word_mask)
    
    if completed is True:
        print("Well done, you win !")
    else:
        print("You lose...")
    
    again = input("Wanna play again ? (y/n) : ")
    new_game = functions.regex(again)
    correct = user_input(new_game, again)
    
    if correct == "y":
        round(pseudo)
    else:
        return


#Début du jeu

print("""
--------- HANGMAN ---------
          ________
          |/      |
          |      ( )
          |      /|\\
          |      / \\
        __|____
---------------------------

""")
player = input("Your pseudo : ")
round(player)

print("End, thanks for playing")