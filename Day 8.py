letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encode():
    encoded_message = ""
    message = input("Type your message:\n").lower()
    shift_no = int(input("Type the shift number: "))
    for i in message:
        if i in letter:
            index = letter.index(i)
            encoded_message+= letter[(index+shift_no)%26]
        else:
            encoded_message+=i
    print("".join(encoded_message))

def decode():
    decoded_message = ""
    message = input("Type your message:\n").lower()
    shift_no = int(input("Type the shift number: ")) + 26
    for i in message:
        if i in letter:
            index = letter.index(i)
            decoded_message+= letter[(index-shift_no)%26]
        else:
            decoded_message+=i
    print("".join(decoded_message))

again = 'yes'
while(again == 'yes'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
    if direction == 'encode':
        encode()
    elif direction == 'decode':
        decode()
    else:
        print("wrong choice")
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
print("GoodBye!")

