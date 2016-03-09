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
		self.core = numbers_of_elements - size

	def transformation(self, index, solution, event):
		y = solution
		k = index
		for x in range(self.size):
			j = self.size - 1 - x
			if k % 2 == 0:
			
				core = y[self.indexes[j]:self.indexes[j]+self.core+1]
				temp_solution = y[:self.indexes[j]] + y[self.indexes[j]+self.core+1:]
				best = None

				for i in range(len(temp_solution)):
				
					temp = temp_solution[:i] + core + temp_solution[i:]
					val = event.f(temp)
					if val is None:
						continue

					if best is None or val < event.f(best):
						best = temp

				if best is not None:
					y = best
			k /= 2
		return y						
				
 
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

	def generateSolution(self, result, solution):
		pass
