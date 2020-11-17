from deck import Deck
from hand import Hand
from deck import suits,ranks,values

playing = True

def hit_or_stand(hand):
	global playing
	while True: 
		str = input("Would you like to HIT or STAND? Press H to Hit, S to Stand\n")
		if str[0].lower() == 'h':
			hand.add_card(x.deal())
		elif str[0].lower() == 's':
			playing = False
		else:
			print("Sorry! Please enter again.")
			continue
		break

def ask_bet(total):
	b = int(input('Enter bet amount:'))
	while(b>total):
		b = int(input('Enter bet amount:'))

	return b

def show_some(player,dealer):
	print("Dealer's Hand:")
	print(" <card hidden>")
	print('',dealer.hand[1])
	print("\n\nPlayer's Hand: ",*player.hand,sep = "\n")

def show_all(player,dealer):
	print("Dealer's Hand: ",*dealer.hand,sep = "\n")
	print("\n\nPlayer's Hand: ",*player.hand,sep = "\n")

while True:
	x = Deck()
	x.shuffle()
	player_hand = Hand()
	dealer_hand = Hand()
	player_hand.add_card(x.deal())
	player_hand.add_card(x.deal())
	dealer_hand.add_card(x.deal())
	dealer_hand.add_card(x.deal())
	show_some(player_hand,dealer_hand)
	hit_or_stand(player_hand)

	while playing:
		show_some(player_hand,dealer_hand)
		if player_hand.value <21:
			hit_or_stand(player_hand)
		else:
			playing = False

	while dealer_hand.value <=17:
		dealer_hand.add_card(x.deal())
	print("\n")
	show_all(player_hand,dealer_hand)	
	if dealer_hand.value > 21:
		print("Dealer busts. Player wins")
	elif player_hand.value > 21:
		print("Player busts. Dealer wins")
	elif (player_hand.value<=21 and player_hand.value>dealer_hand.value):
		print("Player wins.")
	elif (dealer_hand.value<=21 and dealer_hand.value>player_hand.value):
		print("Dealer wins")
	else:
		print("The game is a tie")

	p = input("Would you like to play again? Press Y for yes, N for no  ")
	if p[0].lower() == 'y':
		del player_hand,dealer_hand,x
		continue
	elif p[0].lower() == 'n':
		print("Thanks for playing Blackjack")
		break
	else:
		break
