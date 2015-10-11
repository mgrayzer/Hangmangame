__author__ = 'mmwin8'
#-*- coding: utf-8 -*-

import random as r
import re
import csv
import winsound


def main():
    game()


def game():
    words = []
    with open('wordlist.csv') as csvFile:
        fileWords = csv.reader(csvFile)
        for rows in fileWords:
            newWords = (', '.join(rows))
            words.append(newWords)

    def randoms():
        a = r.choice(words)
        return a
    secretWord = randoms()
    guessesAllowed = len(secretWord) + 3
    print('Welcome to the hangman game.')
    print('I am thinking of a word Which is '+ str(len(secretWord)) + ' letters long')
    print("You have got " + str(guessesAllowed) + " guesses")

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

    blank = ['_ '] * len(secretWord)
    counter = 0
    guessesAllowed2 = guessesAllowed
    import webbrowser as w

    while counter < guessesAllowed2:
        letter()
        for steps in result[-1]:
            if steps in secretWord:
                print('Correct guess well done!')
                winsound.PlaySound('C:/Users/mmwin8/Desktop/MekhiPython/correct.wav',winsound.SND_FILENAME)
            else:
                print('Sorry Incorrect guess!')
                winsound.PlaySound('C:/Users/mmwin8/Desktop/MekhiPython/Wrong.wav',winsound.SND_FILENAME)

        count = 0
        for i, c in enumerate(secretWord):
            if c in result:
                count += 1
                blank.insert(count-1,c)
                blank.pop(count)
            else:
                count += 1
                blank.insert(count-1, '_')
                blank.pop(count)
        result2 = ''.join(blank)

        print("This is your progress " + result2)

        if result2 == secretWord:
            print("You have gotten it huraaaaaaaaaaay!!")
            winsound.PlaySound('C:/Users/mmwin8/Desktop/MekhiPython/Applause.wav',winsound.SND_FILENAME)
            break
        if result[-1] not in secretWord:
            guessesAllowed2 += -1

        if guessesAllowed2 > 1:
            print("You have got " + (str(guessesAllowed2)) + " Guesses left")

        elif guessesAllowed2 == 0:
            print("You are dead the correct word is " + secretWord)
            w.open('https://em.wattpad.com/18d21d96bcc10003b9371cd\n'
                   'a793d061779447d40/687474703a2f2f322e62702e626c6\n'
                   'f6773706f742e636f6d2f2d3550\n'
                   '516d6a685a61495f4d2f554161773833696738474\n'
                   '92f41414141414141414677632f7a387a4d5755723034334d2\n'
                   'f73313630302f68616e676d616e362e676966')
            winsound.PlaySound('C:/Users/mmwin8/Desktop/MekhiPython/dead.wav',winsound.SND_FILENAME)

        else:
            print("You have got " + (str(guessesAllowed2)) + " Guess left")
    tryAgain = input("would you like to try again y/n?")
    if tryAgain == "y":
        game()
    else:
        print("good bye")


main()
