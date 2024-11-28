# Vrank fighter
# this is my program for making game

import pygame
import random
import numpy
import cv2
#from PIL import Image

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()

# **** VARIABLES ****

WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BROWN = (150, 75, 0)
bWIDTH, bHEIGHT = 160,160
valP1 = pygame.Rect(400,300, 1, 1)
valP2 = pygame.Rect(400,300, 1, 1)
HEARTimg = pygame.image.load('HEART.png')
HEART = pygame.transform.scale(HEARTimg, (50, 50))
TITLE_font = pygame.font.SysFont('castellar', 40)
CHARTITLE_font = pygame.font.SysFont('castellar', 30)
CHAR_font = pygame.font.SysFont('castellar', 22)
title_font=  pygame.font.SysFont('comicsansms', 18)
TITLE = TITLE_font.render("CHOOSE A MAP", 5, WHITE)
CHARtitle = CHARTITLE_font.render("CHOOSE YOUR CHARACTERS", 5, RED)
CHAR1title = CHAR_font.render("PLAYER 1 (WASD)", 5, WHITE)
CHAR2title = CHAR_font.render("PLAYER 2 (ARROW KEYS)", 5, WHITE)

#MAPS
DOJOimg = pygame.image.load('DOJO.jpg')
DOJObutton = pygame.transform.scale(DOJOimg,(bWIDTH, bHEIGHT))
DOJO = pygame.transform.scale(DOJOimg,(WIDTH, HEIGHT))
selVRANKDOJO = False
titleDOJO = title_font.render("VRANKS DOJO", 5, WHITE)

CHURCHimg = pygame.image.load('CHURCH.jpg')
CHURCH = pygame.transform.scale(CHURCHimg,(WIDTH, HEIGHT))
CHURCHbutton = pygame.transform.scale(CHURCHimg,(bWIDTH, bHEIGHT))
selVRANKCHURCH = False
titleCHURCH = title_font.render("HOLY CHURCH OF VRANK", 80, WHITE)

PLUMBINGimg = pygame.image.load('PLUMBING.jpg')
PLUMBING = pygame.transform.scale(PLUMBINGimg,(WIDTH, HEIGHT))
PLUMBINGbutton = pygame.transform.scale(PLUMBINGimg,(bWIDTH, bHEIGHT))
selVRANKPLUMBING = False
titlePLUMBING = title_font.render("PLUMBING FACILITY", 5, WHITE)

#CHARACTER VARIABLES
velJASE = 10
JASEwidth, JASEheight = 80, 80
JASEimg = pygame.image.load('JASE.jpg')
JASE = pygame.transform.scale(JASEimg,(JASEwidth, JASEheight))
JASEbutton = pygame.transform.scale(JASEimg, (100, 100))
JASEbullets = []
JASEbullets1 = []
JASEbulVEL = 15
PERCimg = pygame.image.load('PERC.png')
PERC = pygame.transform.scale(PERCimg, (30, 30))
JASEperc1 = pygame.Rect(-500, -500, 0, 0)
JASEperc2 = pygame.Rect(-500, -500, 0, 0)
valJASE = pygame.Rect(400,300,JASEwidth, JASEheight)
JASEperc1 = pygame.Rect(random.randint(25,WIDTH),random.randint(0,HEIGHT), 30, 30)
JASEperc2 = pygame.Rect(random.randint(25,WIDTH),random.randint(0,HEIGHT), 30, 30)
tolJ1 = random.randint(1,3)
SMOKEimg = pygame.image.load('SMOKE.png')
smoke_s, smoke_s1, smoke_x, smoke_y = 0,0, -500,-500
jaseSMOKE = pygame.Rect(-500,-500, smoke_s, smoke_s1)
smoke_Y = 0
jaseVAPEimg = pygame.image.load('stlth.jpg')
jaseVAPE = pygame.transform.scale(jaseVAPEimg,(110,90))

velCALLUM = 10
CALLUMwidth, CALLUMheight = 80,80
CALLUMimg = pygame.image.load('CALLUM.JPG')
CALLUM = pygame.transform.scale(CALLUMimg,(CALLUMwidth, CALLUMheight))
CALLUMbutton = pygame.transform.scale(CALLUMimg,(100,100))
CALLUMbullets = []
CALLUMbullets1 = []
CALLUMbulVEL = 15
valCALLUM = pygame.Rect(400,300,CALLUMwidth,CALLUMheight)
CALLUMRODimg = pygame.image.load('CALLUMROD.png')
CALLUMROD = pygame.transform.scale(CALLUMRODimg,(60,140))
CALLUMRODrect = pygame.Rect(-500,-500,30,70)
FISHING = False
REEL = False
FISHINGSTUN = False
REELIN_sound = pygame.mixer.Sound('REELIN.wav')
callumrodicon = pygame.image.load('callumrodicon.png')
callumROD = pygame.transform.scale(callumrodicon,(40,40))
callumdomicon = pygame.image.load("callumdomain.jpg")
callumDOM = pygame.transform.scale(callumdomicon,(50,50))
BULtime = False
ChickenCatch = False
WALNUTimg = pygame.image.load('Walnut.png')
WALNUT = pygame.transform.scale(WALNUTimg,(CALLUMwidth, CALLUMheight))
Chickenimg = pygame.image.load('chicken.jpg')
CHICKEN = pygame.transform.scale(Chickenimg,(60,60))
Chicken2img = pygame.image.load('chicken2.jpg')
CHICKEN2 = pygame.transform.scale(Chicken2img,(60,60))
Chicken3img = pygame.image.load('chicken3.jpg')
CHICKEN3 = pygame.transform.scale(Chicken3img,(60,60))
ChickenList = list()
StoredChickens = list()
numbchickens = 12
numbstoredchickens = 0
CallumBackyardimg = pygame.image.load('CallumBackyard.jpg')
CallumBackyard = pygame.transform.scale(CallumBackyardimg,(WIDTH, HEIGHT))
FarmSong = pygame.mixer.Sound('FarmTrack.wav')

