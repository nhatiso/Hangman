import random
word_list = ['mango', 'apple', 'orange', 'pineapple', 'peach']
word = random.choice(word_list)
guess = input('Please enter a single letter - ')
if len(guess) == 1 and guess.isalpha() :
    print('Good guess!')
else:
    print('Oops! That is not a valid input') 