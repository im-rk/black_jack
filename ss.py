import random

user_cards=[]
computer_cards=[]
def dealcards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def play():
    user_cards=[]
    computer_cards=[]

    for i in range(2):
        user_cards.append(dealcards())
        computer_cards.append(dealcards())
    def calculatescore(cards):
        if sum(cards)==21 and len(cards)>2:
            return 0
        if sum(cards)==21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    is_game_over=False
    while not is_game_over:
        user_score=calculatescore(user_cards)
        computer_score=calculatescore(computer_cards)

        print(f"your cards:{user_cards}, user score:{user_score}")
        print(f"computer cards:{computer_cards}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            userin=input('do you want draw more cards,type y or n:')
            if userin==y:
                user_cards.append(dealcards())
            else:
                is_game_over=True

        while computer_score!=0 and computer_score<17:
            computer_cards.append(dealcards())
            computer_score=calculatescore(computer_cards)