velLANE = 10 
LANEwidth, LANEheight = 90, 90
LANEimg = pygame.image.load('LANE.JPG')
LANE = pygame.transform.scale(LANEimg,(LANEwidth,LANEheight))
LANELOVEimg = pygame.image.load('HEART.png')
LANELOVE = pygame.transform.scale(LANELOVEimg,(40,40))
CUTELANEimg = pygame.image.load('CUTELANE.png')
CUTELANE = pygame.transform.scale(CUTELANEimg,(LANEwidth,LANEheight))
LANEbutton = pygame.transform.scale(LANEimg,(100,100))
LANEbullets = []
LANEbullets1 = []
LOVEbullets = []
LANEbulVEL = 15
intLOVEbullets = 0
valLANE = pygame.Rect(400,300,LANEwidth,LANEheight)
LANEOVERLOAD = False

velGOOMBA = 12
GOOMBAwidth, GOOMBAheight = 70, 70
KENimg = pygame.image.load('GOOMBA.jpg')
GOOMBA = pygame.transform.scale(KENimg,(GOOMBAwidth, GOOMBAheight))
KENbutton = pygame.transform.scale(KENimg, (100, 100))
k808_sound = pygame.mixer.Sound('KenCarson.wav')
KENbullets = []
KENbullets1 = []
KENbulVEL = 15
valGOOMBA = pygame.Rect(400,300, GOOMBAwidth, GOOMBAheight)
RICKimg = pygame.image.load('RICKS.jpg')
RICK = pygame.transform.scale(RICKimg,(50,50))
RICK1img = pygame.image.load('RICK1.jpg')
RICK1 = pygame.transform.scale(RICK1img,(50,50))
KENricksimg = RICK
KENrick = pygame.Rect(-500,-500 + 50, 40,40)
RICK1.set_colorkey(WHITE)
RICK.set_colorkey(WHITE)
RICKSbutton = pygame.transform.scale(RICKimg,(40,40))
RICKSbutton.set_colorkey(WHITE)

valLONE = pygame.Rect(-500,-500,GOOMBAwidth,GOOMBAheight)
LONEimg = pygame.image.load('LONE.jpg')
LONE = pygame.transform.scale(LONEimg,(GOOMBAwidth,GOOMBAheight))
LONEbuttonimg = pygame.image.load('LONEbutton.jpg')
LONEbutton = pygame.transform.scale(LONEbuttonimg,(40,40))
LONEhealth = 20
LONEbullets = []
LONEbulVEl = 15

VRANKwidth, VRANKheight = 90, 90
velVRANK = 9
VRANKimg = pygame.image.load('VRANKt.jpg')
VRANK = pygame.transform.scale(VRANKimg,(VRANKwidth,VRANKheight))
VRANKbutton = pygame.transform.scale(VRANKimg, (100, 100))
VRANKbulVEL = 15
VRANKbullets = []
VRANKbullets1 = []
valVRANK = pygame.Rect(200,300, VRANKwidth, VRANKheight)
VRANKsheild = pygame.Rect(-500, -500, 0, 0)
BURGERimg = pygame.image.load('SMASHBURGER.jpg')
BURGER = pygame.transform.scale(BURGERimg, (120,250))
MUNCH_sound = pygame.mixer.Sound('MUNCH.wav')
burgerimg = pygame.image.load('burger.png')
burger = pygame.transform.scale(burgerimg,(40,40))
VRANKdogimg = pygame.image.load('vrankhusky.png')
VRANKdog = pygame.transform.scale(VRANKdogimg,(100,100))
VRANKdogrect = VRANKdog.get_rect()
VRANKdog1 = pygame.Rect(0,-500,VRANKdogrect.w,VRANKdogrect.h)
VRANKdog2 = pygame.Rect(0,-500,VRANKdogrect.w,VRANKdogrect.h)
VRANKdog3 = pygame.Rect(0,-500,VRANKdogrect.w,VRANKdogrect.h)
VRANKdog4 = pygame.Rect(0,-500,VRANKdogrect.w,VRANKdogrect.h)
dogiconimg = pygame.image.load('huskyicon.png')
dogicon = pygame.transform.scale(dogiconimg,(40,40))
EAGLE_sound = pygame.mixer.Sound("EAGLE.wav")

BROCKwidth, BROCKheight = 80, 80
velBROCK = 10
velxBROCK = 25
BROCKimg = pygame.image.load('BROCK.jpg')
BROCK = pygame.transform.scale(BROCKimg, (BROCKwidth, BROCKheight))
BROCKbutton = pygame.transform.scale(BROCKimg, (100, 100))
Dirtbike_sound = pygame.mixer.Sound('BROCKSDIRTBIKE.wav')
BROCKbullets = []
BROCKbullets1 = []
BROCKbulVEL = 15
valBROCK = pygame.Rect(200,300, BROCKwidth, BROCKheight)
BROCKbike = pygame.Rect(-500, -500, 0, 0)
BROCKbike1 = pygame.Rect(1500, 1500, 0, 0)
valBIKE_x, valBIKE_y = valP1.x, valP1.y
BIKE1img = pygame.image.load('DIRTBIKE1.png')
BIKE2img = pygame.image.load('DIRTBIKE2.png')
BIKE1 = pygame.transform.scale(BIKE1img, (160, 100))
BIKE2 = pygame.transform.scale(BIKE2img, (160, 100))
bikeiconimg = pygame.image.load('bikebutton.png')
bikeicon = pygame.transform.scale(bikeiconimg,(40,40))
cooldownB1 = 0
cooldownB2 = 0
brockcharge = 0

TITLE_font = pygame.font.SysFont('castellar', 40)
title_font=  pygame.font.SysFont('comicsansms', 18)
TITLE = TITLE_font.render("CHOOSE A MAP", 5, WHITE)
Health_font = pygame.font.SysFont('Segoe UI', 27)
GAME_font = pygame.font.SysFont('Dark Stone', 29)
tol_text = GAME_font.render("TOLERENCE BREAK", 5, WHITE)

