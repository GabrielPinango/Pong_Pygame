import pygame
from pygame.locals import *
from ball import pelota

def cargar_img(nombre):
	try:
		img = pygame.image.load(nombre)
	except:
		print 'no se puede cargar la imagen' +str(nombre)
	return img

class raqueta_dos(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = cargar_img('raqueta2.png')
		self.rect = self.image.get_rect()
		self.rect.center = (620, 240)
	
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[K_DOWN]:
			self.rect.y += 6
		if keys[K_UP]  :
			self.rect.y -= 6
		self.control()
	
	def control(self):
		if self.rect.top <=0:
			self.rect.top = 0
		if self.rect.bottom >=480:
			self.rect.bottom = 480