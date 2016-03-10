#!/usr/bin/python

from random import randint

class Mask():
	size=0
	indexes=[]
	
	def __init__(self, size, numbers_of_elements):
		max_index = numbers_of_elements-1
		self.indexes = [0]*size
		for i in range(size):
			vertex = randint(0, max_index)
			while vertex in self.indexes:
				vertex = randint(0, max_index)
			self.indexes[i] = vertex
			
		self.size=size

	def transformation(self, index, solution, event):
		pass
 
	def calculateBestMask(self, event, solution):
		best = None
		best_sol = None
		index = -1
		for i in range(self.size):
			#print "Farei a transformacao power range"
			sol = self.transformation(i,solution,event)
			#print sol
			t = event.f(sol)
			if best is None or t < best:
				best_sol = sol
				best = t
				index = i

		result = {"index": index, "solution": best_sol, "distance": best}
		#print "Esse e o dicionario"
		#print result
		return result

	def calculateWeight(self, index, probabilities):
		j = index
		weight = 1
		for i in range(self.size):
			x = self.size - 1 - i
			p = probabilities[self.indexes[x]]
			if j % 2 == 1:
				weight *= p
			else:
				weight *= (1 - p)
			j /= 2

		return weight
