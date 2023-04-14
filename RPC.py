import random

RPC = ["rock", "paper", "scissor"]

while True:
    player_choice = input("\nrock, paper, scissor, shoot!!!\nPlayer choice: ")

    AI_choice = random.choice(RPC)
    print("AI choice: "+ AI_choice)
    
    if(AI_choice == player_choice):
        print("Issa tie!!")
    else:
        if(AI_choice == "rock"):
            if(player_choice == "paper"):
                win = True
            else:
                win = False

        if(AI_choice == "paper"):
            if(player_choice == "scissor"):
                win = True
            else:
                win = False

        if(AI_choice == "scissor"):
            if(player_choice == "rock"):
                win = True
            else:
                win = False
        
        if(win):
            print("You win!!")
        else:
            print("you suck!!!!!")