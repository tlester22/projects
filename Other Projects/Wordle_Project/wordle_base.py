import random
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.mit.edu/~ecprice/wordlist.10000'

pg = requests.get(URL)

soup = bs(pg.text, 'html')

words= soup.find('p').text

my_list = words.split('\n')

def wordle_input():
    while True:
        guess = input('Type your 5-letter word guess here: ')
        if len(guess) == 5 and guess in final_list:
            new_guess = guess.lower()
            return new_guess
        elif len(guess) == 5 and guess not in my_list:
            print('Not a word in list.')
        else:
            print('Please choose a 5-letter word.')
def answer_pick():
    answer = random.choice(final_list)
    return answer
def wordle_play():
    answer = answer_pick()
    tries = 1
    while tries <= 6:
        new_guess = wordle_input()
        n = 0
        while n < 5:
            if new_guess[n] == answer[n]:
                print('right!')
            elif new_guess[n] in answer:
                print('so close!')
            else:
                print('wrong.')

            n += 1

        if new_guess == answer:
            print('You win!')
            tries = 7
        else:
            print('Next try.')
            tries += 1
    replay = input('Do you want to play again? y/n')
    if replay.lower() == 'y':
        wordle_play()
    elif replay.lower() == 'n':
        print('Thanks for playing!')
    else:
        print("Please type 'y' or 'n'. ")
wordle_play()