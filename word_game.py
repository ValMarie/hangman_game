import random
import string
from random_words import words


def get_valid_wordlist(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice (words)

    return word

def wordGame():
    word = get_valid_wordlist(words)
    letters = set(word)
    each_alphabet = set(string.ascii_lowercase)
    used_letters = set()

    no_of_trials = 4

    while len(letters) > 0 and no_of_trials > 0:
        # getting the used letters
        print("You have ", no_of_trials, "lives left and You have used these letters: ", " ".join(used_letters)) 

        # showing the current word
        current_word = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(current_word))

        inputted_letters = input("Guess the letter: ")
        if inputted_letters in each_alphabet - used_letters:
            used_letters.add(inputted_letters)
            if inputted_letters in letters:
                letters.remove(inputted_letters)
            else:
                no_of_trials = no_of_trials - 1
                print("Sorry, that letter ", inputted_letters, " is not in word")
        
        elif inputted_letters in used_letters:
            print("You already used that letter")

        else:
            print("Invalid entry. Try again")
        print("\n") 

    if no_of_trials == 0:
        print("GAME OVER \n Sorry the word is", word)
    else:
        print("Good job!\n You correctly guesed the word", word)
    
        
        

player_input = print("Guess the  word: ")
wordGame()


