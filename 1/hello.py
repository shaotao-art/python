from sys import exit
from pygame.locals import *
import pygame

#图片位置声明
background_image_filename = './1/sushiplate.jpg'
mouse_image_filename = './1/fugu.png'

#pygame的初始化
pygame.init()
#设置窗口
#pygame.display.set_mode（resolution =（0,0），flags = 0，depth = 0）  flag参数   depth 颜色深度，不需要自己设置
screen = pygame.display.set_mode((640, 480),RESIZABLE)
#设置窗口的标题
pygame.display.set_caption('hello world')


#预先加载各种图片
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()



#游戏主函数
while True:
    #监听屏幕事件 并判断退出
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    #实在的在界面上画出背景图片
    screen.blit(background, (0, 0))

    
    x, y = pygame.mouse.get_pos()

    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    #实在的在界面上画出鼠标的图片
    screen.blit(mouse_cursor, (x,y ))

    #随着鼠标的移动不断更新显示的图片
    pygame.display.update()

