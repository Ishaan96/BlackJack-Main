from deck import values

class Hand():

	def __init__(self):
		self.hand = []
		self.value = 0

	def add_card(self,card):
		self.hand.append(card)

		if(card.rank == 'Ace'):
			if(self.value+11 > 21):
				self.value += values['Ace'][0]
			else:
				self.value += values['Ace'][1]
		else:
			self.value += values[card.rank]


	def __str__(self):
		return str(self.value)

