import random

defalut_deck = list(range(60))

current_deck = defalut_deck.copy()

def reset_deck():
    """Reverts the deck back to it's original state
    """
    global current_deck
    current_deck = defalut_deck.copy()

def shuffle_deck():
    """Randomized the order of the deck
    """
    random.shuffle(current_deck)

def draw_cards(number_cards: int) -> tuple:
    """Draws a number of cards from the top of the deck,
    while removing them from the deck.

    :param number_cards: Number of cards to get from the deck
    :type number_cards: int
    :return: Cards from the deck
    :rtype: tuple
    """
    drawn_cards = []
    for _ in range(number_cards):
        if current_deck:
            drawn_cards.append(current_deck.pop(0))
    return tuple(drawn_cards)

def draw_specific_card(card: str):
    """Takes a specified card out of the deck if it's in the deck

    :param card: Name of the card to get
    :type card: str
    :return: A card from the deck
    """
    if card in current_deck:
        card_index = current_deck.index(card)
        return current_deck.pop(card_index)
    
def look_at_cards(number_cards: int, bottom: bool=False) -> tuple:
    """Gets a list of cards from top to bottom or bottom to top of the deck,
    without removing them from the deck.

    :param number_cards: Number of cards to look at
    :type number_cards: int
    :param bottom: True=Look at from bottom to top, False=top to bottom
    :type bottom: bool
    :return: A number of cards in order from the designated side of the deck
    :rtype: tuple
    """
    direction = -1 if bottom else 1
    seen_cards = current_deck[::direction][:number_cards]
    return tuple(seen_cards)
    
print(current_deck)
shuffle_deck()
print(current_deck)
print(draw_cards(7))
print(current_deck)
choice = random.choice(current_deck)
print(choice)
print(draw_specific_card(choice))
print(current_deck)

reset_deck()
print(current_deck)