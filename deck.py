from blackjack_mainscript import suits,ranks,values
from card import Card
import random

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))

    def __str__(self):
        for card in self.deck:
            x = card
        return x.rank +' of '+ x.suit

    def shuffle(self):
        random.shuffle(self.deck)
     

    def deal(self):
        return self.deck.pop()



x = Deck()

