import random

your_choice = input("Please choice between, rock, paper and scissors: ").lower()

choices = ["rock", "paper", "scissors"]



computer_choice = random.choice(choices)

if computer_choice == your_choice:
        print ("It is a Draw!!!")
else:
    if your_choice == "paper":
        if computer_choice == "rock":
            print("You Win! The computer choosed rock and you paper, paper cover rock. ")
        if computer_choice == "scissors": 
            print (" You Loose!!The computer choosed scissors and you paper, scissor cut paper. ")
    if your_choice == "rock":
        if computer_choice == "paper":
            print("You loose! The computer choosed paper and you rock, paper cover rock. ")
        if computer_choice == "scissors": 
            print (" You Win !!The computer choosed scissors and you rock, rock broke scissor. ")    
    if your_choice == "scissors":
        if computer_choice == "paper":
            print("You Win! The computer choosed paper and you scissors, scissor cut paper. ")
        if computer_choice == "rock": 
            print (" You loose !!The computer choosed rock and you scissors, rock broke scissor. ")    
    
     