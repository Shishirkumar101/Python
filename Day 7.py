import random
world_list = ['aardvark', 'baboon', 'camel']

word = random.choice(world_list)
print(word)
blank_word = ['_']*len(word)
print(*blank_word)
life = 6
while(life != 0 and '_' in blank_word):
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in word:
        if guess_letter not in blank_word:
            for i in range(len(word)):
                if guess_letter == word[i]:
                    blank_word[i] = guess_letter
        
        else:
            print("You already guessed this word!")
        
    else:
        print("Wrong word! Guess again. ")
        life -= 1
    print(*blank_word)
    print(f"life remaning : {life}")
print("GAME OVER!!!!")