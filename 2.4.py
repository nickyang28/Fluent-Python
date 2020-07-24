# -*- coding:utf-8 -*-
import collections

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
    deck = FrenchDeck()
    print(deck[4::13])
    As = slice(4, 52, 13)
    print(deck[As])
