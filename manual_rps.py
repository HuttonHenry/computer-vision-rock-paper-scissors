import random


def get_computer_choice():
    rps = [ "Rock", "Paper", "Scissors"]
    choice = random.choice(rps)
    return choice

def get_user_choice():
    req = input("Please enter Rock, Paper or Scissors")
    return req

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        winner = "It is a tie!" 
    # User wins under these conditions.
    elif (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Scissors" and user_choice == "Rock") :
        winner = "You won!"
    # Otherswise the computer wins
    else:
        winner = "You lost"
    print(winner)
    return winner

def play():
    a=get_computer_choice()
    b=get_user_choice()
    get_winner(a,b)