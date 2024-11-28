# Brayden Paterson
# 2022-10-18
# Number counter
# this is my program for pygame testing

import pygame # loads the pygame into memory
pygame.init() # get the game running
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# **** VARIABLES ****
bolRUN = True
win = False
rec_sx = 90
rec_sy = 90
step_x = 7
step_y = 7
cir_S = 15
playerCOL = (200,255,0)
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
scoretxt = pygame.font.SysFont('Dark Stone', 40)
player1score = 0 
player2score = 0
valRECT2 = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15,30,30)
valCIR2 = pygame.Rect(10,HEIGHT/2,10, 100)
valCIR3 = pygame.Rect(WIDTH - 20,HEIGHT/2,10, 100)
VRANKimg = pygame.image.load('VRANKT.jpg')
VRANKball = pygame.transform.scale(VRANKimg,(30,30))
resTXT = pygame.font.SysFont('Dark Stone', 60)
resTEXT = resTXT.render('HIT R TO RESTART', 5, WHITE)
strWINNER = ("")
# **** CLASSES ****

# **** FUNCTIONS ****

def MoveRect(valCIR2, valCIR3):
    global valRECT2, step_x, step_y
    if valRECT2.y <= 0 or valRECT2.y >= HEIGHT - valRECT2.w:
        step_y = step_y*-1
    collide1 = valRECT2.colliderect(valCIR2)
    if collide1:
        valRECT2.x += 15 + step_x
        if step_x < 20:
            step_x = step_x*-1.05
    collide2 = valRECT2.colliderect(valCIR3)
    if collide2:
        valRECT2.x -= 15 - step_x
        if step_x < 20:
            step_x = step_x*-1.05

    valRECT2.x = valRECT2.x + step_x
    valRECT2.y = valRECT2.y + step_y
    screen.blit(VRANKball, (valRECT2))
        
# **** PROGRAM ****

pygame.display.set_caption("PYGAME INTRO")
while bolRUN == True:
    screen.fill((BLACK))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bolRUN = False
#*** KEY PRESSES ****
        if event.type == pygame.KEYDOWN:
            if win == True:
                if event.key == pygame.K_r:
                    player1score = 0
                    player2score = 0
                    step_x = 7
                    step_y = 7
                    win = False
    keys_pressed = pygame.key.get_pressed()            
    if keys_pressed[pygame.K_w]:
                valCIR2.y -= 20
    elif keys_pressed[pygame.K_s]:
                valCIR2.y += 20
    if keys_pressed[pygame.K_UP]:
                valCIR3.y -= 20
    elif keys_pressed[pygame.K_DOWN]:
                valCIR3.y += 20
# BARRIERS
    if valRECT2.x >= WIDTH - 15:
        step_x = 5
        step_y = 5
        player1score += 1
        valRECT2.x = WIDTH/2
        valRECT2.y = HEIGHT/2
        if player1score == 10:
            step_x = 0
            step_y = 0
            strWINNER = ("PLAYER 1 WINS")
            winTXT = resTXT.render('%s'%(strWINNER), 5, WHITE)
            win = True

    elif valRECT2.x <= 5:
        step_x = 5
        step_y = 5
        player2score += 1
        valRECT2.x = WIDTH/2
        valRECT2.y = HEIGHT/2
        if player2score == 10:
            step_y = 0
            step_x = 0
            strWINNER = ("PLAYER 2 WINS")
            winTXT = resTXT.render('%s'%(strWINNER), 5, WHITE)
            win = True


#**** DRAWS ****

    pygame.time.delay(50)
    pygame.draw.rect(screen, BLUE, pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT))
    MoveRect(valCIR2, valCIR3)
    P1scoretxt = scoretxt.render('%s'%(player1score), 5, WHITE)
    P2scoretxt = scoretxt.render('%s'%(player2score), 5, WHITE)
    screen.blit(P2scoretxt,(WIDTH - 40, 50))
    screen.blit(P1scoretxt,(20, 50))
    pygame.draw.rect(screen, BLUE, valCIR2)
    pygame.draw.rect(screen, BLUE, valCIR3)
    if win == True:
        screen.blit(resTEXT,(WIDTH/2 - 185, HEIGHT/2- 20))
        screen.blit(winTXT,(WIDTH/2 - 140, HEIGHT/2- 80))

        #pygame.draw.circle(screen,(playerCOL),(cir_X,cir_Y),cir_S)    
    pygame.display.flip()



quit()
