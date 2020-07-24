# coding: utf-8
import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        super(FrenchDeck, self).__init__()
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __repr__(self):
        return '[{}]'.format(', '.join([_card.__repr__() for _card in self._cards]))

    def __setitem__(self, key, value):
        self._cards[key] = value


if __name__ == "__main__":
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    print(deck[0])
    print(deck)
    print(choice(deck))

    suit_values = {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}

    def spades_high(_card):
        rank_value = FrenchDeck.ranks.index(_card.rank)
        return rank_value * len(suit_values) + suit_values[_card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)

    deck[0] = Card(rank='3', suit='clubs')
    print(deck[0])
