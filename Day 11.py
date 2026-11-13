#Blackjack Capston Projects
import random

def card_deal(k = 1):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choices(cards ,  k = k)

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(p_score , d_score):
    if p_score == d_score:
        return "Drow"
    elif d_score == 0 :
        return "Lose, opponent has a Blackjack"
    elif p_score == 0:
        return "Win with a Blackjack"
    elif p_score > 21:
        return "You went over, You lose"
    elif d_score > 21:
        return "opponent went over, You win"
    elif p_score > d_score:
        return "You Win"
    else: 
        return "You lose"


def blackjack():
    is_game_over = False
    player_cards = []
    dealer_cards = []
    payer_score = -1
    dealer_score = -1

    player_cards += card_deal(k = 2) 
    dealer_cards += card_deal(k = 2)
    while(not is_game_over):
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                player_cards += card_deal()
                player_score = calculate_score(player_cards)
            else:
                is_game_over = True
    while(0 < dealer_score < 17 ):
        dealer_cards += card_deal()
        dealer_score = calculate_score(dealer_cards)
    
    print(f"Your final hand:{player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(player_score , dealer_score))
    

while(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y'):
    blackjack()
else:
    print("Game Over!!")

