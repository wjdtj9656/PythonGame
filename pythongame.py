#!/usr/bin/env python
# coding: utf-8

# In[18]:


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
item_width = 30
item_height = 30
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
    
#파워 표시
def drawPower(count):
    global gamepad
    font = pygame.font.SysFont(None,20)
    text = font.render('Power :' + str(count),True,(255,255,255))
    gamepad.blit(text,(0,20))
    
#속도 표시
def drawSpeed(count):
    global gamepad
    font = pygame.font.SysFont(None,20)
    text = font.render('Speed :' + str(count),True,(255,255,255))
    gamepad.blit(text,(0,30))
    
#돈 표시
def drawMoney(count):
    global gameplad
    font = pygame.font.SysFont(None,20)
    text = font.render('Money :' + str(count),True,(255,255,255))
    gamepad.blit(text,(400,0))
    
#화면에 글씨 표시(종료)
def dispMessage(text):
    global gamepad
    textfont = pygame.font.Font('font/DX.ttf',80)
    text = textfont.render(text,True,RED)
    textpos = text.get_rect()
    textpos.center = (pad_width/2,pad_height/2)
    gamepad.blit(text,textpos)
    pygame.display.update()
    sleep(1)
    initGame()
    
def showMessage(text):
    global gamepad
    textfont = pygame.font.Font('font/DX.ttf',20)
    text = textfont.render(text,True,RED)
    textpos = text.get_rect()
    textpos.center = (pad_width/2,pad_height/2)
    gamepad.blit(text,textpos)
    pygame.display.update()
    sleep(2)
    
    
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
    
def showPower(text):
    global gamepad
    text += " = Power "
    textfont = pygame.font.Font('font/DX.ttf',80)
    text = textfont.render(text,True,RED)
    textpos = text.get_rect()
    textpos.center = (pad_width/2,pad_height*3/8)
    gamepad.blit(text,textpos)
    
#전투기가 적과 충돌했을때 메세지 출력
def crash():
    global gamepad
    dispMessage('crashed!!!!!!')

