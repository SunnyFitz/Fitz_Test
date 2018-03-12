# -*- coding: UTF-8 -*-

import pygame
import sys
from pygame.locals import *

#初始化
pygame.init()
#创建窗口
size = width,height = 800 ,500 
speed = [-2,1]
bg = (255,255,255)
screen = pygame.display.set_mode(size)
#设置标题
pygame.display.set_caption("This is a test")
#图片
bird = pygame.image.load("bird.jpg")
#获取图片位置
position = bird.get_rect()
bird = pygame.transform.flip(bird,True,False)
#刷新帧数
clock = pygame.time.Clock()
l_head = bird
r_head = pygame.transform.flip(bird,True,False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1,0]
                bird = l_head
            if event.key == K_RIGHT:
                speed = [1,0]
                bird = r_head
            if event.key == K_UP:
                speed = [0,-1]
            if event.key == K_DOWN:
                speed = [0,1]
            
    position = position.move(speed)
    if position.left < 0 or position.right > width:
        bird = pygame.transform.flip(bird,True,False)
        speed[0] = -speed[0] 
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    screen.fill(bg)
    screen.blit(bird,position)
    pygame.display.flip() 
    #pygame.time.delay(10)
    clock.tick(100)
