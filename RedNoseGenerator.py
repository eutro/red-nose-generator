# Author: Benedek Szilvasy
# Created: March 2015
# Version: 1.1
#
# Benedek Szilvasy Copyright (c) 2015. All rights reserved.

import random, pygame, sys
from pygame.locals import *
from time import sleep

(width, height) = (640, 640)
window = pygame.display.set_mode((width, height))
pygame.init()
pygame.display.set_caption('Red Nose Generator')
window.fill((255, 255, 255))

######################################################################OPTIONS########################################################################
global plainBg
plainBg = True

def mainMenu():
	window.blit(title.render(('''Red Nose Generator.'''),True,(0, 0, 0)),(175, 75))
	window.blit(pygame.font.SysFont("arial black", 20).render(('''Version 1.1'''),True,(0, 0, 0)),(175, 110))
	if mousePos[0] > 197 and mousePos[0] < 459 and mousePos[1] > 180 and mousePos[1] < 220:
		window.blit(buttonFont.render(('''   Generate Nose!   '''),True,(0, 0, 0),(63, 0, 127)),(200, 180))
		if mouseUp:
			return 'Go'
	else:
		window.blit(buttonFont.render(('''   Generate Nose!   '''),True,(0, 0, 0),(127, 0, 255)),(200, 180))
	pygame.draw.rect(window, (0, 0, 0), (197, 180, 265, 38), 5)
	if plainBg:
		if mousePos[0] > 147 and mousePos[0] < 525 and mousePos[1] > 255 and mousePos[1] < 295:
			window.blit(buttonFont.render(('''    Plain Background (On)    '''),True,(0, 0, 0),(63, 0, 127)),(150, 255))
			if mouseUp:
				global plainBg
				plainBg = False
		else:
			window.blit(buttonFont.render(('''    Plain Background (On)    '''),True,(0, 0, 0),(127, 0, 255)),(150, 255))
		pygame.draw.rect(window, (0, 0, 0), (147, 255, 374, 38), 5)
	else:
		if mousePos[0] > 147 and mousePos[0] < 525 and mousePos[1] > 255 and mousePos[1] < 295:
			window.blit(buttonFont.render(('''    Plain Background (Off)    '''),True,(0, 0, 0),(63, 0, 127)),(150, 255))
			if mouseUp:
				global plainBg
				plainBg = True
		else:
			window.blit(buttonFont.render(('''    Plain Background (Off)    '''),True,(0, 0, 0),(127, 0, 255)),(150, 255))
		pygame.draw.rect(window, (0, 0, 0), (147, 255, 376, 38), 5)
	if mousePos[0] > 198 and mousePos[0] < 458 and mousePos[1] > 330 and mousePos[1] < 370:
		window.blit(buttonFont.render(('''                Credits                 '''),True,(0, 0, 0),(63, 0, 127)),(150, 330))
		if mouseUp:
			return 'Credits'
	else:
		window.blit(buttonFont.render(('''                Credits                 '''),True,(0, 0, 0),(127, 0, 255)),(150, 330))
	pygame.draw.rect(window, (0, 0, 0), (150, 330, 360, 38), 5)
	return 'Menu'

def creds():
	window.blit(title.render(('''       Credits        '''),True,(0, 0, 0)),(175, 75))
	window.blit(smallerType.render(('''       Coding        '''),True,(0, 0, 0)),(175, 130))
	window.blit(smallerType.render(('''Benedek & Medard Szilvasy'''),False,(0, 0, 0)), (175, 180))
	window.blit(smallerType.render(('''       Graphics        '''),True,(0, 0, 0)),(175, 230))
	window.blit(smallerType.render(('''Benedek Szilvasy'''),False,(0, 0, 0)), (175, 280))
	window.blit(smallerType.render(('''Russell Trow'''),False,(0, 0, 0)), (175, 330))
	if mousePos[0] > 0 and mousePos[0] < 64 and mousePos[1] > 600 and mousePos[1] < 640:
		window.blit(smallerType.render(('''Back'''),True,(0, 0, 0),((205, 0, 0))),(0, 610))
		if mouseUp:
			return 'Menu'
	else:
		window.blit(smallerType.render(('''Back'''),True,(0, 0, 0),((255, 0, 0))),(0, 610))
	return 'Credits'

