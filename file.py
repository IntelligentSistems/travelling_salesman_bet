#!/usr/bin/python
import os

class File():
	fileRef = "Default"
	matrixSize = 0
	graph = []
	def __init__(self, fileName):
		self.fileNameOut = os.path.splitext(fileName)[0] + "Results.txt"
		#self.fileRef = fileName + "Result"
		num = []
		graph = []
		with open(fileName, 'r') as f:
			graphSize = int(f.readline())
			for line in f:
				for s in line.split():
					temp = int(s)
					if temp == 9999:
						temp = -1
					num.append(temp)
					if len(num) == graphSize:
						graph.append(num)
						num = []			
				
		self.graph = graph

	def PrintOut(self, result, iteration):
		fileOut = open(self.fileNameOut, 'a')
		fileOut.write("Resultado do teste " + str(iteration) + " = " + str(result))
		fileOut.write("\n")