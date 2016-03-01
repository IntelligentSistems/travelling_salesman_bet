#!/usr/bin/python

from random import random
from names import randomName

class Player():
	name="Default"
	probabilities=[]
	bets=[]
	bankroll=1000.0
	weights=[]
	
	def __init__(self, size, bankroll=100.0):
		if size<1:
			print "Erro to instatiate Player"
			return
	  
		self.bankroll = bankroll
		self.name=randomName()
		self.probabilities = [0] * size
		for i in range(size):
			self.probabilities[i] = random()

	
	def calculateWeight(self, index, mask):
		j = index
		weight = 1
		for i in range(mask.size):
			x = mask.size - 1 - i
			p = self.probabilities[mask.indexes[x]]
			if j % 2 == 1:
				weight *= p
			else:
				weight *= (1 - p)
			j /= 2

		return weight

	def calculateWeights(self, mask):
		number_of_weights = pow(2,mask.size)
		
		for i in range(number_of_weights):
			w = self.calculateWeight(i, mask)
			self.weights.append(w)
	
	def makeBets(self, house):
		for i in range(len(self.weights)):
			bet=0
			if house.weights[i] > self.weights[i]:
				p = 1.0/self.weights[i]
				bet = ((p*house.weights[i] - 1)/(house.weights[i] - 1))*self.bankroll
				bet = min(self.bankroll, max(bet, house.bet_min))
			
			self.bankroll -= bet
			self.bets.append(bet)
			house.receiveBet(bet)
	
	def isWinner(self, result):
		return self.bets[result] > 0
	
	def isBroken(self):
		return self.bankroll == 0
	
	def receiveAward(self, house, result):
		self.bankroll += house.weights[result]*self.bets[result]
	
	def createNew(self):
		return Player(len(self.probabilities))

