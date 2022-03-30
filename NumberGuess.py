import random
x = random.randint(1, 99)

def userGame():
    secret_number = random.randint(x, 100)
    user_guess = 0
    while user_guess != secret_number:
        user_guess = int(input(f"Guess a number between {x} and 100: "))
        if user_guess > secret_number:
            print("The number is smaller!")
        elif user_guess < secret_number:
            print("The number is larger!")
        elif user_guess == secret_number:
            print("You got it!!!! :D")
            break

def computerGuess():
    user_number = int(input("Enter a number 1-100 you want the computer to guess: "))
    smallest_num = 1
    largest_num = 100
    while True:
        computer_guess = random.randint(smallest_num, largest_num)
        print(f"The computer guessed {computer_guess}")
        if computer_guess > user_number:
            print("It guessed too high this time")
            largest_num = computer_guess - 1
        elif computer_guess < user_number:
            print("It guessed too low this time")
            smallest_num = computer_guess + 1
        elif computer_guess == user_number:
            print("The computer got it!!")
            break

while True:
    user_input = input("Would you like to guess the number(play), make the computer guess(computer) or quit (q): ")
    if user_input == "play":
        userGame()
    elif user_input == "computer":
        computerGuess()
    elif user_input == "q":
        print("Quitting")
        break
    else:
        print("Invalid input")
        
