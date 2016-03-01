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

	def transformation(self, index, solution, event):
		y = solution
		if solution is None:
			print "WWWTTTTFFFF"
		for j in range(self.size):
			if index % pow(2,j) == 0:
				print "Oi "+ str(y)
				core = y[self.indexes[j]:self.indexes[j]+5]
				print "core: "+ str(core)
				temp_solution = y[:self.indexes[j]] + y[self.indexes[j]+5:]
				best = None

				print "Vou para o for. Me aguarde"

				for i in range(len(temp_solution)):

					print "Vamos imprimir temp a seguir. Ou nao"

					temp = temp_solution[:i] + core + temp_solution[i:]

					print temp

					if best is None or event.f(temp) < event.f(best):
						best = temp
						print "Entrei no if."
				
				print "TEMP SOLUTION "+ str(temp_solution)

				if best is not None:
					y = best
				
		return y						
				
 
	def calculateBestMask(self, event, solution):
		best = 0
		best_sol = None
		index = -1
		for i in range(self.size):
			print "Farei a transformacao power range"
			sol = self.transformation(i,solution,event)
			print sol
			t = event.f(sol)
			if t < best:
				best_sol = sol
				best = t
				index = i

		result = {"index": index, "solution": best_sol, "distance": best}
		print "Esse e o dicionario"
		print result
		return result

	def generateSolution(self, result, solution):
		pass