#GameOver
def gameover():
    global gamepad,deadSound
    pygame.mixer.Sound.play(deadSound)
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
    global gamepad,clock,fighter,enemy,enemy2,enemy3,bullet,bomb,item,item2,itemNum,maxShot,fighter_speed,money,bullets
    global background2,background1
    global shotSound,hitSound,deadSound,powerSound
    
    isShot = False
    shotcount = 0
    background1_y = 0
    background2_y = background_height
    currentEnemy = 0
    maxEnemy = 3
    currentEnemy2 = 0
    maxEnemy2 = 0
    currentEnemy3 = 0
    maxEnemy3 = 0
    itemCount = 0;
    levelStandard = 5
    level = 1
    maxShot = 2
    fighter_speed = 5
    money = 999
    bullets = 1
    #좌표 리스트
    bullet_xy = []
    enemy_xy = []
    item_xy = []
    enemy2_xy = []
    enemy3_xy = []
    
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
                    x_change -= fighter_speed
                elif event.key == pygame.K_RIGHT:
                    if(x_change > 5):
                        continue
                    x_change += fighter_speed
                elif event.key == pygame.K_UP:
                    if(y_change < -5):
                        continue
                    y_change -= fighter_speed
                elif event.key == pygame.K_DOWN:
                    if(y_change > 5):
                        continue
                    y_change += fighter_speed
                    
                elif event.key == pygame.K_LCTRL:
                    if len(bullet_xy) < maxShot:
                        interval = 0
                        temp = 0
                        pygame.mixer.Sound.play(shotSound)
                        bullet_x = x + fighter_width/4
                        bullet_y = y - fighter_height
                        bullet_xy.append([bullet_x,bullet_y])
                        if bullets >= 2:
                            for bulletNum in range(1,bullets):
                                if(bulletNum >= maxShot):
                                    break
                                interval -= 10
                                if bulletNum %2 ==0:
                                    temp = abs(interval)
                                elif bulletNum %2 ==1:
                                    temp = interval
                                bullet_x2 = x + temp
                                bullet_y2 = y - fighter_height
                                bullet_xy.append([bullet_x2,bullet_y])
                                
                elif event.key == pygame.K_p:
                    pause()
                    x_change = 0
                    y_change = 0
                elif event.key == pygame.K_s:
                    shopmenu()
                    x_change = 0
                    y_change = 0
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
            
        #업그레이드 적기 초기 위치
        if(currentEnemy2 < maxEnemy2):
            enemy2_x = random.randrange(0,pad_width-enemy_width)
            enemy2_y = 0
            enemy2_speed = 6
            enemy2_xy.append([enemy2_x,enemy2_y])
            currentEnemy2 += 1
            
        #업그레이드2 적기 초기 위치
        if(currentEnemy3 < maxEnemy3):
            enemy3_x = random.randrange(0,pad_width-enemy_width)
            enemy3_y = 0
            enemy3_speed = 9
            enemy3_xy.append([enemy3_x,enemy3_y])
            currentEnemy3 += 1
            
        #아이템 초기 위치
        if(itemCount > 0):
            item_x = random.randrange(0,pad_width-item_width)
            item_y = 0
            item_xy.append([item_x,item_y])
            
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
                showPower(str(maxShot))
                gameover()
        #전투기와 (업그레이드)적 전투기가 충돌했을때.
        for ex,ey in enemy2_xy:
             if(ex > x and ex < x + fighter_width and ey > y and ey < y + fighter_height) or (ex +enemy_width > x and ex +enemy_width < x + fighter_width and ey + enemy_height > y and ey < y +fighter_height):
                showLevel(str(level))
                showScore(str(shotcount))
                showPower(str(maxShot))
                gameover()
        #전투기와 (업그레이드2)적 전투기가 충돌했을때.
        for ex,ey in enemy3_xy:
             if(ex > x and ex < x + fighter_width and ey > y and ey < y + fighter_height) or (ex +enemy_width > x and ex +enemy_width < x + fighter_width and ey + enemy_height > y and ey < y +fighter_height):
                showLevel(str(level))
                showScore(str(shotcount))
                showPower(str(maxShot))
                gameover()
                
        #전투기의 무기발사 그리기
        if len(bullet_xy) != 0:
            for i,bxy in enumerate(bullet_xy):
                bxy[1] -= 10
                bullet_xy[i][1] = bxy[1]
                #총알이 적 비행기를 맞추었을때.
                for ex,ey in enemy_xy:
                    if bxy[1] < ey-10 + enemy_height and bxy[1] > ey-10:
                        if(bxy[0] > ex-10 and bxy[0] < ex-10 + enemy_width):
                            #폭발소리
                            #pygame.mixer.Sound.play(hitSound)
                            #총알,적 비행기 삭제
                            if bxy in bullet_xy:
                                bullet_xy.remove(bxy)
                                money += 1
                            enemy_xy.remove([ex,ey])
                            # 현재 적비행기 수 -1
                            currentEnemy -= 1
                            # 폭발 이미지
                            drawObject(bomb,ex,ey)
                            
                            isShot = True
                            shotcount += 1
                #총알이 (업그레이드)적 비행기를 맞추었을때.
                for ex,ey in enemy2_xy:
                    if bxy[1] < ey-10 + enemy_height and bxy[1] > ey-10:
                        if(bxy[0] > ex-10 and bxy[0] < ex-10 + enemy_width):
                            #폭발소리
                            #pygame.mixer.Sound.play(hitSound)
                            #총알,적 비행기 삭제
                            if bxy in bullet_xy:
                                bullet_xy.remove(bxy)
                                money += 2
                            enemy2_xy.remove([ex,ey])
                            # 현재 적비행기 수 -1
                            currentEnemy2 -= 1
                            # 폭발 이미지
                            drawObject(bomb,ex,ey)
                            
                            isShot = True
                            shotcount += 1
                #총알이 (업그레이드2)적 비행기를 맞추었을때.
                for ex,ey in enemy3_xy:
                    if bxy[1] < ey-10 + enemy_height and bxy[1] > ey-10:
                        if(bxy[0] > ex-10 and bxy[0] < ex-10 + enemy_width):
                            #폭발소리
                            pygame.mixer.Sound.play(hitSound)
                            #총알,적 비행기 삭제
                            if bxy in bullet_xy:
                                bullet_xy.remove(bxy)
                                money += 3
                            enemy3_xy.remove([ex,ey])
                            # 현재 적비행기 수 -1
                            currentEnemy3 -= 1
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
        if len(enemy_xy) != 0:
            for ex,ey in enemy_xy:
                    drawObject(enemy,ex,ey)
                    
        #(업그레이드)적 비행기 그리기
        if len(enemy2_xy) != 0:
            for i,exy in enumerate(enemy2_xy):
                exy[1] += enemy2_speed
                enemy2_xy[i][1] = exy[1]
                
                if exy[1] >= 640:
                    try:
                        enemy2_xy.remove(exy)
                        currentEnemy2 -= 1
                    except:
                        pass
        if len(enemy2_xy) != 0:
            for ex,ey in enemy2_xy:
                    drawObject(enemy2,ex,ey)
        
        #(업그레이드)적 비행기 그리기
        if len(enemy3_xy) != 0:
            for i,exy in enumerate(enemy3_xy):
                exy[1] += enemy3_speed
                enemy3_xy[i][1] = exy[1]
                
                if exy[1] >= 640:
                    try:
                        enemy3_xy.remove(exy)
                        currentEnemy3 -= 1
                    except:
                        pass
        if len(enemy3_xy) != 0:
            for ex,ey in enemy3_xy:
                    drawObject(enemy3,ex,ey)
                    
        #아이템 그리기
        if len(item_xy) > 0:
            for i,ixy in enumerate(item_xy):
                ixy[1] += enemy_speed
                item_xy[i][1] = ixy[1]
                
                if ixy[1] >= 640:
                    try:
                        item_xy.remove(ixy)
                        itemCount -= 1
                    except:
                        pass
        if len(item_xy) != 0:
            for ix,iy in item_xy:
                if itemNum == 0:
                    drawObject(item,ix,iy)
                elif itemNum == 1:
                    drawObject(item2,ix,iy)
                itemCount -= 1
                
         #전투기와 아이템이 충돌했을때.
        for ix,iy in item_xy:
            if(itemNum == 0 and ix > x and ix < x + fighter_width and iy > y and iy < y + fighter_height) or (itemNum ==0 and ix +enemy_width > x and ix +item_width < x + fighter_width and iy + item_height > y and iy < y +fighter_height):
                itemCount -= 1
                item_xy.remove([ix,iy])
                pygame.mixer.Sound.play(powerSound)
                maxShot += 1
            elif(itemNum == 1 and ix > x and ix < x + fighter_width and iy > y and iy < y + fighter_height) or (itemNum ==1 and ix +enemy_width > x and ix +item_width < x + fighter_width and iy + item_height > y and iy < y +fighter_height):
                itemCount -= 1
                item_xy.remove([ix,iy])
                pygame.mixer.Sound.play(powerSound)
                fighter_speed += 1
                
        #총알 그리기
        if len(bullet_xy) != 0:
            for bx,by in bullet_xy:
                drawObject(bullet,bx,by)
                
        drawScore(shotcount)
        drawLevel(level)
        drawPower(maxShot)
        drawSpeed(fighter_speed)
        drawMoney(money)
                
        if shotcount > levelStandard:
            levelStandard += 5
            maxEnemy += 1
            level += 1
            itemCount = random.choice([0,1])
            
            itemNum = random.choice([0,1])
            
            if(level > 3):
                maxEnemy2 += 1
            if level > 4:
                maxEnemy3 += 1
        drawObject(fighter,x,y)
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
#게임 초기화
def initGame():
    global gamepad,clock,fighter,enemy,enemy2,enemy3,bullet,bomb,item,item2
    global background1,background2
    global shotSound,hitSound,deadSound,powerSound
    global titleImg,startImg,quitImg,clickStartImg,clickQuitImg,Button,helpImg,helptitleImg,attackImg,moveImg,pauseImg,shopImg,preImg
    global shoptitleImg,moneyImg,bulletImg,moneyImg2
    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.pre_init(44100,-16,2,1)
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('pydi2021')
    fighter = pygame.image.load('image/fighter.png')
    fighter = pygame.transform.scale(fighter,(fighter_width,fighter_height))
    enemy = pygame.image.load('image/enemy.png')
    enemy = pygame.transform.scale(enemy,(enemy_width,enemy_height))
    enemy = pygame.transform.rotate(enemy,180)
    enemy2 = pygame.image.load('image/enemy2.png')
    enemy2 = pygame.transform.scale(enemy2,(enemy_width,enemy_height))
    enemy2 = pygame.transform.rotate(enemy2,270)
    enemy3 = pygame.image.load('image/enemy3.png')
    enemy3 = pygame.transform.scale(enemy3,(enemy_width,enemy_height))
    enemy3 = pygame.transform.rotate(enemy3,270)
    bullet = pygame.image.load('image/bullet.png')
    bullet = pygame.transform.scale(bullet,(bullet_width,bullet_height))
    bullet = pygame.transform.rotate(bullet,90)
    bomb = pygame.image.load('image/bomb.png')
    bomb = pygame.transform.scale(bomb,(enemy_width+30,enemy_height+30))
    item = pygame.image.load('image/levelup.png')
    item = pygame.transform.scale(item,(item_width,item_height))
    item2 = pygame.image.load('image/speedup.png')
    item2 = pygame.transform.scale(item2,(item_width,item_height))
    item2 = pygame.transform.rotate(item2,90)
    background1 = pygame.image.load('image/background.png')
    background2 = background1.copy()
    shotSound = pygame.mixer.Sound('sound/shotSound.wav')
    shotSound.set_volume(0.3)
    hitSound = pygame.mixer.Sound('sound/hitSound2.wav')
    hitSound.set_volume(0.3)
    powerSound = pygame.mixer.Sound('sound/getpower.wav')
    powerSound.set_volume(0.3)
    deadSound = pygame.mixer.Sound('sound/dead.wav')
    deadSound.set_volume(1.0)
    pygame.mixer.music.load('sound/bgm.wav')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    #메인 메뉴
    titleImg = pygame.image.load("image/title.PNG")
    startImg = pygame.image.load("image/start.png")
    quitImg = pygame.image.load("image/quit.png")
    clickStartImg = pygame.image.load("image/clickedstart.png")
    clickQuitImg = pygame.image.load("image/clickedquit.png")
    helpImg = pygame.image.load("image/helpi.png")
    helpImg = pygame.transform.scale(helpImg,(100,100))
    helptitleImg = pygame.image.load("image/helptitle.png")
    helptitleImg = pygame.transform.scale(helptitleImg,(100,100))
    attackImg = pygame.image.load("image/attack.PNG")
    attackImg = pygame.transform.scale(attackImg,(200,30))
    moveImg = pygame.image.load("image/move.PNG")
    moveImg = pygame.transform.scale(moveImg,(200,30))
    pauseImg = pygame.image.load("image/pause.PNG")
    pauseImg = pygame.transform.scale(pauseImg,(200,30))
    shopImg = pygame.image.load("image/shop.PNG")
    shopImg = pygame.transform.scale(shopImg,(200,30))
    preImg = pygame.image.load("image/pre.PNG")
    preImg = pygame.transform.scale(preImg,(200,100))
    shoptitleImg = pygame.image.load("image/shoptitle.png")
    shoptitleImg = pygame.transform.scale(shoptitleImg,(200,200))
    moneyImg = pygame.image.load("image/needMoney.png")
    moneyImg = pygame.transform.scale(moneyImg,(50,50))
    moneyImg2 = pygame.image.load("image/price1.PNG")
    moneyImg2 = pygame.transform.scale(moneyImg2,(50,50))
    bulletImg = pygame.image.load("image/bullets.png")
    bulletImg = pygame.transform.scale(bulletImg,(70,70))
    
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    runGame()
                
        gamepad.fill(BLACK)
        
        titletext = gamepad.blit(titleImg,(140,200))
        startButton = Button(startImg,120,430,140,20,clickStartImg,120,430,runGame)
        quitButton = Button(quitImg,320,430,60,20,clickQuitImg,320,430,quitgame)
        helpButton = Button(helpImg,200,480,200,480,helpImg,200,480,helpmenu)
        pygame.display.update()
        clock.tick(15)