bulletpng = pygame.image.load('bullet.png')
bullet1png = pygame.image.load('bullet1.png')
bullet1img = pygame.transform.scale(bullet1png,(40,40))
bulletimg = pygame.transform.scale(bulletpng,(40,40))
pew_sound = pygame.mixer.Sound('pew.wav')
P1_HIT = pygame.USEREVENT + 1
P2_HIT = pygame.USEREVENT + 2
LONE_HIT = pygame.USEREVENT + 3
particles = []
current_time = pygame.time.get_ticks()
cooldownV1 = -8000
cooldownV2 = -12000
cooldownJ1 = -5000
cooldownJ2 = -9000
cooldownB1 = -8000
cooldownB2 = -8000
cooldownJ3 = 0
cooldownG1 = -12000
cooldownG2 = -18000
cooldownC1 = -5000
cooldownC2 = -120000
cooldownL1 = -18000
LaneCuteTime = 6000
LONEbultime = -400
fishingstun_time = -2000

tolBREAK = False
selJASE = False
selGOOMBA = False
selBROCK = False
selVRANK = False
MAPsel = False
CHAR1sel = False
CHAR2sel = False
run = True
smoke = True
ExplosionP1 = False
collide = False
BROCKbol = False
left = False
right = False
ricks = False
lone = False
loneswitch = False
# **** CLASSES ****
class Button:
    def __init__ (self, x, y, image, scale):
        buttonWIDTH, buttonHEIGHT = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image,(int(buttonWIDTH * scale),int(buttonHEIGHT * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def DrawButton(self):
        action = False
        
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
        screen.blit(self.image,(self.rect.x, self.rect.y))
        return action
    
class Explosion(pygame.sprite.Sprite):  #class for Explosion
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 12):
            ######### Add these images to the folder
            img = pygame.image.load(f'Explosion{num}.png')
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosion_speed = 1
        #update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

class  cls_Particle(): #class for particles under ship, behind bullets.
    def __init__(self,x, y, x_vel, y_vel, radius, colour, lifetime):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = radius 
        self.colour = colour
        self.lifetime = lifetime #variable to determime when to take the particle off of the screen
        
    def DrawParticles(self,screen): #method for drawing the particles with the values provided when creating a instance of the class
        self.lifetime -= 1
        self.x += self.x_vel
        self.y += self.y_vel
        pygame.draw.circle(screen, self.colour,(self.x,self.y),self.radius)

class cls_Chicken():
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.imgint = int(random.randint(1,3))
        if self.imgint == 1:
            self.img = CHICKEN
        elif self.imgint == 2:
            self.img = CHICKEN2
        elif self.imgint == 3:
            self.img = CHICKEN3
        self.speedx = int(random.randint(-12,12))
        self.speedy = int(random.randint(-12,12))
        self.hitbox = pygame.Rect(self.x, self.y, 60,60)
        self.stored = False

class cls_LANEHEART():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = LANELOVE
        self.speed = 20
        self.hitbox = pygame.Rect(self.x, self.y, 40,40)

# **** FUNCTIONS ****

def CALLUMbullettime():
    pygame.transform.average_color()
def P1Movement():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] and valP1.y - valP1.h - velP1 > 0 - valP1.h:
        valP1.y -= velP1
    if keys_pressed[pygame.K_s] and valP1.y + valP1.h + velP1 < HEIGHT:
        valP1.y += velP1
    if keys_pressed[pygame.K_a] and valP1.x - valP1.w - velP1 > 0 - valP1.w:
        valP1.x -= velP1
    if keys_pressed[pygame.K_d] and valP1.x + valP1.w + velP1 < WIDTH:
        valP1.x += velP1

def CallumFishing(valP1, valP2):
    global FISHING
    global FISHINGSTUN
    if not valP1.colliderect(valP2):
        if valP1.x > valP2.x:
            valP1.x -= 22
        elif valP1.x < valP2.x:
            valP1.x += 22
        if valP1.y > valP2.y:
            valP1.y -= 14 
        elif valP1.y < valP2.y:
            valP1.y += 14
    if valP1.colliderect(valP2):
        FISHING = False
        FISHINGSTUN = True

def P2Movement():
    global left
    global right
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and valP2.y - valP2.h - velP2 > 0 - valP2.h:
        valP2.y -= velP2
        if lone == True and valLONE.y - valLONE.h - velP2 > 0 - valLONE.h:
            valLONE.y -= velGOOMBA
    if keys_pressed[pygame.K_DOWN] and valP2.y + valP2.h + velP2 < HEIGHT:
        valP2.y += velP2
        if lone == True and valLONE.y + valLONE.h + velP2 < HEIGHT:
            valLONE.y += velGOOMBA
    if keys_pressed[pygame.K_LEFT] and valP2.x - valP2.w - velP2 > 0 - valP2.w:
        valP2.x -= velP2
        left = True
        right = False
    if keys_pressed[pygame.K_RIGHT] and valP2.x + valP2.w + velP2 < WIDTH:
        valP2.x += velP2
        right = True
        left = False

def ChickenSpawn():
    for i in range(numbchickens):
        ChickenList.append(cls_Chicken(random.randint(60, 660), random.randint(100, 550)))
def ChickenMove():
    for i in range(numbchickens):
        ChickenList[i].x = ChickenList[i].x + ChickenList[i].speedx
        ChickenList[i].y = ChickenList[i].y + ChickenList[i].speedy
        if ChickenList[i].x >= 700:
            ChickenList[i].speedx = -ChickenList[i].speedx
        if ChickenList[i].x <= 40:
            ChickenList[i].speedx = -ChickenList[i].speedx
        if ChickenList[i].y <= 100:
            ChickenList[i].speedy = -ChickenList[i].speedy
        if ChickenList[i].y >= 500:
            ChickenList[i].speedy = -ChickenList[i].speedy
        if ChickenList[i].hitbox.colliderect(valP1):
            pygame.event.post(pygame.event.Event(P1_HIT))
