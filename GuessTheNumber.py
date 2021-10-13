"""
date: 10/13/2021
author: Ahmed Ryan
"""

from random import randint

start = 1
end = 1000

value = randint(start, end)

print('The computer chose a number between', start, 'and', end)

guess = None

while guess != value:
    text = input('Guess the number: ')
    guess = int(text)

    if guess < value:
        print('Your guess is lower than the number')
    elif guess > value:
        print('Your guess is higher than the number')

print('Congratulations!!! You guessed the number right!')
