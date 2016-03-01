#!/usr/bin/python

from random import randint

class Mask():
	indexes=[]
	
	def __init__(self, size, max_index):
		self.indexes = [0]*size
		for i in range(size):
			self.indexes[i] = randint(0, max_index)

	def calculateBestMask(self, event, solution):
		pass

	def generateSolution(self, result, solution):
		pass
