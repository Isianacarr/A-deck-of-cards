# This is a program to represent a Card as a Class

"""A simple playing card. A card is characterized by two componets:
    Rank: an interger value in the range 1-13, inclusive (Ace-King)
    Suit: A character in 'cdhs' for clubs, diamonds, hearts, and spades"""


class Card(object):
    SUITS = 'cdhs'
    SUIT_NAMES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    RANKS = range(1, 14)
    RANK_NAMES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                  'Seven', 'Eight', 'Nine', 'Ten',
                  'Jack', 'Queen', 'King']

    def __init__(self, rank, suit):
        """Constructor
        pre: rank in range(1,14) and suit in 'cdhs'
        post: self has the given rank and suit"""

        self.rank_num = rank
        self.suit_char = suit

    def suit(self):
        """Card Suit
        post: returns the suit of self as a single character"""

        return self.suit_char

    def rank(self):
        """Card Rank
        post: returns the rank of self as a int"""

        return self.rank_num

    def suit_name(self):
        """Card Suit Name
        post: returns one of ('Clubs', 'Diamonds', 'Hearts', 'Spades')
        corresponding to the self's suit"""

        index = self.SUITS.index(self.suit_char)
        return self.SUIT_NAMES[index]

    def rank_name(self):
        """Card Rank Name
        post: returns one of ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                  'Seven', 'Eight', 'Nine'..... 'King')
        corresponding to the self's rank"""

        index = self.RANKS.index(self.rank_num)
        return self.RANK_NAMES[index]

    def __str__(self):
        """String Representation
        post: Returns string representating self, e.g. 'Ace of Spades' """

        return self.rank_name() + ' of ' + self.suit_name()


    """We need a way to compare the cards if we are to use them in practical
    applications. Here is a set of operator overloaded functions that allows 
    us to compare cards using python operators such as <,>,== and so on. """
    def __eq__(self, other):

        return (self.suit_char == other.suit_char and
                self.rank_num == other.rank_num)

    def __lt__(self,other):

        if self.suit_char == other.suit_char:
            return self.rank_num < other.rank_num
        else:
            return self.suit_char < other.suit_char

    def __ne__(self, other):

        return not(self == other)

    def __le__(self, other):

        return self < other or self == other