#coding: utf8
import matplotlib.pyplot as plt
import math
import numpy as np

xList = range(100)

y1 = [x*x for x in xList]
y2 = [math.sin(x) for x in xList]
y3 = [math.sqrt(x) for x in xList]


def draw():
    # plt.plot(y1, 'b-',  label='y=x*x')
    plt.plot(y2, label='y=sin(x)')
    plt.plot(y3, 'r*', label='y=sqrt(x)')
    plt.grid()
    plt.legend()
    plt.show()

def drawWithTicks():
    # plt.plot(y1, 'b-',  label='y=x*x')
    plt.plot(y2, label='y=sin(x)')
    plt.plot(y3, 'r*', label='y=sqrt(x)')
    yticks = np.arange(min(y2), max(y2), 1) # 设置坐标轴刻度
    plt.yticks(yticks)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0)) # 坐标轴用科学计数法
    plt.grid()
    plt.legend()
    plt.show()

draw()

xList = range(1, 23)

y = [math.sqrt((x**3 + 7*x + 11) % 23) for x in xList]
y2 = [-math.sqrt((x**3 + 7*x + 11) % 23) for x in xList]
def drawElliptic():
    plt.plot(xList, y)
    plt.plot(xList, y2)
    plt.grid()
    plt.show()

drawElliptic()

