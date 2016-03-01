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
		pass
	
