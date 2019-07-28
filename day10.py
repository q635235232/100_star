import tkinter
import tkinter.messagebox
import pygame
from enum import Enum, unique
from math import sqrt
from random import randint


def main1():
    flag = True

    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello world!') \
            if flag else ('blue', 'Goodbye,world!')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    top = tkinter.Tk()
    top.geometry('240x160')
    top.title('小游戏')
    label = tkinter.Label(top, text='Hello world!', font='Arial-32', fg='red')
    label.pack(expand=1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()


# 大球吃小球游戏
def main2():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    screen.fill((255, 255, 255))
    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    # pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    ball_image = pygame.image.load('./res/ball.png')
    screen.blit(ball_image, (50, 50))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def main3():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    x, y = 50, 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        pygame.display.flip()
        pygame.time.delay(50)
        x, y = x + 5, y + 5


@unique
class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_width():
            self.sy = -self.sy

    def eat(self, other):
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


def main4():
    balls=[]
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    running=True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                x,y=event.pos
                radius=randint(10,100)
                sx,sy=randint(-10,10),randint(-10,10)
                color=Color.random_color()
                ball=Ball(x,y,radius,sx,sy,color)
                balls.append(ball)
        screen.fill((255,255,255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    main4()
