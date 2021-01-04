import pygame
from pygame.locals import *
from sys import exit
#设置屏幕大小
pygame.init()
SCREEN_SIZE=(640,480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

#设置字体及其大小
font = pygame.font.SysFont("arial",16)
font_height = font.get_linesize()
event_text = []


while True :
#等待时间的进行。并向事件队列里添加数据
    event = pygame.event.wait()
    event_text.append(str(event))

    event_text=event_text[int(-SCREEN_SIZE[1]/font_height):]

#退出
    if event.type ==QUIT:
        exit()
        
    screen.fill((255, 255, 255))
#屏幕上信息的显示
    y = SCREEN_SIZE[1]-font_height
    for text in reversed(event_text):
        screen.blit(font.render(text, True ,(0,0,0)),(0,y))
        y-=font_height

    pygame.display.update()