def genNose(bg, graphx, image='None'):
	if bg:
		window.fill((255, 255, 255))
	if image != 'None':
		window.blit(graphx[image[0]], (160, 160))
		if graphx[image[0]] == graphx[4]:
			if toLoad[image[1]][0] != 'D':
				image[1] += 4
			window.blit(graphx[image[1]], (250, 150))
			window.blit(graphx[image[2]], (273, 260))
		else:
			window.blit(graphx[image[1]], (250, 170))
			window.blit(graphx[image[2]], (273, 330))

	else:
		image = createNose()
	if mousePos[0] > 0 and mousePos[0] < 64 and mousePos[1] > 600 and mousePos[1] < 640:
		window.blit(smallerType.render(('''Back'''),True,(0, 0, 0),((205, 0, 0))),(0, 610))
		if mouseUp:
			return ('Menu', image)
	else:
		window.blit(smallerType.render(('''Back'''),True,(0, 0, 0),((255, 0, 0))),(0, 610))
	if mousePos[0] > 595 and mousePos[0] < 640 and mousePos[1] > 600 and mousePos[1] < 640:
		window.blit(smallerType.render(('''Go!'''),True,(0, 0, 0),((205, 0, 0))),(595, 610))
		if mouseUp:
			return ('Go', 'Nuffink')
	else:
		window.blit(smallerType.render(('''Go!'''),True,(0, 0, 0),((255, 0, 0))),(595, 610))
	return ('Generate', image)

def createNose():
	return [random.choice((1, 2, 3, 4)), random.choice((5, 6, 7, 8, 9, 10, 11, 12)), random.choice((13, 14, 15, 16, 17))]

mouseUp = False
toLoad = ['Background', 'MummyNose', 'NingaNose', 'CavemanNose', 'RoboNose', 'SemiBrownEye', 'SemiBlueEye', 'BrownEye', 'BlueEye', 'DBLSemiBrownEye', 'DBLSemiBlueEye', 'DBLBrownEye', 'DBLBlueEye', 'GrinMouth', 'ToothyMouth', 'BlushMouth', 'TongueMouth', 'SmileMouth']
loaded = False
page = 'Menu'
amountLoaded = 0
title = pygame.font.SysFont("arial black", 30)
buttonFont = pygame.font.SysFont("arial", 30)
smallerType = pygame.font.SysFont("arial", 25)
loadingPercent = 0
txt = title.render(('''Loading. Please wait.'''),True,(0, 0, 0))
graphics = []

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.MOUSEBUTTONUP:
			mouseUp = True
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit()

	mousePos = pygame.mouse.get_pos()
	# We don't want to max out the CPU so put in a sleep()
	sleep(0.1)

	if not loaded:
		window.fill((255, 255, 255))
		window.blit(txt,(175, 250))
		try:
			graphics.append(pygame.image.load(('images/' + toLoad[amountLoaded]) + '.png'))
		except IndexError:
			loadingPercent = 100.0
		amountLoaded += 1
		if not loadingPercent == 100:
			loadingPercent = (100 / (len(toLoad))) * amountLoaded
		pygame.draw.rect(window, (0, 127, 255), (190, 300, 300/100*int(loadingPercent), 40), 0)
		pygame.draw.rect(window, (0, 0, 0), (190, 300, 300, 40), 5)
		if loadingPercent >= 100:
			loaded = True
		sleep(0.00001)
	else:
		window.blit(graphics[0], (0, 0))
		if page == 'Menu':
			page = mainMenu()
			mouseUp = False
		elif page == 'Credits':
			page = creds()
			mouseUp = False
		elif page == 'Generate':
			data = genNose(plainBg, graphics, img)
			img = data[1]
			page = data[0]
			mouseUp = False
		elif page == 'Go':
			data = genNose(plainBg, graphics)
			img = data[1]
			page = data[0]
			mouseUp = False
	pygame.display.update()