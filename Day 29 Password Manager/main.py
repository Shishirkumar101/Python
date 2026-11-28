from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
            "s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J",
            "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    symbols = ["!","@","#","$","%","*","(",")","+"]

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symboles = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_letters + password_symboles

    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website_name = website_entry.get()
    email_address = email_entry.get()
    password = password_entry.get()

    if len(website_name) == 0:
        messagebox.showinfo(title="Oops" , message="Enter the Website")
    elif len(password) == 0:
        messagebox.showinfo(title="Oops" , message="Enter the Password")
    elif len(email_address) == 0:    
        messagebox.showinfo(title="Oops" , message="Enter the email/username")
    else:
        is_ok = messagebox.askokcancel(title=website_name , message=f"These are the detail entered: \nEmail: {email_address} \nPassword: {password} \nIs it ok to save?")
        if is_ok:    
            with open("data.txt", 'a') as file:
                file.write(f"{website_name} | {email_address} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=20 , pady=20)


canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100 , image=logo_img)
canvas.grid(column = 1, row=0)


# Labels
website_text = Label(text="Website:")
website_text.grid(column = 0, row = 1)

email_text = Label(text="Email/UserName:")
email_text.grid(column = 0,row=2)

password_text = Label(text="Password:")
password_text.grid(column=0,row=3)

# Entry
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1 , row=1, columnspan=2)


email_entry = Entry(width=35)
email_entry.insert(0,"shishir@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

# Button
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2 ,row=3)

add = Button(text="Add", width=30 , command=save_data)
add.grid(column=1 , row=4, columnspan=2)

windows.mainloop()