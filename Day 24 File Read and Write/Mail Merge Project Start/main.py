#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt') as name_list:
    for name in name_list.readlines():
        with open('Input/Letters/starting_letter.txt') as file:
            data = file.readlines()
            data[0] = data[0].replace("[name]" , name.strip("\n"))
        with open(f"Output/readyToSend/{name.strip("\n")}.txt",'w') as letter:
            letter.writelines(data)



# with open('Input/Names/invited_names.txt') as names:
#     name = names.readline()