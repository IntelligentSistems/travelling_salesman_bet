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

mask=None

if len(sys.argv) == 3 and sys.argv[2] in masks:
	mask = masks[sys.argv[2]]
else:
	mask = MaskMoveCore


filename = sys.argv[1]
g = Game(filename, mask=mask)
for i in range(10):
	result = g.play()
	fileOut = File(filename).PrintOut(g.event.f(g.solution),i)


