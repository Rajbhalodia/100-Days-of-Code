import random

rock = "rock"
papper = "papper"
sicssor ="sicssor"

userchoice = (int(input('''
1. Type 0 for rock
2. Type 1 for papper
3. Type 2 for sicssor \n''')))

computer_choice = random.randint(0,2)
print(f"Computer has choose {computer_choice}")

if userchoice >= 3 or userchoice<0:
    print("Number is invalid, You Loose")
elif computer_choice == 0 and userchoice == 2:
    print("Computer WINS THE GAME")
elif computer_choice > userchoice:
    print("OH NO! COMPUTER WINS")
elif userchoice > computer_choice:
    print("Hurray! You have managed to defeat the Computer")
elif userchoice == computer_choice:
    print("IT IS A DRAW")
elif userchoice ==0 and computer_choice ==2:
    print("Hurray! You have defeated the Computer")
else:
    print("You typed an Invalid INPUT NUMBER, You Lose HEHEHEHEHE")