def ChickenStore():
    global numbchickens, numbstoredchickens, ChickenCatch
    for i in range(numbchickens):
        if valP2.colliderect(ChickenList[i].hitbox) and ChickenCatch == True:
            ChickenList[i].stored = True
            if ChickenList[i].stored == True:
                StoredChickens.append(ChickenList[i])
                numbstoredchickens += 1
                print(numbstoredchickens)
                ChickenCatch = False
        
def P2Shoot(P2bullets, valP2, event):
    for P2bullet in P2bullets:
        P2bullet.x += P2bulVEL
        if VRANKsheild.colliderect(P2bullet) or valP1.colliderect(P2bullet) or BROCKbike1.colliderect(P2bullet) or BROCKbike.colliderect(P2bullet):
            P2bullets.remove(P2bullet)
            if valP1.colliderect(P2bullet):
                pygame.event.post(pygame.event.Event(P1_HIT))
                explosion = Explosion(P2bullet.x,P2bullet.y)
                explosion_group.add(explosion)
        if P2bullet.x >= 800 or  P2bullet.x <= -10:
            P2bullets.remove(P2bullet)
    for P2bullet1 in P2bullets1:
        P2bullet1.x -= P2bulVEL
        if VRANKsheild.colliderect(P2bullet1) or valP1.colliderect(P2bullet1) or BROCKbike1.colliderect(P2bullet1) or BROCKbike.colliderect(P2bullet1):
            P2bullets1.remove(P2bullet1)
            if valP1.colliderect(P2bullet1):
                pygame.event.post(pygame.event.Event(P1_HIT))
                explosion = Explosion(P2bullet1.x,P2bullet1.y)
                explosion_group.add(explosion)
        if P2bullet1.x >= 800 or  P2bullet1.x <= -10:
            P2bullets1.remove(P2bullet1)
def P1Shoot(P1bullets, valP1, event):
    if LANEOVERLOAD == False:
        for P1bullet in P1bullets:
            P1bullet.x += P1bulVEL
            if valP2.colliderect(P1bullet) or VRANKsheild.colliderect(P1bullet) or BROCKbike1.colliderect(P1bullet) or BROCKbike.colliderect(P1bullet) or valLONE.colliderect(P1bullet):
                P1bullets.remove(P1bullet)
                if valP2.colliderect(P1bullet):
                    pygame.event.post(pygame.event.Event(P2_HIT))
                    explosion = Explosion(P1bullet.x,P1bullet.y)
                    explosion_group.add(explosion)
                if valLONE.colliderect(P1bullet):
                    pygame.event.post(pygame.event.Event(LONE_HIT))
            if P1bullet.x >= 800 or  P1bullet.x <= -10:
                P1bullets.remove(P1bullet)
        for P1bullet1 in P1bullets1:
            P1bullet1.x -= P1bulVEL
            if valP2.colliderect(P1bullet1) or VRANKsheild.colliderect(P1bullet1) or BROCKbike1.colliderect(P1bullet1) or BROCKbike.colliderect(P1bullet1) or valLONE.colliderect(P1bullet1):
                P1bullets1.remove(P1bullet1)
                if valP2.colliderect(P1bullet1):
                    pygame.event.post(pygame.event.Event(P2_HIT))
                    explosion = Explosion(P1bullet1.x,P1bullet1.y)
                    explosion_group.add(explosion)
                if valLONE.colliderect(P1bullet1):
                    pygame.event.post(pygame.event.Event(LONE_HIT))
            if P1bullet1.x >= 800 or  P1bullet1.x <= -10:
                P1bullets1.remove(P1bullet1)
    elif LANEOVERLOAD == True:
        for i in range(intLOVEbullets):

            if LOVEbullets[i].x > valP2.x:
                LOVEbullets[i].x = LOVEbullets[i].x - LOVEbullets[i].speed
            if LOVEbullets[i].x < valP2.x:
                LOVEbullets[i].x = LOVEbullets[i].x + LOVEbullets[i].speed
            if LOVEbullets[i].y > valP2.y:
                LOVEbullets[i].y = LOVEbullets[i].y - LOVEbullets[i].speed
            if LOVEbullets[i].y < valP2.y:
                LOVEbullets[i].y = LOVEbullets[i].y + LOVEbullets[i].speed
            if LOVEbullets[i].y == valP2.y and LOVEbullets[i].x == valP2.x:
                pygame.event.post(pygame.event.Event(P2_HIT))
                LOVEbullets.remove(LOVEbullets[i])

def LONEShoot(LONEbullets, valLONE, event):
    if left == True:
        LONEbulVEL = P2bulVEL *-1
    elif right == True:
        LONEbulVEL = P2bulVEL
    else:
        LONEbulVEL = P2bulVEL
    for LONEbullet in LONEbullets:
        LONEbullet.x += LONEbulVEL
        if VRANKsheild.colliderect(LONEbullet) or valP1.colliderect(LONEbullet) or BROCKbike1.colliderect(LONEbullet) or BROCKbike.colliderect(LONEbullet):
            LONEbullets.remove(LONEbullet)
            if valP1.colliderect(LONEbullet):
                pygame.event.post(pygame.event.Event(P1_HIT))
        if LONEbullet.x >= 800 or  LONEbullet.x <= -10:
            LONEbullets.remove(LONEbullet)

def grayscale():
    global BultimeBackground
    arr = cv2.imread('DOJO.jpg',0)  
    BultimeBackground = pygame.surfarray.make_surface(arr)

