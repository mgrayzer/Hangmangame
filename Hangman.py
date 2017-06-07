__author__ = 'mmwin8'
# -*- coding: utf-8 -*-
import random as r
import re
import csv
import winsound
import webbrowser as w


def main():
    game()


def game():
    words = []
    with open('wordlist.csv') as csvFile:
        file_words = csv.reader(csvFile)
        for rows in file_words:
            new_words = (', '.join(rows))
            words.append(new_words)

    def randoms():
        a = r.choice(words)
        return a
    secret_word = randoms()
    guesses_allowed = len(secret_word) + 3
    print('Welcome to the hangman game.')
    print('I am thinking of a word Which is ' + str(len(secret_word)) + ' letters long')
    print("You have got " + str(guesses_allowed) + " guesses")

    result = []

    def letter():
        b = input('Please guess a letter').lower()
        if not re.match('^[abcdefghijklmnopqrstuvwxyzäöüß]*$', b):
            print('Error Only letters from a-z allowed!')
            letter()
        elif len(b) > 1:
            print('Error one 1 letter allowed!')
            letter()
        elif b in result:
            print('Oops you have already guessed this letter!')
            letter()
        else:
            result.append(b)
        return b

    blank = ['_ '] * len(secret_word)
    counter = 0
    guesses_allowed2 = guesses_allowed

    while counter < guesses_allowed2:
        letter()
        for steps in result[-1]:
            if steps in secret_word:
                print('Correct guess well done!')
                winsound.PlaySound('correct.wav', winsound.SND_FILENAME)
            else:
                print('Sorry Incorrect guess!')
                winsound.PlaySound('Wrong.wav', winsound.SND_FILENAME)

        count = 0
        for i, c in enumerate(secret_word):
            if c in result:
                count += 1
                blank.insert(count-1, c)
                blank.pop(count)
            else:
                count += 1
                blank.insert(count-1, '_')
                blank.pop(count)
        result2 = ''.join(blank)

        print("This is your progress " + result2)

        if result2 == secret_word:
            print("You have gotten it huraaaaaaaaaaay!!")
            winsound.PlaySound('Applause.wav', winsound.SND_FILENAME)
            break
        if result[-1] not in secret_word:
            guesses_allowed2 += -1

        if guesses_allowed2 > 1:
            print("You have got " + (str(guesses_allowed2)) + " Guesses left")

        elif guesses_allowed2 == 0:
            print("You are dead the correct word is " + secret_word)
            w.open('https://em.wattpad.com/18d21d96bcc10003b9371cd\n'
                   'a793d061779447d40/687474703a2f2f322e62702e626c6\n'
                   'f6773706f742e636f6d2f2d3550\n'
                   '516d6a685a61495f4d2f554161773833696738474\n'
                   '92f41414141414141414677632f7a387a4d5755723034334d2\n'
                   'f73313630302f68616e676d616e362e676966')
            winsound.PlaySound('dead.wav', winsound.SND_FILENAME)

        else:
            print("You have got " + (str(guesses_allowed2)) + " Guess left")
    try_again = input("would you like to try again y/n?")
    if try_again == "y":
        game()
    else:
        print("good bye")

if __name__ == '__main__':
    main()
