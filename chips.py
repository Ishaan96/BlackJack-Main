class Chips():

	def __init__(self,total=100):
		self.total_chips = total

	def win_bet(self,bet):
		self.total += bet 
	
	def lose_bet(self,bet):
		self.total -= bet