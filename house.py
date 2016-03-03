#!/usr/bin/python


class House():
	bet_min=1
	bet_max=200
	bankroll=10000.0
	weights=[]
	
	def __init__(self, bet_min=1, bet_max=200, bankroll=10000.0):
		self.bet_min = bet_min
		self.bet_max = bet_max
	
	
	def calculateWeights(self, players):
		size = len(players[0].weights)
		self.weights = [ 0 for x in range(size) ]
		
		big_weight=0
		for i in range(size):
			w=0
			for player in players:
				big_weight += player.weights[i]
				w += player.weights[i]
			self.weights[i] = w

		for i in range(size):
			self.weights[i] /= big_weight
	
	def receiveBet(self, bet):
		self.bankroll += bet
