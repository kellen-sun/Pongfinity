import pygame, sys, random, math

pygame.init()
pygame.display.set_caption('Pongfinity')
pygame.font.init()
sizex, sizey = 1600, 900
black = (0,0,0)
dis = pygame.display.set_mode((sizex, sizey))
dis.fill(black)

gameOver = False
paddlex1, paddley1 = 30, 360
paddlex2, paddley2 = 1540, 360
paddlesizex, paddlesizey = 30, 180
ballx, bally, ballsize = 800, 450, 25
speed = 25
point1 = 0
point2 = 0
angle = random.randint(0, 359)
speedx, speedy = speed*math.cos(math.radians(angle)), speed*math.sin(math.radians(angle))
white = (255, 255, 255)
font = pygame.font.SysFont('FreeMono, Monospace', 60)


def randombounce(sx, sy):
    global speed
    angle = math.atan2(sx,sy)
    dangle = random.uniform(-0.08, 0.08)
    angle += dangle
    y = speed*math.cos(angle)
    x = speed*math.sin(angle)
    return x, y

while not gameOver:
    for event in pygame.event.get():
        #check for input
        if event.type == pygame.QUIT:
            sys.exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] and paddley1>=0:
        paddley1-= 10
    if pressed[pygame.K_s] and paddley1<=720:
        paddley1 += 10
    if pressed[pygame.K_UP] and paddley2>=0:
        paddley2 -= 10
    if pressed[pygame.K_DOWN] and paddley2<=720:
        paddley2 += 10
    
    #move actors and bounce off walls
    if ballx < ballsize or ballx+ballsize > sizex:
        speedx, speedy = randombounce(-speedx, speedy)
    if bally < ballsize or bally+ballsize > sizey:
        speedx, speedy = randombounce(speedx, -speedy)
    ballx += speedx
    bally += speedy

    #bounce on paddles
    if ballx-ballsize<paddlex1+paddlesizex and paddley1+paddlesizey>bally>paddley1:
        speedx, speedy = randombounce(-speedx, speedy)
    if ballx+ballsize>paddlex2 and paddley2+paddlesizey>bally>paddley2:
        speedx, speedy = randombounce(-speedx, speedy)

    #points and scoring
    if ballx-ballsize<0:
        point2 += 1
        angle = random.randint(0, 359)
        ballx, bally, ballsize = 800, 450, 25
        speedx, speedy = speed*math.cos(math.radians(angle)), speed*math.sin(math.radians(angle))
    if ballx+ballsize>sizex:
        point1 += 1
        ballx, bally, ballsize = 800, 450, 25
        angle = random.randint(0, 359)
        speed+=1
        speedx, speedy = speed*math.cos(math.radians(angle)), speed*math.sin(math.radians(angle))

    #redraw actors
    dis.fill((0,0,0))
    pygame.draw.rect(dis, white, pygame.Rect(paddlex1, paddley1, paddlesizex, paddlesizey))
    pygame.draw.rect(dis, white, pygame.Rect(paddlex2, paddley2, paddlesizex, paddlesizey))
    pygame.draw.circle(dis, white, (ballx, bally), ballsize)
    dis.blit(font.render(str(point1), False, white), (sizex//2-60, 0))
    dis.blit(font.render(str(point2), False, white), (sizex//2+60, 0))
    pygame.time.Clock().tick(30)
    pygame.display.flip()