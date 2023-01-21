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
        result = "It's a tie!"
    # Combinations for user to win
    elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors"):
        result = "You won!"
    # All other Combinations means Computer wins
    else:
        result = "You lost"
    print(result)
    return result