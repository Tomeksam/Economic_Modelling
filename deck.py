import random

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  # Class-level list of possible ranks
    SUITS = ["♤", "♡", "♢", "♧"]  # Class-level list of suits

    def __init__(self, suit, rank):
        """
        Constructor:
        - Checks that suit and rank are valid.
        - Stores values as private attributes.
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank buddy")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._suit = suit
        self._rank = rank

    def __str__(self):
        """
        __str__:
        - Defines how the card appears when printed.
        - Returns rank and suit as a string.
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        __repr__:
        - Defines how the card appears in lists etc.
        - Uses the same format as __str__.
        """
        return self.__str__()

    @property
    def suit(self):
        """
        suit (getter):
        - Returns the suit of the card.
        """
        return self._suit

    @property
    def rank(self):
        """
        rank (getter):
        - Returns the rank of the card.
        """
        return self._rank

class Deck:
    def __init__(self):
        """
        Constructor:
        - Creates a full deck of cards (52 total) using nested loops.
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        __str__:
        - Returns the current deck as a list of cards in string form.
        """
        return str(self._deck)

    def shuffle(self):
        """
        shuffle():
        - Randomly shuffles the deck in-place using random.shuffle.
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        deal():
        - Removes and returns the top card (first item) from the deck.
        """
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()
    print(deck)        # Show full unshuffled deck
    deck.shuffle()     # Shuffle the deck
    print(deck)        # Show shuffled deck
    print(deck.deal()) # Deal (remove + return) the top card