def helpmenu():
    helpm = True
    while helpm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mainmenu()
                    
        gamepad.fill(BLACK)
        
        helptitle = gamepad.blit(helptitleImg,(200,100))
        attackTitle = gamepad.blit(attackImg,(150,300))
        moveTitle = gamepad.blit(moveImg,(150,350))
        pauseTitle = gamepad.blit(pauseImg,(150,400))
        shopTitle = gamepad.blit(shopImg,(150,450))
        preTitle = Button(preImg,200,500,200,480,preImg,200,500,mainmenu)
        pygame.display.update()
        clock.tick(15)
def shopmenu():
    global maxShot,fighter_speed,money,shop
    shop = True
    gamepad.fill(BLACK)
    
    def shopSwitch():
        global shop
        shop = False
    while shop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shop = False
        shoptitle = gamepad.blit(shoptitleImg,(140,100))
        powerButton = Button(item,120,430,100,100,item,120,430,buyPowerUp)
        speedButton = Button(item2,320,430,100,100,item2,320,430,buySpeedUp)
        bulletButton = Button(bulletImg,210,300,100,100,bulletImg,210,300,bulletUp)
        moneyImg1a = gamepad.blit(moneyImg,(110,460))
        moneyImg2a = gamepad.blit(moneyImg,(310,460))
        moneyImg3a = gamepad.blit(moneyImg2,(210,370))
        preTitle = Button(preImg,200,500,200,480,preImg,200,500,shopSwitch)
        pygame.display.update()
        clock.tick(15)
def buyPowerUp():
    global maxShot,money,shop
    if money >= 50:
        maxShot += 1
        money -= 50
        showMessage("구매완료//게임으로 돌아갑니다.")
        shop = False
    else:
        showMessage("돈 부족//게임으로 돌아갑니다.")
        shop = False
def buySpeedUp():
    global fighter_speed,money,shop
    if money >= 50:
        fighter_speed += 1
        money -= 50
        showMessage("구매완료//게임으로 돌아갑니다.")
        shop = False
    else:
        showMessage("돈부족//게임으로 돌아갑니다.")
        shop = False
def bulletUp():
    global fighter_speed,money,shop,bullets
    if money >= 50:
        bullets += 1
        money -= 200
        showMessage("구매완료//게임으로 돌아갑니다.")
        shop = False
    else:
        showMessage("돈부족//게임으로 돌아갑니다.")
        shop = False
def pause():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_p:
                    pause = False
initGame()
#runGame()


# In[ ]:




