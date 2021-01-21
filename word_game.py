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
    each_alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(letters) > 0:
        # getting the used letters
        print("You have used these letters: ", " ".join(used_letters)) 

        # showing the current word
        current_word = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(current_word))

        inputted_letters = input("Guess the letter: ").upper()
        if inputted_letters in each_alphabet - used_letters:
            used_letters.add(inputted_letters)
            if inputted_letters in letters:
                letters.remove(inputted_letters)
        
        elif inputted_letters in used_letters:
            print("You already used that leter")

        else:
            print("Invalid entry. Try again")

wordGame()
# player_input = input("Guess the  word: ")

