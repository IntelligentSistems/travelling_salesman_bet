#!/usr/bin/python

class File():
	fileRef = "Default"
	matrixSize = 0
	graph = []
	def __init__(self, fileName):
		num = []
		graph = []
		with open(fileName, 'r') as f:
			graphSize = f.readline()
			for line in f:
				for s in line.split():
					num.append(int(s))			
				print str(num)
				graph.append(num)
				num = []
		self.graph = graph



