from deck import x

class Hand():

	def __init__(self):
		self.hand = []
		self.value = 0

	def add_card(self):
		self.hand.append(x.deal())
		self.value += values[x.rank]


	def __str__(self):
		return 'Testing Hand class'

x.shuffle()
print(x)