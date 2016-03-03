#!/usr/bin/python

from house import House
from player import Player
from event import Event
from mask import Mask

class Game():
	turns=5
	event=None
	house=None
	players=[]
	solution=[]
	
	def __init__(self, size_of_player=4, turns=5, players_number=20, mask_size=3):
		self.mask_size = mask_size
		self.size_of_player = size_of_player
		self.turns = turns
		self.house = House()
		self.event = Event(size=size_of_player)
		
		for index in range(players_number):
			player = Player(size_of_player)
			self.players.append(player)
	
	def generateMask(self):
		return Mask(self.mask_size, self.size_of_player)
	
	def play(self):
		self.solution = self.event.getInitialSolution()
		for turn in range(self.turns):
			mask = self.generateMask()
			
			for player in self.players:
				player.calculateWeights(mask)
			
			self.house.calculateWeights(self.players)
			print "Weights of house: "+ str(self.house.weights)
			
			for player in self.players:
				player.makeBets(self.house)
				print "The player "+ player.name +" has "+ str(player.bankroll) +" and makes bets." + str(player.bets)
			
			result = mask.calculateBestMask(self.event, self.solution)
			print "The result was "+ str(result["index"])
			
			for index in range(len(self.players)):
				player = self.players[index]
				if player.isWinner(result["index"]):
					player.receiveAward(self.house, result["index"])
					print "The player "+ player.name +" receives award."
				if player.isBroken():
					print "The player "+ player.name +" is out."
					self.players[index] = player.createNew()
					print "The new player "+ self.players[index].name +" is in."
			
			print "The house has "+ str(self.house.bankroll)
			if result["distance"] < self.event.f(self.solution):
				self.solution = result["solution"]

		return self.solution
