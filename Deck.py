"This is a Deck class"

from random import randrange
from Card import Card


class Deck(object):

    def __init__(self):
        """post: Create a 52-card deck in standard order"""
        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank,suit))

        self.cards = cards

    def shuffle(self):
        """Shuffle the deck
        post: randomizes the order of the cards in self"""

        n = self.size()
        cards = self.cards
        for i,card in enumerate(cards):
            pos = randrange(i, n)
            cards[i] = cards[pos]
            cards[pos] = card

        self.cards = cards

    def deal(self):
        """Deal a single card
        post: self.size() > 0
        post: returns the next card in self, and removes it from self."""

        return self.cards.pop()

    def size(self):
        """Cards left
        post: Returns the number of cards in self"""

        return len(self.cards)

