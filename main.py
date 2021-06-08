import random
import hangman_art
import hangman_words
#import replit

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#print logo art
print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
past_guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #replit.clear()
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess not in past_guesses:
        past_guesses += guess
        #print(past_guesses)
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
            #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f"You chose {guess}, that is not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You have no more lives left! You lose.")
                print(f"The word is {chosen_word}")
    else:
        print("You have already guessed that letter.")  

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py.
    print(hangman_art.stages[lives])