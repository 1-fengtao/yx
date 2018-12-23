import pygame,random,sys

# 导入pygame(游戏中的操作)中所有的常量
from pygame.locals import *


# 字体的对象,位置(X,Y), 绘制的内容

# 第一步render()绘制内容
# 第二步blit()绘制
# 第三步创建窗口
# 第四步Font()将内容输出到界面上

# 1.定义一个输出字体的函数
def print_text(font,x,y,text,color=(255,255,255)):
# 1.1render()绘制内容
    # True的作用:抗锯齿,提高图像的质量
    imgtext = font.render(text,True,color)
    # 打开窗口
    screen.blit(imgtext,(x,y))
# 1.2 初始化pygame()
pygame.init()
# 1.3 创建一个窗口
screen = pygame.display.set_mode((600,500))

# 1.4创建一个标题
pygame.display.set_caption('接小球')

# 1.5 输出 参数1:字体 参数2: 字体大小
font1 = pygame.font.Font(None,24)

# 1.6 隐藏或显示鼠标光标  False:隐藏
pygame.mouse.set_visible(False)

# 1.7 设置元素的颜色  字体:白  挡板:红 小球:黄  背景:蓝
white= 255,255,255
red = 220,50,50
yellow = 230,230,50
blue = 0,0,100

# 1.8 玩的次数(有几条命)
lives = 3
# 分数
score = 0

# 1.9 游戏结束的标记,鼠标点击的位置,初始化挡板的位置,小球的位置,速度变量
game_ocer = True
mouse_x = mouse_y = 0
# 初始化挡板的位置
pos_x = 300
pos_y = 460
# 小球的初始位置
bomb_x = random.randint(0,500)
bomb_y = -80
vel_y =1

# 2 循环中创建一个事件处理
while True:
    # pygame.event.get() 获取pygane中的事件
    for event in pygame.event.get():
        # 如果事件是退出
        if event.type == QUIT:
            # 退出
            sys.exit()
            # 如果事件是鼠标的运动
        elif event.type == MOUSEMOTION:
            # event.pos 鼠标的位置
            mouse_x,mouse_y = event.pos
            # 如果事件是鼠标的抬起
        elif event.type == MOUSEBUTTONUP:
            if game_ocer:
                # 结束游戏,并初始化命数和得分
                game_ocer =False
                lives = 3
                score = 0
    # 2.1 获得所有键盘按键的状态
    keys = pygame.key.get_pressed()
#     2.2 如果 我的事件是Esc,那么就退出
    if keys[K_ESCAPE]:
        sys.exit()
    # 填充窗口背景颜色
    screen.fill(blue)

    if game_ocer: #False
        print_text(font1,100,200,'<CLICK TO PLAY>')
    else:
#         没有结束就让小球动起来,通过速度变量改变垂直方向的值
        bomb_y += vel_y
#         思考:分析什么情况下接到了小球
#         屏幕的高度是500,小球
        # 没有接到  生成小球,命数减一
        if bomb_y>500:
            bomb_x = random.randint(0,500)
            bomb_y = -50
            lives -= 1
            if lives ==0:
                game_ocer = True
        # 接住了 加分数,生成小球
        elif bomb_y > pos_y:
            if bomb_x >pos_x and bomb_x < pos_x +120:
                # 分数加10
                score += 10
                # 重新生成小球
                bomb_x = random.randint(0,500)
                bomb_y = -50
#         绘制小球
        pygame.draw.circle(screen,yellow,(bomb_x,int(bomb_y)),30,0)
        # 2.3 挡板位置的判断
        # 挡板的位置等于鼠标的位置
        pos_x = mouse_x
# 当鼠标位置超出窗口时,归零
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500:
            pos_x = 500
        # 2.4  绘制挡板
        pygame.draw.rect(screen,red,(pos_x,pos_y,120,40),0)
    # 2.5 输出我的生命值
    print_text(font1,0,0,'LIVES:'+str(lives))

    # 2.6 输出我们的得分
    print_text(font1,500,0,'SCORE:'+str(score))

    # 2.7 更新显示
    pygame.display.update()