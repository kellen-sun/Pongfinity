import pygame, sys, random

pygame.init()
pygame.display.set_caption('Pongfinity')
dis = pygame.display.set_mode((1600, 900))
dis.fill((0,0,0))

gameOver = False

paddlex1, paddley1 = 30, 360
paddlex2, paddley2 = 1540, 360
paddlesizex, paddlesizey = 30, 180
ballx, bally, ballsize = 800, 450, 25
white = (255, 255, 255)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #Currently requires multiple clicks to keep the paddle moving smoothly
            if event.key == pygame.K_w and paddley1>0:
                paddley1 -= 50
            if event.key == pygame.K_s and paddley1<720:
                paddley1 += 50
            if event.key == pygame.K_UP and paddley2>0:
                paddley2 -= 50
            if event.key == pygame.K_DOWN and paddley2<720:
                paddley2 +=50
    dis.fill((0,0,0))
    pygame.draw.rect(dis, white, pygame.Rect(paddlex1, paddley1, paddlesizex, paddlesizey))
    pygame.draw.rect(dis, white, pygame.Rect(paddlex2, paddley2, paddlesizex, paddlesizey))
    pygame.draw.circle(dis, white, (ballx, bally), ballsize)
    pygame.time.Clock().tick(30)
    pygame.display.flip()