import random;

#user choice

player_input=input("Enter your choice")
player_input=player_input.lower()
while(player_input!="rock" and player_input!="paper" and player_input!="scissor"):
    print(player_input)
    player_input=input("Invalid Choice....Enter Again!!!")
    player_input=player_input.lower()

#Computer Choice
    
computerInt = random.randint(0,2)
if (computerInt == 0):
                computer_input = "rock"
elif (computerInt == 1):
                computer_input = "paper"
elif (computerInt == 2):
                computer_input = "scissor"
else:
                computer_input = "Wrong Choice"


#winner


if(player_input==computer_input):
    print("Draw")
elif(player_input=="rock"):
    if (computer_input=="scissor"):
        print("Player Wins")
    else:
        print("Computer Wins")

elif(player_input=="paper"):
    if(computer_input=="scissor"):
        print("Computer Wins")
    else:
        print("Player Wins");

elif(player_input=="scissor"):
    if(computer_input=="paper"):
        print("player wins")
    else:
        print("Computer Wins")
        
print(" Your Choice "+ player_input + " Computer Choice " + computer_input)
