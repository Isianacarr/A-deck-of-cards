#Hand.py

class Hand(object):
    """A labled collection of cards that can be sorted"""

    def __init__(self, label=""):
        """Create an empty collection within a given label."""

        self.label = label
        self.cards = []


    def add(self, card):
        """Add Card to the hand"""

        self.cards.append(card)

    def sort(self):
        """Arrange the cards in descending bridge order"""

        cards0 = self.cards
        cards1 = []

        """ while cards0 != []:
            next_card = max(cards0)
            cards0.remove(next_card)
            cards1.append(next_card)
        self.cards = cards1"""

        for i, card in enumerate(self.cards):
            index = self.cards.index(max(self.cards))
            self.cards[i] = self.cards[index]
            self.cards[index] = card


    def dump(self):
        """Print out the contents of the hand"""

        print(self.label + "'s cards:")
        for c in self.cards:
            print(" ", c)

