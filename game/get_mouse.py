# -*- coding: UTF-8 -*-

import pygame
import sys

#初始化
pygame.init()
#创建窗口
size = width,height = 800 ,500
bg = (0,0,0)
screen = pygame.display.set_mode(size)
#设置标题
pygame.display.set_caption("This is a test")

event_texts = []
font = pygame.font.Font(None,20)
line_height = font.get_linesize()
position = 0
screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.blit(font.render(str(event),True,(0,255,0)),(0,position))
        #print(font.render(str(event),True,(0,255,0)),(0,position))
        position += line_height
        if position > height:
            position = 0
            screen.fill(bg)
        pygame.display.flip()
