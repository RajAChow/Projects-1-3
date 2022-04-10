import random
from library import words, hangman_pics, good_guess, bad_guess
import string
import time
alphabet = set(string.ascii_uppercase)

#This function chooses the word the user must guess
def wordToGuess(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    #this boolean assures that the following words are not selected    
    if word != "kwantlen" and word != "rai" and word != "zimmerman":
        return word.upper()

#This is the main function where the game is played
def playGame():
    hangman_pics.reverse()
    #The line below calls my unique function go to line 108 to see what it does
    user_list = makeList()
    #This intial while loop will continue playing the game until the user quits
    while True:
        """
        If the user inputs m when the makeList() function is being run, user_list will never = False
        leaving the option to play with either their own list or the default one every time
        """
        if user_list != False:
            while True:
                user_list_type_check = input("\nDo you want to use your own list (o) or the default one (d)?: ")
                user_list_type_check.lower()
                if user_list_type_check == "o":
                    game_word = wordToGuess(user_list)
                    break
                elif user_list_type_check == "d":
                    game_word = wordToGuess(words)
                    break
                else:
                    print("Invalid input")
            """
            #If the user inputs n when the makeList() function is being run, user_list will = False
            and the user won't be able to play with their own list, until they restart the code
            """
        elif user_list == False:
            game_word = wordToGuess(words)
        game_letters = set(game_word)
        user_guessed = set()
        
        user_lives = 6
        
        while len(game_letters) > 0 and user_lives > 0:
            print("\nYou have", user_lives, "lives left and you guessed these letter: ", " ".join(sorted(user_guessed)))
            show_word_guess = [letter if letter in user_guessed else "_" for letter in game_word]
            print("Word: :", " ".join(show_word_guess))
            
            user_letter_guess = input("Guess a letter: ").upper()
            if user_letter_guess in alphabet - user_guessed:
                user_guessed.add(user_letter_guess)
                if user_letter_guess in game_letters:
            #The two time.sleep(1) in the code adds a one second delay before revealing a result
                    time.sleep(1)
                    game_letters.remove(user_letter_guess)
                    if len(game_letters) > 0:
                        #good_guess is an imported list, printing it will print 1 of 7 unique "right guess" messages
                        print(f"\n{random.choice(good_guess)}")
                else:
                    time.sleep(1)
                    user_lives -= 1
                    """
                    If the user has a wrong output, it will print a picture of the 
                    hangman corresponding to the number of lives the user has
                    """
                    print(hangman_pics[user_lives])
                    #bad_guess is an imported list, printing will print 1 of 7 unique "wrong guess" messages
                    print(random.choice(bad_guess))
            elif user_letter_guess in user_guessed:
                print("You already guessed this letter")
            else:
                print("Inavlid input")
        
        if user_lives == 0:
            print(f"\n{hangman_pics[user_lives]}")
            print(f"You didn't get the word {game_word} in time")
        else:
            print(f"\nYou got the word {game_word}")
        
        #This repeatedly asks the user if they want to play again until they enter a valid output
        while True:
            user_play_again = input("do you want to play again (y) or quit (q)?: ")  
            user_play_again.lower()
            if user_play_again.lower() == "y":
                print("Playing again")
                break
            elif user_play_again.lower() == "q":
                print("gg")
                break
            else:
                print("Invalid input")
        
        #this continues the intial while loop, continuing the game
        if user_play_again.lower() == "y":
            continue
        #this break out of the intial while loop, ending the game
        break 

#This is my unique function that allows the user to make their own list once at the start of their playthrough
def makeList():
    user_list = []
    #It is asked at the start if the user wants to make a list or not, you cannot edit your list or change your mind after
    while True:
        user_input = input("\nDo you want to make your own word list (m) or no (n)?: ")
        user_input.lower()
        #If they input m, they will be asked for a word to add
        if user_input == "m":
            while True:
                user_input = input("\nDo you want to add a word (a) to your list or quit (q)?: ")
                user_input.lower()
                if user_input == "a":
                    word = input("Type the word you want to add: ")
                    word = word.upper()
                    #This for loop assures that there are only letters in the user's word
                    for x in word:
                        y = 1
                        if x in alphabet:
                            continue
                        elif x not in alphabet:
                            y = 0
                            print("Please enter a valid word")
                            break
                    #If there is only letters then the word is added to the list
                    if y != 0:   
                        user_list.append(word)
                        """
                        This checks if the user wants to stop making the list, however if you said you wanted to 
                        make a list at the start, you can't quit without adding at least one thing to the list
                        """            
                elif user_input == "q":
                    if len(user_list) > 0:
                        return user_list
                        break
                    else:
                        print("You have to add at least one thing to the list")
                        continue
                else:
                    print("Invalid input")
        #If the user inputs n at the start, they won't make a list
        elif user_input == "n":
            print("No user list")
            return False
            break
        else:
            print("Invalid input")
        
playGame()
