#Task 1
score = [63, 71, 98, 84, 67, 92, 76, 89, 60, 95]
max = 0
for i in score:
    if i > max:
        max = i
print(max)

#Final Task
import random
letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
         "s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J",
         "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","*","(",")","+"]
print("Welcome to the PyPassword generator!")
nr_letters = int(input("How manay letter would you like in your password?\n"))
nr_number = int(input("How manay numbers would you like?\n"))
nr_symbol = int(input("How many symbols would you like?\n"))
password = []
for i in range(nr_letters):
    password.append(random.choice(letters))
for i in range(nr_number):
    password.append(random.choice(numbers))
for i in range(nr_symbol):
    password.append(random.choice(symbols))

print(''.join(password))
random.shuffle(password)
print(''.join(password))