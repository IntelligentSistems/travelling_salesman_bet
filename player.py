#!/usr/bin/python

from random import random

from names import randomName

class Player():
	name="Default"
	probabilities=[]
	bets=[]
	bankroll=1000.0
	
	def __init__(self, size, bankroll=100.0):
		if size<1:
			print "Erro to instatiate Player"
			return
	  
		self.bankroll = bankroll
		self.name=randomName()
		self.probabilities = [0] * size
		self.bets = [0] * size
		for i in range(size):
			self.probabilities[i] = random()

	
	def calculateWeights(self, mask):
		pass
	
	def makeBets(self, house):
		pass
	
	def isWinner(self, result):
		pass
	
	def isBroke(self, result):
		pass
	
	def receiveAward(self, house, result):
		pass
	
	def createNew(self):
		pass
