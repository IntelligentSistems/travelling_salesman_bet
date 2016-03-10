#!/usr/bin/python

from house import House
from player import Player
from event import Event
from mask_movecore import MaskMoveCore

class Game():
	turns=5
	event=None
	house=None
	players=[]
	solution=[]
	fileName = None
	
	def __init__(self, filename=None, size_of_player=20, turns=10000000, players_number=20, mask_size=3, convergence=1000, mask=MaskMoveCore):
		self.convergence = convergence
		self.mask_size = mask_size
		self.mask = mask
		self.turns = turns
		self.house = House()
		if filename is not None:
			self.event = Event(filename=filename)
		else:
			self.event = Event(size=size_of_player)

		self.size_of_player = len(self.event)
		
		for index in range(players_number):
			player = Player(self.size_of_player)
			self.players.append(player)
	
	def generateMask(self):
		return self.mask(self.mask_size, self.size_of_player)
	
	def play(self):
		self.solution = self.event.getInitialSolution()
		convergence = 0
		#print "graph: "
		#print self.event
		print "iteration: -1; f(solution) = "+str(self.event.f(self.solution))
		for turn in range(self.turns):
			mask = self.generateMask()
			
			for player in self.players:
				player.calculateWeights(mask)
			
			self.house.calculateWeights(self.players)
			#print "Weights of house: "+ str(self.house.weights)
			
			for player in self.players:
				player.makeBets(self.house)
				#print "The player "+ player.name +" has "+ str(player.bankroll) +" and makes bets." + str(player.bets)
			
			result = mask.calculateBestMask(self.event, self.solution)
			#print "The result was "+ str(result["index"])
			
			for index in range(len(self.players)):
				player = self.players[index]
				if player.isWinner(result["index"]):
					player.receiveAward(self.house, result["index"])
					#print "The player "+ player.name +" receives award."
				if player.isBroken():
					#print "The player "+ player.name +" is out."
					self.players[index] = player.createNew()
					#print "The new player "+ self.players[index].name +" is in."
				#print "The player "+ player.name +" has "+ str(player.bankroll)
			
			#print "The house has "+ str(self.house.bankroll)
			if result["distance"] < self.event.f(self.solution):
				convergence = 0
				self.solution = result["solution"]
				#print "iteration: "+str(turn)+"; f(solution) = "+str(self.event.f(self.solution))
			else:
				convergence += 1
			
			
			if convergence >= self.convergence:
				break
		
		
		return self.solution
