#!/usr/bin/python

from random import randint

class Mask():
	size=0
	indexes=[]
	
	def __init__(self, size, numbers_of_elements):
		max_index = numbers_of_elements-1
		self.indexes = [0]*size
		for i in range(size):
			self.indexes[i] = randint(0, max_index)
		self.size=size

	def calculateBestMask(self, event, solution):
		pass

	def generateSolution(self, result, solution):
		pass
