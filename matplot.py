import matplotlib.pyplot as plt
import math


xList = range(100)

y1 = [x*x for x in xList]
y2 = [math.sin(x) for x in xList]
y3 = [math.sqrt(x) for x in xList]


def draw():
    # plt.plot(y1, 'b-',  label='y=x*x')
    plt.plot(y2, label='y=sin(x)')
    plt.plot(y3, 'r*', label='y=sqrt(x)')
    
    plt.legend()
    plt.show()

draw()