def DrawWindow(selVRANKDOJO, selVRANKCHURCH, KENbullets, P1bullets, current_time, cooldownJ2):
    screen.fill((BROWN))
    #Map Options
    global explosioncount
    if BULtime == True:
        screen.blit(CallumBackyard,(0,0))
    else:
        screen.blit(BACKGROUND, (0,0))
        
    P1healthtxt = Health_font.render('%i'%(P1_health), 5, WHITE)
    P2healthtxt = Health_font.render('%i'%(P2_health), 5, WHITE)
    screen.blit(HEART, (20, 5))
    screen.blit(HEART, (732, 5))
    screen.blit(P1healthtxt, (32, 10))
    screen.blit(P2healthtxt, (745, 10))
    for cls_Particle_ in particles:
        if cls_Particle_.lifetime > 0: #checking to see if the particles lifespan is 
            cls_Particle_.DrawParticles(screen) #using the draw method to draw each particle in the list
    if selGOOMBA == True:
        screen.blit(GOOMBA,(valGOOMBA.x,valGOOMBA.y))
        if current_time - cooldownG1 > 12000:
            screen.blit(RICKSbutton,(650, 8))
    if selVRANK == True:
        if current_time - cooldownV1 > 8000:
            screen.blit(burger,(75,8))
        screen.blit(VRANK,(valVRANK.x, valVRANK.y))
        if current_time - cooldownV2 > 12000:
            screen.blit(dogicon,(130,8))
    if selBROCK == True:
        screen.blit(BROCK,(valBROCK.x, valBROCK.y))
        if current_time - cooldownB1 > 8000:
            screen.blit(bikeicon,(75,8))
        if current_time - cooldownB2 > 8000:
            screen.blit(bikeicon,(110,8))
    if selJASE == True:
        if current_time - cooldownJ2 > 12000:
            screen.blit(jaseVAPE,(660,-20))
        screen.blit(JASE, (valJASE.x, valJASE.y))
        screen.blit(PERC,(JASEperc2.x, JASEperc2.y))
        screen.blit(PERC,(JASEperc1.x, JASEperc1.y))
        if tolBREAK == True:
            screen.blit(tol_text, (500, 10))
    if selCALLUM == True:
        if BULtime == True:
            screen.blit(WALNUT,(valCALLUM.x, valCALLUM.y))
            for i in range(numbchickens):
                if ChickenList[i].stored == False:
                    screen.blit(ChickenList[i].img, (ChickenList[i].x, ChickenList[i].y))
        else:
            screen.blit(CALLUM,(valCALLUM.x, valCALLUM.y))
        screen.blit(CALLUMROD,(CALLUMRODrect.x, CALLUMRODrect.y))
        if FISHING:
            pygame.draw.line(screen,(255,255,255),(valP1.x + (valP1.w/2), valP1.y +(valP1.h/2)),(CALLUMRODrect.x + 60,CALLUMRODrect.y),1)
        if current_time - cooldownC1 > 5000:
            screen.blit(callumROD,(680, 5))   
        if current_time - cooldownC2 > 120000:
            screen.blit(callumDOM,(630, 5)) 
    if selLANE == True:
        if LANEOVERLOAD == False:
            screen.blit(LANE,(valLANE.x,valLANE.y))
        else:
            screen.blit(CUTELANE,(valLANE.x,valLANE.y))
            for i in range(intLOVEbullets):
                screen.blit(LOVEbullets[i].img,(LOVEbullets[i].x, LOVEbullets[i].y))
    for P2bullet in P2bullets:
        screen.blit(bulletimg, (P2bullet))
        particles.append(cls_Particle(P2bullet.x + 10, P2bullet.y + 20, random.randrange(-3,3), random.randrange(-1,2), 4, (150,100,255),random.randint(5,20))) #defining the ships particles
    for P2bullet1 in P2bullets1:
        screen.blit(bullet1img, (P2bullet1))
        particles.append(cls_Particle(P2bullet1.x, P2bullet1.y + 20, random.randrange(-3,3), random.randrange(-1,2), 4, (150,100,255),random.randint(5,20))) #defining the ships particles
    for P1bullet in P1bullets:
        screen.blit(bulletimg, (P1bullet))
        particles.append(cls_Particle(P1bullet.x + 10, P1bullet.y + 20, random.randrange(-3,3), random.randrange(-1,2), 4, (150,100,255),random.randint(5,20))) #defining the ships particles
    for P1bullet1 in P1bullets1:
        screen.blit(bullet1img, (P1bullet1))
        particles.append(cls_Particle(P1bullet1.x, P1bullet1.y + 20, random.randrange(-3,3), random.randrange(-1,2), 4, (150,100,255),random.randint(5,20))) #defining the ships particles
    for LONEbullet in LONEbullets:
        if left == True:
            screen.blit(bullet1img,(LONEbullet))
        if right == True:
            screen.blit(bulletimg,(LONEbullet))
        else:
            screen.blit(bulletimg,(LONEbullet))
 
    screen.blit(BURGER, (VRANKsheild.x, VRANKsheild.y))
    screen.blit(BIKE2,(BROCKbike.x, BROCKbike.y))
    screen.blit(BIKE1,(BROCKbike1.x, BROCKbike1.y))
    screen.blit(VRANKdog,(VRANKdog1.x, VRANKdog1.y))
    screen.blit(VRANKdog,(VRANKdog2.x, VRANKdog2.y))
    screen.blit(VRANKdog,(VRANKdog3.x, VRANKdog3.y))
    screen.blit(VRANKdog,(VRANKdog4.x, VRANKdog4.y))
    screen.blit(LONE,(valLONE.x,valLONE.y))
    if ricks == True:
        screen.blit(KENricksimg,(valP2.x + 25,valP2.y + 50))
    explosion_group.draw(screen)
    explosion_group.update()
    SMOKE = pygame.transform.scale(SMOKEimg,(smoke_s, smoke_s1))
    screen.blit(SMOKE,(jaseSMOKE.x, jaseSMOKE.y))
    if P1_health <= 0:
        winnertext = TITLE_font.render("PLAYER 2 WINS", 5, WHITE)
        screen.blit(winnertext,(WIDTH/2 - 170, HEIGHT/2 - 30))
    if P2_health <= 0:
        winnertext = TITLE_font.render("PLAYER 1 WINS", 5, WHITE)
        screen.blit(winnertext,(WIDTH/2 - 170, HEIGHT/2 - 30))
    pygame.display.update()

    
        
#button variables

