#!/usr/bin/python

from mask import Mask

class MaskMoveCore(Mask):
	core=None

	def __init__(self, size, numbers_of_elements):
		Mask.__init__(self, size, numbers_of_elements)
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
