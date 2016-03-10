#!/usr/bin/python

from game import Game
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

g = Game(filename=sys.argv[1], mask=mask)
g.play()


