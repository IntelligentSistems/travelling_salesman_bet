#!/usr/bin/python

from random import randint
from mask import Mask

class MaskChangeIndex(Mask):


	def fixConflit(self, index, replace_value, vector):
		value = vector[index]
		for i in range(len(vector)):
			if i != index and vector[i] == value:
				vector[i] = replace_value

	def transformation(self, index, solution, event):
		y = []
		y.extend(solution)
		k = index
		for x in range(self.size):
			j = self.size - 1 - x
			if k % 2 == 1:
				vertex = randint(0, self.max_index)
				replace_value = y[self.indexes[j]]
				y[self.indexes[j]] = vertex
				self.fixConflit(self.indexes[j], replace_value, y)
			k /= 2
		return y
