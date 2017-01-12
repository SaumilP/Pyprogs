#!/usr/bin/python

import random
import re
from pics import Pictures
from colors import Colors

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard
llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python
rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider
stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'''.upper().split()

def get_random_word(wordlist):
    word_index = random.randint(0, len(wordlist)-1)
    return wordlist[word_index]

def display_board(PICS, missed_letters, correct_letters, secret_word):
    print(PICS[len(missed_letters)])
    print('')

    print("Missed letters: {}\n".format(','.join(missed_letters)))

    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    print("{}\n".format(' '.join(blanks)))

def get_guess(alread_guessed):
    while True:
        guess = raw_input(">>> ")
        guess = guess.upper()
        if len(guess) != 1:
            print(Colors.WARNING + "Please enter a single letter." + Colors.ENDC)
        elif guess in alread_guessed:
            print(Colors.WARNING + "You have already guessted that letter, Choose again." + Colors.ENDC)
        elif len(re.findall('[^a-zA-Z]',guess)) > 0:
            print(Colors.WARNING + "Please enter a LETTER." + Colors.ENDC)
        else:
            return guess

def play_again():
    print("Do you want to play again? (yes or no)")
    return raw_input().lower().startswith('y')

print('==== H A N G M A N ====')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words).upper()
game_is_done = False

while True:
    display_board(Pictures.HANGMAN_PICS, missed_letters, correct_letters, secret_word)

    # let the player type in a letter
    guess = get_guess(missed_letters + correct_letters)
    if guess in secret_word:
        correct_letters = correct_letters + guess

        # check if the player has won
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print(Colors.OKGREEN + 'Yes! The secret word is "' + secret_word + '"! You have won' + Colors.ENDC)
            game_is_done = True
    else:
        missed_letters = missed_letters + guess

        # check if player has guessed too many times and lost
        if len(missed_letters) == len(Pictures.HANGMAN_PICS)-1:
            display_board(Pictures.HANGMAN_PICS, missed_letters, correct_letters, secret_word)
            print(Colors.FAIL + 'You have run out of guess!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '"' + Colors.ENDC)
            game_is_done = True

    # Ask the player if they want to play again
    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break
