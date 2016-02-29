#!/usr/bin/python

from random import random

from names import randomName

class Player():
    name="Default"
    probabilities=[]
    bets=[]
    bankroll=100.0
    
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

    def calculateWeight(self, pick):
	    weight = 1.0/self.probabilities[pick]
	    return weight
    
    def calculateWeights(self):
        weights = [0] * len(self.probabilities)
        for i in range(len(weights)):
            weights[i] = self.calculateWeight(i)
        return weights
    
    def makeBet(self, bet_min, pick, weight):
        bet = 0
        p = self.probabilities[pick]
        w = 1/p
        
        if weight > w:
            bet = ((p*weight - 1)/(weight - 1)) * self.bankroll
            if bet_min > bet:
                bet = bet_min
            if self.bankroll < bet:
                bet = self.banckroll
        
        self.bets[pick] = bet
        self.bankroll -= bet
        return bet
