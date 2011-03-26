#coding=utf-8
import sys, pygame
p_5927_5c0f_v = p_5bec_v,p_9577_v=320,240
p_901f_5ea6_v = [2,2]
p_984f_8272_v = 255,255,255
p_87a2_5e55_v = pygame.display.set_mode(p_5927_5c0f_v)
p_7269_9ad4_v = pygame.image.load("pygame_icon.bmp")
p_7269_9ad4_908a_754c_v = p_7269_9ad4_v.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    p_7269_9ad4_908a_754c_v = p_7269_9ad4_908a_754c_v.move(p_901f_5ea6_v)
    if p_7269_9ad4_908a_754c_v.left < 0 or p_7269_9ad4_908a_754c_v.right > p_5bec_v:
        p_901f_5ea6_v[0] = -p_901f_5ea6_v[0]
    if p_7269_9ad4_908a_754c_v.top < 0 or p_7269_9ad4_908a_754c_v.bottom > p_9577_v:
        p_901f_5ea6_v[1] = -p_901f_5ea6_v[1]

    p_87a2_5e55_v.fill(p_984f_8272_v)
    p_87a2_5e55_v.blit(p_7269_9ad4_v,p_7269_9ad4_908a_754c_v)
    pygame.display.flip()