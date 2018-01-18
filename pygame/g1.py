#!/usr/bin/env python
# coding=utf-8
import sys,pygame
pygame.init()

size = width,height = 320,240
# print(type(size))
speed= [2,2]
black = 0,0,0

ball = pygame.image.load("ball.jpg")
ball = pygame.transform.scale(ball,(32,32))
ballrect = ball.get_rect()
print(ballrect)

screen = pygame.display.set_mode(size)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()

    print(ballrect)
    ballrect = ballrect.move(speed)
    print(ballrect)
    if ballrect.left < 0 or ballrect.left +ballrect.width > width:
        speed[0] = - speed[0]

    if ballrect.top < 0 or ballrect.top+ballrect.height > height:
        speed[1] = - speed[1]
    screen.fill(black)
    
    screen.blit(ball,ballrect)
    pygame.display.flip()
    pygame.time.wait(10)
