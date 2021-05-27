from random import choice
from string import ascii_lowercase
from sys import exit


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


print('H A N G M A N')
while True:
    print('Type "play" to play the game, "exit" to quit:')
    if input() == 'play':
        break
    if input() == "exit":
        exit()
    else:
        continue

words_list = ['python', 'java', 'kotlin', 'javascript']
word = choice(words_list)
hidden_word = list('-' * len(word))
lives = 8
letter_list = []
while lives != 0:
    if '-' not in hidden_word:
        break
    while True:
        print('\n' + ''.join(hidden_word))
        letter = input('Input a letter: ')
        if len(letter) >= 2:
            print('You should input a single letter')
            continue
        if letter in ascii_lowercase:
            break
        else:
            print('Please enter a lowercase English letter')
            continue
    if letter in letter_list:
        print("You've already guessed this letter")
        continue
    if letter in set(word):
        if letter in set(hidden_word):
            print("You've already guessed this letter")
            letter_list.append(letter)
            continue
        else:
            for index in find(word, letter):
                hidden_word[index] = letter
                letter_list.append(letter)
    else:
        lives -= 1
        print("That letter doesn't appear in the word")
        letter_list.append(letter)
if '-' not in hidden_word:
    print('You survived!')
else:
    print('You lost!')
