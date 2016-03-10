#!/usr/bin/python

from game import Game
from event import Event
from file import File

import sys

from mask_movecore import MaskMoveCore
from mask_changeindex import MaskChangeIndex
masks = {
	"movecore": MaskMoveCore,
	"changeindex" : MaskChangeIndex
}

###Formato da entrada:python main.py <matriz> <mascara> <melhor valor Demasi> <quantidade de testes>

mask=None

if len(sys.argv) == 3 and sys.argv[2] in masks:
	mask = masks[sys.argv[2]]
else:
	mask = MaskMoveCore


filename = sys.argv[1]
numTests = sys.argv[4]
bestResultsCount = 0


g = Game(filename, mask=mask)
fileOut = File(filename)
#Vou rodar uma quantidade de testes passada pelo terminal e soh printar no arquivo aquelas que forem menores do que o menor resultado do Demasi
#Tambem vou guardar a informacao de quao menor eh a solucao
for i in numTests:
	result = g.play()
	if g.event.f(g.solution) < sys.argv[3]:
		fileOut.PrintOut(g.event.f(g.solution), int(sys.argv[3])-g.event.f(g.solution), None)
		bestResultsCount+=1
fileOut.PrintOut(bestResultsCount, 0, str(mask))