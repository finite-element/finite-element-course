from __future__ import division
from matplotlib import pyplot as plt
from matplotlib import animation, rcParams
import numpy as np


def init():
    return []


class Animation(object):
    def __init__(self, fps):

        self.fps = fps
        rcParams.update({'font.size': 36})
        self.fig = plt.figure(facecolor="white", edgecolor="white", figsize=(16, 12))
        self.reset()

    def reset(self):
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)

        ax.axis(np.add(ax.axis(), [-.5, .5, -.5, .5]))
        ax.axis('off')

        self.ax = ax
        self.txt = plt.figtext(0.5, 0.1, "", horizontalalignment='center', wrap=True)

        self.scenes = []

    def add_scene(self, scene):
        self.scenes.append(scene)

    def caption(self, text):

        self.txt.set_text(text)
        return self.txt

    @property
    def frames(self):
        return sum(s.frames for s in self.scenes)

    def __call__(self, i):
        ii = i
        for s in self.scenes:
            if ii < s.frames:
                return s(ii)
            else:
                ii -= s.frames

    def save(self, filename, extra_args=['-vcodec', 'libx264']):
        anim = animation.FuncAnimation(self.fig, self, self.frames, init_func=init, interval=1./self.fps)
        anim.save(filename, fps=self.fps, extra_args=extra_args)


class Scene(object):
    def __init__(self, anim):

        self.anim = anim

    @property
    def frames(self):
        raise NotImplementedError

    def __call__(self, i):
        raise NotImplementedError


class Pause(Scene):
    def __init__(self, duration, anim):
        super(Pause, self).__init__(anim)
        self.duration = duration

    def __call__(self, i):
        return

    @property
    def frames(self):
        return int(round(self.anim.fps * self.duration))


class CellScene(Scene):
    def __init__(self, cell, anim):
        super(CellScene, self).__init__(anim)
        self.cell = cell


class Title(Scene):
    def __init__(self, anim, text):
        super(Title, self).__init__(anim)
        self.text = text

    def __call__(self, i):
        if i == 0:
            self.txt = plt.figtext(0.5, 0.5, self.text, horizontalalignment='center', wrap=True)
        if i > 0:
            self.txt.set_color(str((i + 1) / self.anim.fps))
        if i == self.anim.fps - 1:
            self.txt.set_text("")
            plt.draw()

        return self.txt,

    @property
    def frames(self):
        return int(round(self.anim.fps))
