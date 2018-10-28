class ScrollyDigraph(object):
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('use scroll wheel navigate through space instead of time')

        self.X = X
        _, _, self.slices = X.shape
        self.ind = self.slices // 2

        self.im = ax.imshow(self.X[:, :, self.ind])
        self.update()

    def onscroll(self, event):
        print('{} {}'.format(event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind - 1) % self.slices
        else:
            self.ind = (self.ind + 1) % self.slices
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        self.ax.set_xlabel('slice starting at  {:X}'.format(self.ind * 1048))
        self.im.axes.figure.canvas.draw()
