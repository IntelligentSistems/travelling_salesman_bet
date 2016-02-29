#!/usr/bin/python

from names import randomName

class Player():
	name="Default"
	probabilities=[]
	
	def __init__(self):
		self.name=randomName()
