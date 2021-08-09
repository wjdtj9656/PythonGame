#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame

BLACK = (0,0,0)
pad_width = 480
pad_height = 640

def runGame():
    global gamepad,clock
    
    ongame = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doneFlag = True
        gamepad.fill(BLACK)
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()

def initGame():
    global gamepad,clock
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('dCovery')
    clock = pygame.time.Clock()
    
initGame()
runGame()