DOJO_button = Button(70, 200, DOJObutton, 1)
CHURCH_button = Button(320,200,CHURCHbutton, 1)
PLUMBING_button = Button(570,200,PLUMBINGbutton, 1)
JASE_button  = Button(405, 500, JASEbutton, 1)
CALLUM_button = Button(605, 500, CALLUMbutton, 1)
KEN_button  = Button(505, 500, KENbutton, 1)
VRANK_button  = Button(0, 500, VRANKbutton, 1)
BROCK_button  = Button(100, 500, BROCKbutton, 1)
LANE_button = Button(200, 500, LANEbutton, 1)


#body variables
explosion_group = pygame.sprite.Group()
pygame.display.set_caption("Vrank Fighters")
clock = pygame.time.Clock()
while MAPsel == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MAPsel = True
            CHAR2sel = True
            CHAR1sel = True
    pygame.event.get()
    clock.tick(24)
    screen.fill((116, 170, 173))
    screen.blit(TITLE, (WIDTH/2 - TITLE.get_width()/2, 50))
    screen.blit(titleDOJO,(85, 170))
    screen.blit(titleCHURCH,(285, 170))
    screen.blit(titlePLUMBING,(555, 170))
    if DOJO_button.DrawButton():
        selVRANKDOJO = True
        MAPsel = True
        BACKGROUND = DOJO
    if CHURCH_button.DrawButton():
        selVRANKCHURCH = True
        MAPsel = True
        BACKGROUND = CHURCH
    if PLUMBING_button.DrawButton():
        selVRANKPLUMBING = True
        MAPsel = True
        BACKGROUND = PLUMBING
    pygame.display.update()

while CHAR1sel == False or CHAR2sel == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CHAR1sel = True
            CHAR2sel = True
    pygame.event.get()
    clock.tick(24)
    screen.fill((116, 170, 173))
    pygame.draw.rect(screen, WHITE, pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT))
    screen.blit(CHARtitle, (WIDTH/2 - TITLE.get_width()/2, 50))   
    screen.blit(CHAR1title, (WIDTH/4 - TITLE.get_width()/2, 100))
    screen.blit(CHAR2title, (WIDTH/4 * 3 - TITLE.get_width()/2, 100))
    if VRANK_button.DrawButton():
        selVRANK = True
        selBROCK = False
        CHAR1sel = True
        selLANE = False
        run = True
    if JASE_button.DrawButton():
        selJASE = True
        selGOOMBA = False
        selCALLUM = False
        CHAR2sel = True
        run = True
    if KEN_button.DrawButton():
        selGOOMBA = True
        selJASE = False
        selCALLUM = False
        CHAR2sel = True
        run = True
    if CALLUM_button.DrawButton():
        selCALLUM = True
        selJASE = False
        selGOOMBA = False
        CHAR2sel = True
        run = True
    if LANE_button.DrawButton():
        selLANE = True
        selBROCK = False
        selVRANK = False
        CHAR1sel = True
        run = True
    if BROCK_button.DrawButton():
        selBROCK = True
        selVRANK = False
        selLANE = False
        CHAR1sel = True
        run = True
    pygame.display.update()
#character variables
if selVRANK == True:        
    valP1 = valVRANK
    velP1 = velVRANK
    P1_damage = 2
    P1_health = 150
    P1bullets = VRANKbullets
    P1bullets1 = VRANKbullets1
    P1bulVEL = VRANKbulVEL
if selLANE == True:
    velP1 = velLANE
    valP1 = valLANE
    P1_damage = 2
    P1_health = 150
    P1bullets = LANEbullets
    P1bullets1 = LANEbullets1
    P1bulvel = LANEbulVEL
if selBROCK == True:
    valP1 = valBROCK
    velP1 = velBROCK
    P1_health = 100
    P1_damage = 2
    P1bullets = BROCKbullets
    P1bullets1 = BROCKbullets1
    P1bulVEL = BROCKbulVEL
if selLANE == True:
    valP1 = valLANE
    velP1 = velLANE
    P1_health = 130
    P1bullets = LANEbullets
    P1bullets1 = LANEbullets1
    P1bulVEL = LANEbulVEL

    #PLAYER 2 CHARACERS   
     
if selGOOMBA == True:
    valP2 = valGOOMBA
    velP2 = velGOOMBA
    P2_health = 100
    P2_damage = 3
    P2bullets = KENbullets
    P2bullets1 = KENbullets1
    P2bulVEL = KENbulVEL
if selCALLUM == True:
    valP2 = valCALLUM
    velP2 = velCALLUM
    P2_health = 120
    P2_damage = 2
    P2bullets = CALLUMbullets
    P2bullets1 = CALLUMbullets1
    P2bulVEL = CALLUMbulVEL
if selJASE == True:
    valP2 = valJASE
    velP2 = velJASE
    P2_health = 120
    P2_damage = 2
    P2bullets = JASEbullets
    P2bullets1 = JASEbullets1
    P2bulVEL = JASEbulVEL

