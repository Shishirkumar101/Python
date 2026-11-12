#Task 1
'''import random

if random.randint(0,1):
    print("Heads")
else:
    print("Tails")
'''

#Final Task
import random
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
---'   ____)____
          ______)
          _______)
          _______)
---.───────────┘
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

game = [rock , paper, scissors]
user_choice = int(input("What do you choose? type 0 for rock, 1 for paper or 2 for scissors "))
if user_choice < 3 and user_choice > 0:    
    print("USER CHOICE")
    print(game[user_choice])
computer_choice = random.randint(0,2)
print("COMPUTER CHOICE")
print(game[computer_choice])
if user_choice >= 3 or user_choice < 0:
    print("Wrong Choice game over!!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!!")
elif user_choice > computer_choice :
    print("You Win!!")
elif user_choice == computer_choice:
    print("its a drow!!")
else:
    print("You Lose!!")