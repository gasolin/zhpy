#coding=utf-8
import sys, pygame
p0 = p1,p2=320,240
p3 = [2,2]
p4 = 255,255,255
p5 = pygame.display.set_mode(p0)
p6 = pygame.image.load("pygame_icon.bmp")
p7 = p6.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    p7 = p7.move(p3)
    if p7.left < 0 or p7.right > p1:
        p3[0] = -p3[0]
    if p7.top < 0 or p7.bottom > p2:
        p3[1] = -p3[1]

    p5.fill(p4)
    p5.blit(p6,p7)
    pygame.display.flip()