while run == True:
    pygame.event.get()
    clock.tick(24)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and FISHINGSTUN == False:
                P1bullet = pygame.Rect(valP1.x,valP1.y, 20, 20)
                P1bullets.append(P1bullet)
                pygame.mixer.Sound.play(pew_sound)
            if event.key == pygame.K_LSHIFT and FISHINGSTUN == False:
                if LANEOVERLOAD == False:
                    P1bullet1 = pygame.Rect(valP1.x,valP1.y, 20, 20)
                    P1bullets1.append(P1bullet1)
                    pygame.mixer.Sound.play(pew_sound)
                elif LANEOVERLOAD == True:
                    intLOVEbullets += 1
                    LOVEbullets.append(cls_LANEHEART(valP1.x, valP1.y))
            if event.key == pygame.K_RCTRL:
                if FISHING:
                    REEL = True
                    fishingstun_time = pygame.time.get_ticks()
                    pygame.mixer.Sound.play(REELIN_sound)
                else:
                    P2bullet = pygame.Rect(valP2.x,valP2.y, 20, 20)
                    P2bullets.append(P2bullet)
                    if selGOOMBA == True:
                        pygame.mixer.Sound.play(k808_sound)
                    else:
                        pygame.mixer.Sound.play(pew_sound)
            if event.key == pygame.K_RSHIFT:
                P2bullet1 = pygame.Rect(valP2.x,valP2.y, 20, 20)
                P2bullets1.append(P2bullet1)
                if selGOOMBA == True:
                    pygame.mixer.Sound.play(k808_sound)
                else:
                    pygame.mixer.Sound.play(pew_sound)
    #CHARACTER ABILITIES
            # VRANK ABILITIES
            if selVRANK == True:
                if event.key == pygame.K_q and current_time - cooldownV1 > 8000 :
                    cooldownV1 = pygame.time.get_ticks()
                    VRANKsheild = pygame.Rect(valP1.x,valP1.y - VRANKsheild.h/2 + 20, 120, 250)
                    if VRANKsheild.y < 0:
                        VRANKsheild.y = 1
                    if VRANKsheild.y > HEIGHT - VRANKsheild.h:
                        VRANKsheild.y = HEIGHT - VRANKsheild.h - 1
                elif event.key == pygame.K_q and valP1.colliderect(VRANKsheild):
                    cooldownV1 = pygame.time.get_ticks() + 6000
                    VRANKsheild.x = 900
                    P1_health += 30
                    pygame.mixer.Sound.play(MUNCH_sound)
                if event.key == pygame.K_e and current_time - cooldownV2 > 13000:
                    pygame.mixer.Sound.play(EAGLE_sound)
                    cooldownV2 = pygame.time.get_ticks()
                    collide = False
                    VRANKdog1 = pygame.Rect(0,100,VRANKdogrect.w,VRANKdogrect.h)
                    VRANKdog2 = pygame.Rect(0,300,VRANKdogrect.w,VRANKdogrect.h)
                    VRANKdog3 = pygame.Rect(0,500,VRANKdogrect.w,VRANKdogrect.h)
            
            # BROCK ABILITIES
            if selBROCK == True:
                if event.key == pygame.K_q:
                    if current_time - cooldownB1 > 8000 or current_time - cooldownB2 > 8000:
                        BROCKbol = True
                        brockcharge += 1
                        pygame.mixer.Sound.play(Dirtbike_sound)
                        collide = False
                        valBIKE_x, valBIKE_y = valP1.x, valP1.y
                        BROCKbike = pygame.Rect(valBIKE_x, valBIKE_y + 50, 120, 80)
                        BROCKbike1.x = 1500
                    if valP1.x <= 0:
                        valP1.x = 0
                if event.key == pygame.K_e:
                    if current_time - cooldownB2 > 8000 or current_time - cooldownB1 > 8000:
                        BROCKbol = True
                        brockcharge += 1
                        pygame.mixer.Sound.play(Dirtbike_sound)
                        collide = False
                        valBIKE1_x, valBIKE1_y = valP1.x, valP1.y
                        BROCKbike1 = pygame.Rect(valBIKE1_x, valBIKE1_y + 50, 120, 80)
                        BROCKbike.x = -500
                    if valP1.x <= 0:
                        valP1.x = 0
            #LANE ABILITIES
            if selLANE == True:
                if event.key == pygame.K_q and current_time - cooldownL1 > 18000:
                    cooldownL1 = pygame.time.get_ticks()
                    LANEOVERLOAD = True

            # JASE ABILITIES
            if selJASE == True:
                if event.key == pygame.K_SLASH and valP2.colliderect(JASEperc1) and tolJ1 != 3:
                    JASEperc1 = pygame.Rect(random.randint(0,WIDTH),random.randint(0,HEIGHT), 30, 30)
                    P2_health -= 10
                    P2_damage += 1
                    tolJ1 = random.randint(1,3)
                    cooldownJ1 = pygame.time.get_ticks()
                if event.key == pygame.K_SLASH and valP2.colliderect(JASEperc2) and tolJ1 != 3:
                    JASEperc2 = pygame.Rect(random.randint(0,WIDTH),random.randint(0,HEIGHT), 30, 30)
                    P2_health -= 10
                    P2_damage += 1
                    tolJ1 = random.randint(1,3)
                    cooldownJ1 = pygame.time.get_ticks()
                if event.key == pygame.K_PERIOD and current_time - cooldownJ2 > 9000:
                    smoke = True
                    smoke_Y = valP2.y
                    cooldownJ2 = pygame.time.get_ticks()
                    cooldownJ3 = pygame.time.get_ticks()
                    smoke_s, smoke_s1, smoke_x, smoke_y = 30, 20, valP2.x, valP2.y
                    jaseSMOKE = pygame.Rect(smoke_x, smoke_y,smoke_s, smoke_s1)
            #GOOMBA ABILITIES
            if selGOOMBA == True:
                if event.key == pygame.K_SLASH and current_time - cooldownG1 > 12000:
                    ricks = True
                    cooldownG1 = pygame.time.get_ticks()
                    KENrick = pygame.Rect(valP2.x + 25, valP2.y + 50, 40,40)
                    velP2 += 20
                if event.key == pygame.K_PERIOD and current_time - cooldownG2 > 15000:
                    if valP2.y > HEIGHT - 160:
                        valLONE = pygame.Rect(valP2.x,valP2.y - 100,GOOMBAwidth,GOOMBAheight)
                    else:
                        valLONE = pygame.Rect(valP2.x,valP2.y + 100,GOOMBAwidth,GOOMBAheight)
                    lone = True
            #CALLUM ABILITIES
            if selCALLUM == True:
                if event.key == pygame.K_SLASH and current_time - cooldownC1 > 5000:
                    CALLUMRODrect = pygame.Rect(valP2.x + 30,valP2.y - 85, 30,70)
                    FISHING = True
                if event.key == pygame.K_PERIOD and current_time - cooldownC2 > 120000:
                    BULtime = True
                    grayscale()
                    ChickenSpawn()
                    pygame.mixer.Sound.play(FarmSong)
                    cooldownC2 = pygame.time.get_ticks()
                elif event.key == pygame.K_PERIOD and BULtime == True:
                    ChickenCatch = True

        #VARIABLE SETTING / things that need to be out of the for loop
    if selVRANK == True:
        if VRANKdog1.x <= WIDTH and VRANKdog1.x > -1:
            VRANKdog1.x += 30
            VRANKdog2.x += 30
            VRANKdog3.x += 30
        if VRANKdog1.x >= WIDTH:
            VRANKdog1.x = -500
            VRANKdog2.x = -500
            VRANKdog3.x = -500

    if selJASE == True:
        if valP1.colliderect(jaseSMOKE):
            P1_health -= 0.34
        if smoke_s < 500 and smoke == True:
            smoke_s += 10
        if smoke_s1 < 350 and smoke == True:
            smoke_s1 += 10
            jaseSMOKE = pygame.Rect(smoke_x, smoke_y,smoke_s, smoke_s1)
        if smoke_Y > HEIGHT/2 and jaseSMOKE.y > 20:
            jaseSMOKE.y -= 10
        if current_time - cooldownJ3 > 6000 and jaseSMOKE.x > 0:
            smoke = False
            smoke_s -= 10
            smoke_s1 -= 10
            if smoke_s < 40 or smoke_s1 < 40:
                smoke = True
                jaseSMOKE.x = -500           
        if tolJ1 == 3:
            tolBREAK = True
            P2_damage = 3
            if current_time - cooldownJ1 > 12000:
                tolJ1 = 2
                tolBREAK = False

    if selBROCK == True:
        if BROCKbike.x > 0:
            BROCKbike.x -= 30
            valP1.x = BROCKbike.x + 50
            valP1.y = BROCKbike.y - 30
        if BROCKbike1.x < WIDTH - BROCKbike1.w:
            BROCKbike1.x += 30
            valP1.x = BROCKbike1.x + 25
            valP1.y = BROCKbike1.y - 30
        if brockcharge == 1 and BROCKbol == True:
            cooldownB1 = pygame.time.get_ticks()
            BROCKbol = False
        if brockcharge == 2 and BROCKbol == True:
            cooldownB2 = pygame.time.get_ticks()
            BROCKbol = False
        if brockcharge >= 2:
            brockcharge = 0
        if collide == False:
            if BROCKbike.colliderect(valP2):
                P2_health -= 30
                collide = True
            if BROCKbike1.colliderect(valP2):
                P2_health -= 30
                collide = True
            if VRANKdog1.colliderect(valP2):
                P2_health -= 15
                collide = True
            if VRANKdog2.colliderect(valP2):
                P2_health -= 15
                collide = True
            if VRANKdog3.colliderect(valP2):
                P2_health -= 15
    
    if selGOOMBA == True:
        if left == True:
            KENricksimg = RICK1
        if right == True:
            KENricksimg = RICK
        if ricks == True:
            KENrick = pygame.Rect(valP2.x + 25, valP2.y + 50, 40,40)
        elif ricks == False:
            KENrick = pygame.Rect(-500,-500 + 50, 40,40)
        if current_time - cooldownG1 > 5000 and KENrick.x > 0:
            ricks = False
            velP2 -= 20
        if lone == True:
            valLONE.x = valP2.x
            if valLONE.y > HEIGHT - valLONE.h - velP2:
                loneswitch = False
                print("lone false")
            if valLONE.y < 0 + valLONE.h + velP2:
                loneswitch = True
                print("lone true")
            if loneswitch == False:
                if valLONE.y >= valP2.y - 100:
                    valLONE.y -= velP2

            if loneswitch == True:
                if valLONE.y <= valP2.y + 100:
                    valLONE.y += velP2        
            LONEbullet = pygame.Rect(valLONE.x,valLONE.y, 20, 20)
            if current_time - LONEbultime > 600:
                LONEbullets.append(LONEbullet)
                LONEbultime = pygame.time.get_ticks()
            LONEShoot(LONEbullets, valLONE, event)
    
    if selCALLUM == True:
        if FISHING:
            CALLUMRODrect = pygame.Rect(valP2.x + 30,valP2.y - 85, 30,70)
            if REEL:
                CallumFishing(valP1, valP2)
                cooldownC1 = pygame.time.get_ticks()
        elif FISHING == False:
            CALLUMRODrect = pygame.Rect(-500,-500, 30,70)
            REEL = False
            pygame.mixer.Sound.stop(REELIN_sound)
        if BULtime == True and current_time - cooldownC2 > 15000:
            BULtime = False
            pygame.mixer.Sound.stop(FarmSong)
        elif BULtime == True:
            ChickenMove()
            ChickenStore()
        #print(numbstoredchickens)
    P1Movement()
    P2Movement()
    P2Shoot(P2bullets, valP2, event)
    if FISHINGSTUN == False:
        P1Shoot(P1bullets, valP1, event)
    else:
        if current_time - fishingstun_time > 2000:
            FISHINGSTUN = False
    for event in pygame.event.get():
        if event.type == P2_HIT:
            if BULtime == True:
                P2_health -= P1_damage/2
            else:
                P2_health -= P1_damage
        elif event.type == P1_HIT:
            if BULtime == True:
                P1_health -= 1
            else:
                P1_health -= P2_damage
        elif event.type == LONE_HIT:
            LONEhealth -= P1_damage
            
    DrawWindow(selVRANKDOJO, selVRANKCHURCH, P2bullets, P1bullets, current_time, cooldownJ2)
    if P1_health <= 0:
        import RESTART
        run = False
        RESTART.Open()
    if P2_health <= 0:
        import RESTART
        RESTART.Open()
        run = False
    if LONEhealth <= 0:
        valLONE.y -= 20
        cooldownG2 = pygame.time.get_ticks()
        lone = False
        if valLONE.y < -100:
            valLONE.x = -500
            LONEhealth = 20
    if lone == False:
        for LONEbullet in LONEbullets:
            LONEbullets.remove(LONEbullet)


pygame.quit()
quit()