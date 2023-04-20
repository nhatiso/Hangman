# Hangman
The Hangman game is played betweeen person and computer. The person is expected to guess a fruit name and match it with the randomly selected name by the computer.
A Hangman class is created with two parameters word_list and num_lives used in the three methods.
The check_guess method :
     - checks whether the guess is correct.
     - reduces the number of unguessed letters whenever a correct guess is given
     - reduces the number of lives if incorrect guess is given
The ask_for_input function:
    - prompts the user for input and checks its validity
    - appends all valid guesses to the list_of _guesses 
The play_game method
    - runs all the code for the game
    - it establish the game outcome, that is a win or loss depending on the person's inputs.
