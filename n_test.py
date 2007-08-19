#coding=utf-8
import sys, pygame
size = width,height=320,240
speed = [2,2]
white = 255,255,255
screen = pygame.display.set_mode(size)
ball = pygame.image.load("pygame_icon.bmp")
ballrect = ball.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(white)
    screen.blit(ball,ballrect)
    pygame.display.flip()