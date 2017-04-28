#Snake game

#imports
import pygame
import sys
import time
import random

#initializing pygame
check = pygame.init();
if check[1]>0:
    print("Something error. Quiting...")
else:
    print("Initilized successfuflly")

#Creating play surface
PlaySurface = pygame.display.set_mode((720, 420))
pygame.display.set_caption("Snake Game")

#Colors
red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
acolor = pygame.Color(230, 230, 230)

#PFS controller
fps = pygame.time.Clock()

#Variables
SnakePos = [100, 50]
SnakeBody = [[100, 50], [90, 50], [80, 50]]

FoodPos = [random.randrange(1,72)*10, random.randrange(1,42)*10]
FoodSpawn = True

Direction = 'Right'
ChangeTo = Direction

Score = 0

#Game Over
def gameover():
    Font = pygame.font.SysFont('monaco', 72)
    TextSurface = Font.render('GAME OVER!', False, red)
    rectangle = TextSurface.get_rect()
    rectangle.midtop = (360, 220)
    PlaySurface.blit(TextSurface, rectangle)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

#Display score
def score(Score):
    Font = pygame.font.SysFont('Terminal', 250)
    TextSurface = Font.render(str(Score), False, acolor)
    rectangle = TextSurface.get_rect()
    rectangle.midtop = (330, 150)
    PlaySurface.blit(TextSurface, rectangle)
    pygame.display.flip()

#main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ChangeTo = 'LEFT'
            if event.key == pygame.K_RIGHT:
                ChangeTo = 'RIGHT'
            if event.key == pygame.K_UP:
                ChangeTo = 'UP'
            if event.key == pygame.K_DOWN:
                ChangeTo = 'DOWN'

    #direction validation
    if ChangeTo == 'RIGHT' and not Direction == 'LEFT':
        Direction = 'RIGHT'
    if ChangeTo == 'LEFT' and not Direction == 'RIGHT':
        Direction = 'LEFT'
    if ChangeTo == 'UP' and not Direction == 'DOWN':
        Direction = 'UP'
    if ChangeTo == 'DOWN' and not Direction == 'UP':
        Direction = 'DOWN'

    #update snake position
    if Direction == 'RIGHT':
        SnakePos[0]+=10
    if Direction == 'LEFT':
        SnakePos[0]-=10
    if Direction == 'UP':
        SnakePos[1]-=10
    if Direction == 'DOWN':
        SnakePos[1]+=10

    #snake body mechanism
    SnakeBody.insert(0,list(SnakePos))
    if SnakePos[0] == FoodPos[0] and SnakePos[1] == FoodPos[1]:
        Score += 1
        FoodSpawn = False
    else:
        SnakeBody.pop()

    #Food Spawn
    if FoodSpawn == False:
        FoodPos = [random.randrange(1,72)*10, random.randrange(1,42)*10]
    FoodSpawn = True

    #Background color
    PlaySurface.fill(white)
    score(Score)

    #Snake Body
    for pos in SnakeBody:
        pygame.draw.rect(PlaySurface, red, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(PlaySurface, green, pygame.Rect(FoodPos[0], FoodPos[1], 10, 10))
    pygame.display.flip() #for updating new frame

    #if snake touch the border
        #then game over
    if SnakePos[0] < 0 or  SnakePos[0] > 720:
        gameover()
    if SnakePos[1] < 0 or SnakePos[1] > 420:
        gameover()

    #Frame refresh speed
    fps.tick(15)