from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):
        """
        Initialises a PokerHand by dealing 5 cards from a given deck.
        :param deck: an instance of the Deck class (must already be shuffled)
        """
        self._cards = [deck.deal() for _ in range(5)]  # Draw 5 cards from the deck

    @property
    def cards(self):
        """
        Getter: Returns the list of 5 Card objects in the hand.
        """
        return self._cards

    def __str__(self):
        """
        Returns a string representation of the hand.
        (Note: should be '__str__' to override the built-in print() display).
        """
        return str(self._cards)

    @property
    def is_flush(self):
        """
        Checks if the hand is a flush.
        A flush = all 5 cards have the same suit.
        :return: True if all cards have the same suit, otherwise False.
        """
        first_suit = self.cards[0].suit  # Get the suit of the first card
        return all(card.suit == first_suit for card in self.cards)  # Check all cards


# Simulation to estimate the probability of getting a flush
count = 0     # Total number of hands checked
flushes = 0   # Number of flushes found

while flushes < 100:  # Run until 100 flush hands are found
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_flush:
        flushes += 1  # Increment when a flush is found
    count += 1  # Increment every hand, flush or not

print(f"Probability of a flush is {100 * flushes / count:.2f}%")
