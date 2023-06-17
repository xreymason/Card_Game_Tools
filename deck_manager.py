import random


class DeckManager:
    def __init__(self) -> None:
        self.defalut_deck = []
        self.current_deck = []

    def reset_deck(self):
        """Reverts the deck back to it's original state
        """
        self.current_deck = self.defalut_deck.copy()

    def shuffle_deck(self):
        """Randomized the order of the deck
        """
        random.shuffle(self.current_deck)

    def draw_cards(self, number_cards: int) -> tuple:
        """Draws a number of cards from the top of the deck,
        while removing them from the deck.

        :param number_cards: Number of cards to get from the deck
        :type number_cards: int
        :return: Cards from the deck
        :rtype: tuple
        """
        drawn_cards = []
        for _ in range(number_cards):
            if self.current_deck:
                drawn_cards.append(self.current_deck.pop(0))
        return tuple(drawn_cards)

    def draw_specific_card(self, card: str):
        """Takes a specified card out of the deck if it's in the deck

        :param card: Name of the card to get
        :type card: str
        :return: A card from the deck
        """
        if card in self.current_deck:
            card_index = self.current_deck.index(card)
            return self.current_deck.pop(card_index)
        
    def look_at_cards(self, number_cards: int, bottom: bool=False) -> tuple:
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
        seen_cards = self.current_deck[::direction][:number_cards]
        return tuple(seen_cards)
    
if __name__ == "__main__":
    dm = DeckManager()
    dm.defalut_deck = list(range(60))
    dm.reset_deck()
    print(dm.current_deck)
    dm.shuffle_deck()
    print(dm.current_deck)
    print(dm.draw_cards(7))
    print(dm.current_deck)
    choice = random.choice(dm.current_deck)
    print(choice)
    print(dm.draw_specific_card(choice))
    print(dm.current_deck)

    dm.reset_deck()
    print(dm.current_deck)