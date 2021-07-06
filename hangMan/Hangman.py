import random
import string
from words import words



def valid_word_check(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = valid_word_check(words)
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # what user has guessed

    # user input
    while len(word_letters) > 0:
        # letters used
        print("You've used:", ' '.join(used_letters))

        # what the current word is
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list), '\n')

        user_letter = input('Pick a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You've already guessed that!")
        else:
            print('The hell is that?')

if __name__ == '__main__':
    hangman()
