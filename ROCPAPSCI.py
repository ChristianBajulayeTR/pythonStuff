import random
#add a SCOREBOARD
playOptions = ["Rock", "Paper", "Scissors"]
computer = playOptions[random.randint(0, 2)]

player = False

while player == False:
    player = input("Rock, Paper or Scissors: ").capitalize()
    if player == computer:
        print(f"Its a Tie! You both chose {computer}")
    if player == "Rock":
        if computer == "Paper":
            print("You Lost. Paper covers Rock")
        elif computer == "Scissors":
            print("YOU WON! Rock smashes Scissors")
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lost. Scissors cuts Paper")
        elif computer == "Rock":
            print("YOU WON! Paper covers Rock")
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lost. Rock smashes Scissors")
        elif computer == "Paper":
            print("YOU WON! Scissors cuts Paper")

    play_Again = input("play again? y/n: ")
    if play_Again == "y":
        player = False
        computer = playOptions[random.randint(0, 2)]


