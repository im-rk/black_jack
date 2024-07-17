import random
from replit import clear
from art import logo

def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def play():
    print(logo)

    user_cards=[]
    computer_cards=[]

    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    def calculate_score(cards):
        if sum(cards)==21 and len(cards)==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)
    is_game_over=False
    while not is_game_over:

        user_score=calculate_score(user_cards)
        computers_score=calculate_score(computer_cards)


        print(f"Your cards: {user_cards} ,Your score: {user_score} ")
        print(f"computer first cards:{computer_cards[0]}")


        if user_score==0 or computers_score==0 or user_score>21:
            is_game_over=True
        else:
            userin=input("Type 'y' to get another card ,type 'n' to pass :")
            if userin=='y':
                user_cards.append(deal_cards())
            else:
                is_game_over=True

    while computers_score!=0 and computers_score<17:
        computer_cards.append(deal_cards())
        computers_score=calculate_score(computer_cards)

    
    print(f"your final hand :{user_cards},your final score :{user_score}")
    print(f"computers final hand :{computer_cards},computers final score :{computers_score}")
    print(compare(user_score, computers_score))

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "draw"
    elif computer_score==0:
        return "lose,opponent has a black jack."
    elif user_score==0:
        return "win with a blackjack"
    elif user_score>21:
        return "you lose"
    elif computer_score>21:
        return "opponent went over.you won"
    elif user_score>computer_score:
        return "you won"
    else:
        return 'you lose'


while input('do you want to play game of blackjack.type y or n')=='y':
    clear()
    play()
