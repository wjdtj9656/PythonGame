#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pygame
import random
import sys
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
background_height = 700


#점수 계산
def drawScore(count):
    global gamepad
    font = pygame.font.SysFont(None,20)
    text = font.render('Enemy Kills:' + str(count),True,(255,255,255))
    gamepad.blit(text,(0,10))
#레벨 표시
def drawLevel(count):
    global gamepad
    font = pygame.font.SysFont(None,20)
    text = font.render('Level :' + str(count),True,(255,255,255))
    gamepad.blit(text,(0,0))
#화면에 글씨 표시(종료)
def dispMessage(text):
    global gamepad
    textfont = pygame.font.Font('font/DX.ttf',80)
    text = textfont.render(text,True,RED)
    textpos = text.get_rect()
    textpos.center = (pad_width/2,pad_height/2)
    gamepad.blit(text,textpos)
    pygame.display.update()
    sleep(2)
    initGame()
    
def showLevel(text):
    global gamepad
    text += " = LEVEL "
    textfont = pygame.font.Font('font/DX.ttf',80)
    text = textfont.render(text,True,RED)
    textpos = text.get_rect()
    textpos.center = (pad_width/2,pad_height/4)
    gamepad.blit(text,textpos)
    
def showScore(text):
    global gamepad
    text += " = Score "
    textfont = pygame.font.Font('font/DX.ttf',80)
    text = textfont.render(text,True,RED)
    textpos = text.get_rect()
    textpos.center = (pad_width/2,pad_height/8)
    gamepad.blit(text,textpos)
    
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
    
#배경화면
def back(background,x,y):
    global gamepad
    gamepad.blit(background,(x,y))
    
#게임 실행
def runGame():
    global gamepad,clock,fighter,enemy,bullet,bomb
    global background2,background1
    global shotSound,hitSound
    
    isShot = False
    shotcount = 0
    background1_y = 0
    background2_y = background_height
    currentEnemy = 0
    maxEnemy = 3
    levelStandard = 5
    level = 1
    
    #무기 좌표 리스트
    bullet_xy = []
    enemy_xy = []
    
    #전투기 초기 위치
    x = pad_width*0.45
    y = pad_height*0.9
    x_change = 0
    y_change = 0
    
    
        
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
                        pygame.mixer.Sound.play(shotSound)
                        bullet_x = x + fighter_width/4
                        bullet_y = y - fighter_height
                        bullet_xy.append([bullet_x,bullet_y])
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0;
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    
        gamepad.fill(BLACK)
        #적기 초기 위치
        if(currentEnemy < maxEnemy):
            enemy_x = random.randrange(0,pad_width-enemy_width)
            enemy_y = 0
            enemy_speed = 3
            enemy_xy.append([enemy_x,enemy_y])
            currentEnemy += 1
            
        #배경 움직이기
        background1_y -= 1
        background2_y -= 1
        if background1_y == -background_height:
            background1_y = background_height
        if background2_y == -background_height:
            background2_y = background_height
        back(background1,0,background1_y)
        back(background2,0,background2_y)
        
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
        for ex,ey in enemy_xy:
             if(ex > x and ex < x + fighter_width and ey > y and ey < y + fighter_height) or (ex +enemy_width > x and ex +enemy_width < x + fighter_width and ey + enemy_height > y and ey < y +fighter_height):
                showLevel(str(level))
                showScore(str(shotcount))
                gameover()
                
        #전투기의 무기발사 그리기
        if len(bullet_xy) != 0:
            for i,bxy in enumerate(bullet_xy):
                bxy[1] -= 10
                bullet_xy[i][1] = bxy[1]
                
                #총알이 적 비행기를 맞추었을때.
                for ex,ey in enemy_xy:
                    if bxy[1] < ey:
                        if(bxy[0] > ex-10 and bxy[0] < ex-10 + enemy_width):
                            #폭발소리
                            pygame.mixer.Sound.play(hitSound)
                            #총알,적 비행기 삭제
                            bullet_xy.remove(bxy)
                            enemy_xy.remove([ex,ey])
                            # 현재 적비행기 수 -1
                            currentEnemy -= 1
                            # 폭발 이미지
                            drawObject(bomb,ex,ey)
                            
                            isShot = True
                            shotcount += 1
                if bxy[1] <= 0:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
        #적 비행기 그리기
        if len(enemy_xy) != 0:
            for i,exy in enumerate(enemy_xy):
                exy[1] += enemy_speed
                enemy_xy[i][1] = exy[1]
                
                if exy[1] >= 640:
                    try:
                        enemy_xy.remove(exy)
                        currentEnemy -= 1
                    except:
                        pass
                    
        if len(bullet_xy) != 0:
            for bx,by in bullet_xy:
                drawObject(bullet,bx,by)
        drawScore(shotcount)
        drawLevel(level)
        if len(enemy_xy) != 0:
            for ex,ey in enemy_xy:
                drawObject(enemy,ex,ey)
        if shotcount > levelStandard:
            levelStandard += 5
            maxEnemy += 1
            level += 1
        
        drawObject(fighter,x,y)
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
#게임 초기화
def initGame():
    global gamepad,clock,fighter,enemy,bullet,bomb
    global background1,background2
    global shotSound,hitSound
    global titleImg,startImg,quitImg,clickStartImg,clickQuitImg,Button
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('pydi2021')
    fighter = pygame.image.load('image/fighter.png')
    fighter = pygame.transform.scale(fighter,(fighter_width,fighter_height))
    enemy = pygame.image.load('image/enemy.png')
    enemy = pygame.transform.scale(enemy,(enemy_width,enemy_height))
    enemy = pygame.transform.rotate(enemy,180)
    bullet = pygame.image.load('image/bullet.png')
    bullet = pygame.transform.scale(bullet,(bullet_width,bullet_height))
    bullet = pygame.transform.rotate(bullet,90)
    bomb = pygame.image.load('image/bomb.png')
    bomb = pygame.transform.scale(bomb,(enemy_width+30,enemy_height+30))
    background1 = pygame.image.load('image/background.png')
    background2 = background1.copy()
    shotSound = pygame.mixer.Sound('sound/shotSound.wav')
    hitSound = pygame.mixer.Sound('sound/hitSound.wav')
    pygame.mixer.music.load('sound/bgm.wav')
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    #메인 메뉴
    titleImg = pygame.image.load("image/title.PNG")
    startImg = pygame.image.load("image/start.png")
    quitImg = pygame.image.load("image/quit.png")
    clickStartImg = pygame.image.load("image/clickedstart.png")
    clickQuitImg = pygame.image.load("image/clickedquit.png")

    class Button:
        def __init__(self, img_in, x, y, width, height, img_act, x_act,y_act, action = None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x+width > mouse[0] >x and y + height >mouse[1] > y:
                gamepad.blit(img_act,(x_act, y_act))
                if click[0] and action != None:
                    sleep(1)
                    action()
            else:
                gamepad.blit(img_in,(x,y))
    mainmenu()
    
def quitgame():
    pygame.quit()
    sys.exit()

def mainmenu():
    menu = True
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gamepad.fill(BLACK)
        
        titletext = gamepad.blit(titleImg,(140,320))
        startButton = Button(startImg,120,430,140,20,clickStartImg,120,430,runGame)
        quitButton = Button(quitImg,320,430,60,20,clickQuitImg,320,430,quitgame)
        pygame.display.update()
        clock.tick(15)
        
initGame()
#runGame()


# In[ ]:




