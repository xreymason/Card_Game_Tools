import random

defalut_deck = list(range(60))

current_deck = defalut_deck.copy()

def shuffle_deck():
    random.shuffle(current_deck)

def draw_cards(number_cards: int) -> tuple:
    drawn_cards = []
    for _ in range(number_cards):
        if current_deck:
            drawn_cards.append(current_deck.pop(0))
    return tuple(drawn_cards)
    
print(current_deck)
shuffle_deck()
print(current_deck)
print(draw_cards(7))