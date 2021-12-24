#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

#TELA
height = 640
width = 480

#SONS
pygame.mixer.music.set_volume(0.5)
music = pygame.mixer.music.load('C:/Users/Matheus/OneDrive/Documentos/Projetos/python/pygame/SeekGame/songs/BoxCat Games - CPU Talk.mp3')
found_sound = pygame.mixer.Sound('C:/Users/Matheus/OneDrive/Documentos/Projetos/python/pygame/SeekGame/songs/smw_lemmy_wendy_correct.wav')
loser_sound = pygame.mixer.Sound('C:/Users/Matheus/OneDrive/Documentos/Projetos/python/pygame/SeekGame/songs/smw_lemmy_wendy_falls_out_of_pipe.wav')

pygame.mixer.music.play(-1)

#PLAYER + MOB
y_player = random.randint(40,400)
x_player = random.randint(40,400)

x_mob = random.randint(40,400)
y_mob = random.randint(40,400)

x_trap = random.randint(40,400)
y_trap = random.randint(40,400)

#GAME
found = False
light = False

#VIDA
life = 5

points = 0

fonte_texto = pygame.font.SysFont('arial', 40, True, False)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((height, width))

while True:
    clock.tick(60)
    screen.fill((0,0,0))
    texto = f'Points: {points}'
    texto_formatado = fonte_texto.render(texto, False, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                y_player -= 40
            if event.key == K_a:
                x_player -= 40
            if event.key == K_s:
                y_player += 40
            if event.key == K_d:
                x_player += 40
            if event.key == K_j:
                y_player = random.randint(40,400)
                x_player = random.randint(40,400)
            if event.key == K_f:
                light = True
            if event.key == K_c:
                light = False
            if event.key == K_g:
                pist = pygame.draw.rect(screen, (255, 0, 0), (x_mob-5, y_mob-5, 50, 50))
                if found == True:
                    pist = pygame.draw.rect(screen, (0, 255, 0), (x_mob-5, y_mob-5, 50, 50))
                    
    #LUZ         
    if light == True:
        lig = pygame.draw.circle(screen, (0, 0, 10), (x_player+20, y_player+20), 50)
        if lig.colliderect(mob):
            x_mob = random.randint(40,400)
            y_mob = random.randint(40,400)
            points += 1
            found_sound.play()
            
        if lig.colliderect(trap):
            life = life - 1
            if life == 0:
                print('you lost')
                pygame.quit()
                exit()
       
    #OBJETOS
    player = pygame.draw.rect(screen, (255, 255, 255), (x_player, y_player, 40, 40))
    mob = pygame.draw.rect(screen, (0, 0, 0), (x_mob, y_mob, 40, 40))
    trap = pygame.draw.rect(screen, (0, 0, 0), (x_trap, y_trap, 40, 40))
    
    #VIDA
    player_life = pygame.draw.rect(screen, (0, 255, 0), (x_player, y_player-10, 40, life))
            
    #BARREIRA
    if y_player <= -40:
        y_player = 440
    if y_player >= 480:
        y_player = 0
    if x_player <= -40:
        x_player = 600
    if x_player >= 640:
        x_player = 0
        
    screen.blit(texto_formatado, (50,40))
    pygame.display.update()

