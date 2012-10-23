import pygame
from pygame.locals import *
from ball import pelota

class score(object):
	def __init__(self, name):
		self.name = name		
		self.score_player = 0
	
	def __str__(self):
		return "%s - %i points" % (self.name, self.score_player)