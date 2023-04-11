
import random
word_list = ['mango', 'apple', 'orange', 'pineapple', 'peach']
class Hangman:
    def __init__(self, word_list,num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = list(' ' *len(self.word))
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        

    def  check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for index,char in enumerate(list(self.word)):
                if char == guess:
                    self.word_guessed[index] = guess        
            self.num_letters -=1
        else:
            self.num_lives -=1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} left')
       
    # ask for input method
    def ask_for_input(self):
        while True:
            guess = input('Please enter a single letter - ') 
            if guess.isdigit() or (guess.isalpha() and len(guess) >1):
                print('Invalid letter. Please, enter a single alphabetical character')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess) 
                self.list_of_guesses.append(guess)
                     
    
hangman = Hangman(word_list,num_lives=5)
hangman.ask_for_input()                   

                
            
                 



        
