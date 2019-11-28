import donnees
from random import randrange

random_index = randrange(len(donnees.word))
random_word = donnees.word[random_index]

word = {}
word_mask = {}

def player(pseudo):
            #chercher / écrire info fichier score_player

    # if donnees.player_profil[pseudo]:
    #     game(random_word, donnees.player_profil[vie])
    # else:
    #     donnees.player_profil["pseudo"] = pseudo
    #     donnees.player_profil["vie"] = 8
    #     game(random_word, donnees.player_profil[vie])


def create_mask(word_rand):
    i = 0
    for letter in word_rand:
        word[i] = letter
        word_mask[i] = "*"
        i = i + 1

create_mask(random_word)

def write_letter_try(dico) :
    l = 0
    PAST = ""
    try:
        for letter in dico.values():
            FUTUR = PAST + dico[l] + " - "
            PAST = FUTUR
            l += 1
    except NameError:
        pass
    else:
        print("Wrong guess : ", PAST)

def write_word_mask() :
    k = 0
    past = ""

    for letter in random_word:
        futur = past + word_mask[k] + " "
        past = futur
        k = k + 1
    print("The word : ", past)

def victory(stop):
    if word_mask == word:
        stop = True
    else:
        write_word_mask()

def game(word, life):
    guess = {}
    x = 0
    end_game = False
    while life > 0:
        write_word_mask()
        essai = input("\nenter a letter : ")
        guess[x] = essai
        x += 1
        j = 0
        succes = False
        for letter in random_word:
            if letter == essai:
                word_mask[j] = essai
                succes = True
                j = j + 1
            else:
                j += 1
        
        if succes == False:
            life = life - 1

        elif succes == True:
            victory(end_game)
            print(end_game)


        print("Essaie restant : ", life)
        write_letter_try(guess)