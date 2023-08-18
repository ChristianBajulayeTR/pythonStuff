import random
import words
import string

# Getting a valid word
def get_valid_word(words):
    word = random.choice(words)  # this variable will choose a random word from the list of words

    while " " or "-" in word:  # all words with a dash or space in between are not valid selections
        word = random.choice(words)  # any time there is a dash or space in the word will be re-chosen
        return word  # returns the word

def hangman():
    word = get_valid_word(words)  # localising the get_valid_word variable
    word_letters = set(word)  # variable saves all letters in a word as a set
    alphabet = string.ascii_uppercase  #
    used_letters = set()  # keeping set empty as will be used to keep track of what the player has guessed

    # getting user input
    user_letter = input("Guess a letter: ").upper()  # asks for user input and automatically converts it into upper case
    if user_letter in alphabet and not in used_letters:
        used_letters.add()

    if user_letter in word_letters:
        word_letters.remove()
    elif:
        user_letter in used_letters:
        print("You have already")

