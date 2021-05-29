"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    remaining_guesses = INITIAL_GUESSES

    word_length = len(secret_word)
    word = ""

    for i in range(word_length):
        word += "-"

    while True:
        print('The word now looks like this: ' + word)
        print('You have ' + str(remaining_guesses) + ' guesses left')
        ch = input('Type a single letter here, then press enter: ').upper()

        if len(ch) != 1:
            print('Guess should only be a single character.')
            continue

        isPresent = False

        for i in range(word_length):
            if secret_word[i] == ch:
                word = word[:i] + ch + word[i + 1:]
                isPresent = True
        
        if isPresent == False:
            remaining_guesses -= 1
            print('There are no ' + str(ch) + '\'s in the word')
        else:
            print('That guess is correct.')

        if word == secret_word:
            print('Congratulations, the word is: ' + str(word))
            return

        if remaining_guesses == 0:
            print('Sorry, you lost. The secret word was: ' + str(secret_word))
            return


def get_word():
    f = open(LEXICON_FILE)
    words = []

    for line in f:
        words.append(line.strip())

    f.close()

    index = random.randrange(len(words))

    return words[index]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
