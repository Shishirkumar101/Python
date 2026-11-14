import random
Data = [{
        'name' : 'shishir',
         'country': 'India',
         'follower': 10000
        },
        {
         'name' : 'shishir1',
         'country': 'India',
         'follower': 11000
        },
        {
        'name' : 'shishir2',
        'country': 'India',
        'follower': 12000
        },
        {
        'name' : 'shishir3',
        'country': 'India',
        'follower': 13000
        },
        ]

def check_answer(a, n1, n2, s):
    if a == 'a' and n1['follower'] > n2['follower']:
        return 1 
    elif a == 'b' and n1['follower'] < n2['follower']:
        return 1
    else:
        return -1

def high_low():
    number = random.choice(Data)

    score = 0
    game_over =False

    while(game_over != True):
        number2 = random.choice(Data)
        while(number == number2):
            number2 = random.choice(Data)
        print(f"Compare A: {number['name']}, from {number['country']} ")
        print('VS')
        print(f"Against B: {number2['name']}, from {number2['country']}")
        ans = input("Who has more followers? Type 'A' or 'B': ").lower()
        result = check_answer(ans , number , number2, score)
        if result == -1:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
        else:
            score+=result
            print(f"You're right! Current score: {score}.")
            number = number2

high_low()