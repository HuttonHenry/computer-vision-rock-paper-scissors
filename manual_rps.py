import random

def get_computer_choice():
    rps = [ "Rock", "Paper", "Scissors"]
    choice = random.choice(rps)
    return choice

def get_user_choice():
    try:
        while True:
            choice = ["rock", "paper", "scissors"]
            user_choice = input('Please enter one of the following: "Rock", "Paper", "Scissors"').lower()
            if user_choice in choice:
                break
            else:
                print('Not a valid entry!')
        return user_choice
    except:
        print("error")

def get_winner(computer_choice,user_choice):
    if computer_choice == user_choice:
        print("It's a tie!")
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print("You win!")
        else:
            print("You lost.")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("You win!")
        else:
            print("You lost.")
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            print("You win!")
        else:
            print("You lost.")
