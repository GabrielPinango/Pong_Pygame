import pygame
from pygame.locals import *

def cargar_img(nombre):
	try:
		img = pygame.image.load(nombre)
	except:
		print 'no se puede cargar la imagen' +str(nombre)
	return img

class pelota(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) #Inicializar metodo sprite de pygame
		self.image = cargar_img('ball.png')
		self.rect = self.image.get_rect()
		self.rect.center = (300, 200) #Posicion donde aparecera la pelota
		self.velocidad = [5, 6]
	
	def update(self):
		self.rect.move_ip((self.velocidad[0], self.velocidad[1])) #La pelota adquirira movimiento
		self.control()
	
	def control(self): #Metodo para controlar que la pelota no salga de la pantalla
		#Eje X
		if self.rect.left <=0 or self.rect.right >=640:
			self.velocidad[0] = -self.velocidad[0]
		#Eje Y
		if self.rect.top <=0 or self.rect.bottom >=480:
			self.velocidad[1] = -self.velocidad[1]