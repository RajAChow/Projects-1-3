import random
#This list helps with the redunacy instead of typing "rock", "paper", "scissors", "lizard", "spock" repeatedly
moves = ["rock", "paper", "scissors", "lizard", "spock"]
    
#This function check who won a round 
def checkWinner(user_choice, computer_choice):
    #This checks if the user chose the computer chose the same move then prints a relevant statment
    if user_choice == computer_choice:
        print(f"You both chose {user_choice}, it's a tie!")
    #This checks if the user chose a winning move against the computer then prints a relevant statment 
    elif (user_choice == moves[0] and (computer_choice == moves[2] or computer_choice == moves[3])) or \
    (user_choice == moves[1] and (computer_choice == moves[0] or computer_choice == moves[4])) or \
    (user_choice == moves[2] and (computer_choice == moves[1] or computer_choice == moves[3])) or \
    (user_choice == moves[3] and (computer_choice == moves[4] or computer_choice == moves[1])) or \
    (user_choice == moves[4] and (computer_choice == moves[2] or computer_choice == moves[0])):   
        return True
    else:
        return False 

#This function repeatedly asks the user and computer for a move, then checks to see who won and records the result
def playMove():
        #The two "counts" count how many wins the user and computer has
    win_count = 0
    loss_count = 0
    while True:
        user_choice = input("To play type rock, paper, scissors, lizard, Spock or q to quit: ")
        user_choice = user_choice.lower()
        computer_choice = random.choice(moves)
        if user_choice in moves:
            if checkWinner(user_choice, computer_choice) == True:
                win_count += 1
                print(f"You won by choosing {user_choice} and the computer choosing {computer_choice}")
            elif checkWinner(user_choice, computer_choice) == False:
                loss_count += 1
                print(f"You lost because the computer chose {computer_choice} and you chose {user_choice}") 
        elif user_choice == "q":
            print(f"You won {win_count} time(s) \nThe computer won {loss_count} time(s)")
            break  
        else:
            print("Invalid input")    

playMove()
