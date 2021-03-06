from card import Card
import random

suits = ('Hearts','Diamonds','Clubs','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':[1,11]}


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


        