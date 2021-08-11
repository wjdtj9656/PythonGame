#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pygame
import random
from time import sleep

#게임 내 전역 변수
BLACK = (0,0,0)
RED = (255,0,0)
pad_width = 480
pad_height = 640
fighter_width = 36;
fighter_height = 38;
enemy_width = 30
enemy_height = 30
bullet_width = 25
bullet_height = 25

#점수 계산
def drawScore(count):
    global gamepad
    font = pygame.font.SysFont(None,20)
    text = font.render('Enemy Kills:' + str(count),True,(255,255,255))
    gamepad.blit(text,(0,0))

#화면에 글씨 보이게
def dispMessage(text):
    global gamepad
    textfont = pygame.font.Font('font/DX.ttf',80)
    text = textfont.render(text,True,RED)
    textpos = text.get_rect()
    textpos.center = (pad_width/2,pad_height/2)
    gamepad.blit(text,textpos)
    pygame.display.update()
    sleep(2)
    runGame()

#전투기가 적과 충돌했을때 메세지 출력
def crash():
    global gamepad
    dispMessage('crashed!!!!!!')

#GameOver
def gameover():
    global gamepad
    dispMessage('Game Over!')

#게임 등장 객체
def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))
    
#게임 실행
def runGame():
    global gamepad,clock,fighter,enemy,bullet
    
    isShot = False
    shotcount = 0
    
    #무기 좌표 리스트
    bullet_xy = []
    
    #전투기 초기 위치
    x = pad_width*0.45
    y = pad_height*0.9
    x_change = 0
    y_change = 0
    
    #적기 초기 위치
    enemy_x = random.randrange(0,pad_width-enemy_width)
    enemy_y = 0
    enemy_speed = 3
    
    ongame = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if(x_change < -5):
                        continue
                    x_change -= 5
                elif event.key == pygame.K_RIGHT:
                    if(x_change > 5):
                        continue
                    x_change += 5
                elif event.key == pygame.K_UP:
                    if(y_change < -5):
                        continue
                    y_change -= 5
                elif event.key == pygame.K_DOWN:
                    if(y_change > 5):
                        continue
                    y_change += 5
                    
                elif event.key == pygame.K_LCTRL:
                    if len(bullet_xy) < 2:
                        bullet_x = x + fighter_width/4
                        bullet_y = y - fighter_height
                        bullet_xy.append([bullet_x,bullet_y])
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0;
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        gamepad.fill(BLACK)
        
        #전투기 위치 재조정
        x += x_change
        if x < 0:
            x=0
        elif x > pad_width - fighter_width:
            x = pad_width - fighter_width
        y += y_change
        if y < 0:
            y = 0
        elif y > pad_height - fighter_height:
            y = pad_height - fighter_height

            
        #전투기와 적 전투기가 충돌했을때.
        if(enemy_x > x and enemy_x < x + fighter_width and enemy_y > y and enemy_y < y + fighter_height) or (enemy_x +enemy_width > x and enemy_x +enemy_width < x + fighter_width and enemy_y + enemy_height > y and enemy_y < y +fighter_height):
            crash()
        #전투기의 무기발사 그리기
        if len(bullet_xy) != 0:
            for i,bxy in enumerate(bullet_xy):
                bxy[1] -= 10
                bullet_xy[i][1] = bxy[1]
                
                #총알이 적 비행기를 맞추었을때.
                if bxy[1] < enemy_y:
                    if bxy[0] > enemy_x-10 and bxy[0] < enemy_x-10 + enemy_width:
                        bullet_xy.remove(bxy)
                        
                        isShot = True
                        shotcount += 1
                        
                if bxy[1] <= 0:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
        if len(bullet_xy) != 0:
            for bx,by in bullet_xy:
                drawObject(bullet,bx,by)
                
        drawScore(shotcount)
        
        #적을 아래로 이동
        enemy_y += enemy_speed
        if enemy_y > pad_height:
            enemy_y = 0
            enemy_x = random.randrange(0,pad_width-enemy_width)
        
        
        drawObject(enemy,enemy_x,enemy_y)
        drawObject(fighter,x,y)
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
#게임 초기화
def initGame():
    global gamepad,clock,fighter,enemy,bullet
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('dCovery')
    fighter = pygame.image.load('image/fighter.png')
    fighter = pygame.transform.scale(fighter,(fighter_width,fighter_height))
    enemy = pygame.image.load('image/enemy.png')
    enemy = pygame.transform.scale(enemy,(enemy_width,enemy_height))
    enemy = pygame.transform.rotate(enemy,180)
    bullet = pygame.image.load('image/bullet.png')
    bullet = pygame.transform.scale(bullet,(bullet_width,bullet_height))
    bullet = pygame.transform.rotate(bullet,90)
    clock = pygame.time.Clock()
    
initGame()
runGame()


# In[ ]:




