from __future__ import division
from matplotlib import pyplot as plt
from fe_utils import ReferenceTriangle, LagrangeElement, UnitSquareMesh, \
    ReferenceInterval, UnitIntervalMesh, FunctionSpace
import numpy as np
from matplotlib import animation, rcParams


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


def init():
    return []


class CellScene(Scene):
    def __init__(self, cell, anim):
        super(CellScene, self).__init__(anim)
        self.cell = cell


class Title(Scene):
    def __call__(self, i):
        if i == 0:
            self.txt = plt.figtext(0.5, 0.5, "Numbering the entities on a reference triangle.", horizontalalignment='center', wrap=True)
        if i > 0:
            self.txt.set_color(str((i + 1) / self.anim.fps))
        if i == self.anim.fps - 1:
            self.txt.set_text("")
            plt.draw()

        return self.txt,

    @property
    def frames(self):
        return int(round(self.anim.fps))


class BuildTriangle(CellScene):
    def __call__(self, i):
        if i == 0:
            nodes = []
            nodes.append(self.anim.caption("We start with the reference triangle vertices at (0, 0), (0, 1), and (1, 0)"))
            for v in self.cell.vertices:
                nodes.append(plt.plot(v[0], v[1], 'ko', markersize=20))
            return nodes

    @property
    def frames(self):
        return int(round(4. * self.anim.fps))


class LabelTriangleVertices(CellScene):
    def __call__(self, i):
        if i == 0:
            c = [self.anim.caption("We label the vertices in lexicographic order.")]
        else:
            c = []

        for j, v in enumerate(self.cell.vertices):
            if i == int(j * self.frames/4):
                return c + [self.anim.ax.annotate('(%s, %s)' % (0, j), xy=v, xytext=(10, 10),
                                                  textcoords='offset points', color="black")]

    @property
    def frames(self):
        return int(round(4. * self.anim.fps))


class DrawEdges(CellScene):
    def __call__(self, i):
        if i == 0:
            return self.anim.caption("The edges are oriented from lower numbered vertex to higher."),
        ii = (i - self.frames // 10) % (2 * self.anim.fps)
        jj = (i - self.frames // 10) // (2 * self.anim.fps)
        if jj < 3:
            j0 = min(jj, (jj+1) % 3)
            j1 = max(jj, (jj+1) % 3)
            v0 = self.cell.vertices[j0]
            v1 = self.cell.vertices[j1]
            dx = v1 - v0
            if ii == 0:
                self.anim.caption("From vertex %d to vertex %d." % (j0, j1))
                self.ar = self.anim.ax.annotate("", v0 + .2 * dx, v0 + .05 * dx, arrowprops={"color": "blue",
                                                                                             "headlength": 20})
            elif ii < self.anim.fps:
                self.ar.xy = v0 + (.2 + .75 * (ii / self.anim.fps)) * dx
            return self.ar,
        elif ii == 0:
            return self.anim.caption("Notice that that last edge appears to run backwards!"),

    @property
    def frames(self):
        return int(round(10. * self.anim.fps))


class LabelEdges(CellScene):
    def __call__(self, i):
        if i == 0:
            c = [self.anim.caption("Next we label the edges. Each edge recieves the edge number of the opposite vertex.")]
        else:
            c = []

        for j, v in enumerate(self.cell.vertices):
            if i == int(j * self.frames/4):
                v0 = self.cell.vertices[(j + 1) % 3]
                v1 = self.cell.vertices[(j + 2) % 3]
                dx = v1 - v0
                dx_t = np.array([-dx[1], dx[0]])
                dx_t *= np.sign(np.dot(dx_t, (1, 1))/np.sqrt(np.dot(dx_t, dx_t)))
                return c + [self.anim.ax.annotate('(%s, %s)' % (1, j), xy=(v0 + v1)/2, xytext=15 * dx_t,
                                                  textcoords='offset points', color="blue")]

    @property
    def frames(self):
        return int(round(4. * self.anim.fps))


class LabelCell(CellScene):
    def __call__(self, i):
        if i == 0:
            return self.anim.caption("Finally, we label the cell itself."),

        if i == int(self.anim.fps):
            return self.anim.ax.annotate('(%s, %s)' % (2, 0), xy=(0.25, 0.25), xytext=(0, 0),
                                         textcoords='offset points', color="red"),

    @property
    def frames(self):
        return int(round(4. * self.anim.fps))

a = Animation(fps=30)

cell = ReferenceTriangle

a.add_scene(Title(a))
a.add_scene(BuildTriangle(cell, a))
a.add_scene(LabelTriangleVertices(cell, a))
a.add_scene(DrawEdges(cell, a))
a.add_scene(LabelEdges(cell, a))
a.add_scene(LabelCell(cell, a))
a.save("reference_element.mp4")

