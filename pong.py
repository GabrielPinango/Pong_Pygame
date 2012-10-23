background_image_filename = 'table.ashx'

import pygame
from pygame.locals import *
from sys import exit
from bat import raqueta_uno
from bat2 import raqueta_dos
from ball import pelota
from score import score

player = { "Player 1":score("Player 1"), "Player 2":score("Player 2")}

ancho, alto = 640, 480

pygame.init()

screen = pygame.display.set_mode((ancho, alto), 0, 32)
background = pygame.image.load(background_image_filename).convert()
raquetas = pygame.sprite.RenderClear()

raqueta1 = raqueta_uno()
raqueta2 = raqueta_dos()
raquetas.add(raqueta1)
raquetas.add(raqueta2)

pelota = pelota()

first_player = player['Player 1']
second_player = player['Player 2']

clock = pygame.time.Clock() #Crear el objeto Clock

def colicion(sprite, grupo):
	for COLICION in pygame.sprite.spritecollide(sprite, grupo, 0):
		pelota.velocidad[0] = -pelota.velocidad[0]
		
def score(first_player, second_player):
	if pelota.rect.left <=0:
		second_player.score_player += 1
		for player_name in sorted(player.keys()):
			print player[player_name]
	if pelota.rect.right >=640:
		first_player.score_player += 1
		for player_name in sorted(player.keys()):
			print player[player_name]

while True:
	clock.tick(60) #Para hacer que corra a 60 frames per second (FPS)
		
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		
	colicion(pelota, raquetas)
	score(first_player, second_player)
	
	pelota.update()	
	raqueta2.update()
	raqueta1.update()
	raquetas.update()
	screen.fill((0, 0, 0))
	raquetas.draw(screen)
	screen.blit(background, (0, 0))	
	screen.blit(pelota.image, pelota.rect)
	screen.blit(raqueta1.image, raqueta1.rect)
	screen.blit(raqueta2.image, raqueta2.rect)	
	pygame.display.update()