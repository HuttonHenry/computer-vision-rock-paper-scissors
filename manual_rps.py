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
        result = "Draw"
    # Combinations for user to win
    elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors"):
        result = "User Wins!"
    # All other Combinations means Computer wins
    else:
        result = "Computer Wins!"
    print(result)
    return result