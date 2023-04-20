import random
word_list = ['mango', 'apple', 'orange', 'pineapple', 'peach']
class Hangman:
    ''' 
    The Hangman class with its methods.
    '''
    def __init__(self, word_list,num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = list(' ' *len(self.word))
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    '''
    The check_guess method :
     > checks whether the guess is correct.
     > reduces the number of unguessed letters whenever a correct guess is given
     > reduces the number of lives if incorrect guess is given
     '''    
        

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
       
    '''
    The ask_for_input function:
    > prompts the user for input and checks its validity
    > appends all valid guesses to the list_of _guessses
    '''
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
                print(f'{self.word_guessed}')
                break
                     
    '''
    The play_game method
    > runs all the code for the game'''
    def play_game(self,word_list):
        
        self.num_lives = 5
        while True:
            
            if self.num_lives == 0:
               print('You have lost !')
               break  
            elif self.word_guessed == list(self.word):
                print('Conratulations. You have won the game !')
                break 
            else:
                self.ask_for_input()
                 
            
               
            

                      
game = Hangman(word_list,num_lives=5)
game.play_game(word_list)