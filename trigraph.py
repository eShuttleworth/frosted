from mpl_toolkits.mplot3d import Axes3D  
import numpy as np
import matplotlib.pyplot as plt


class ScrollyTrigraph(object):
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('use scroll wheel navigate through space instead of time')

        self.X = X
        self.slices = len(X)
        self.ind = self.slices//2

        self.im = ax.scatter(self.X[self.ind][0], self.X[self.ind][1], self.X[self.ind][2])
        # self.update()

    def onscroll(self, event):
        print('{} {}'.format(event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind - 1) % self.slices
        else:
            self.ind = (self.ind + 1) % self.slices
        self.update()

    def update(self):
        # self.im = self.ax.scatter(self.X[self.ind][0], self.X[self.ind][1], self.X[self.ind][2])

        self.ax.set_xlabel('slice starting at  {:X}'.format(self.ind*1048))
        self.im.axes.figure.canvas.draw()
