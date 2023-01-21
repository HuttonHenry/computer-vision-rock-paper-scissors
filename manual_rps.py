import random

def get_computer_choice():
    rps = [ "Rock", "Paper", "Scissors"]
    choice = random.choice(rps)

def get_user_choice():
    req = input("Please make a choice.")
