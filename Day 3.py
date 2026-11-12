"""
#Task 1
Number = int(input("Enter a number: "))
if Number % 2:
    print("Odd")
else:
    print("Even")


#Task 2

print("Welcome to Python pizza delivery!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese n your pizza? Y or N: ")

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == 'Y':
        bill+=1
    print(f"Total bill : {bill}")
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == 'Y':
        bill+=1
    print(f"Total bill : {bill}")
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == 'Y':
        bill+=1
    print(f"Total bill : {bill}")
else:
    print("Enter correct choice")

"""

#Final Task

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go ?")
ans = input('Type "left" or "right"\n').lower()
if ans != 'left':
    print("You fell into a hole. Game Over")
else:
    print("You've come to a lake. There is an island in the middle of the lake")
    ans = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if ans != 'wait':
        print("You get attacked by an angry trout. Game Over.")
    else:    
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        ans = input('One red, one yellow and one blue. Which colour do you choose?\n').lower()
        if ans == 'red':
            print("It's a room full of fire. Game Over.")
        elif ans =='blue':
            print("You enter a room of beasts. Game Over.")
        elif ans =='yellow':
            print("You found the treasure! You Win!")
        else:
            print("Wrong Choice Game Over.")    