from __future__ import division
from matplotlib import pyplot as plt
from fe_utils import ReferenceTriangle
import numpy as np
from animation_tools import Animation, Scene, CellScene, Title
from matplotlib.text import Annotation
from matplotlib.lines import Line2D


class DrawReferenceTriangle(CellScene):
    def __init__(self, cell, origin, scale, anim):
        super(DrawReferenceTriangle, self).__init__(cell, anim)

        self.origin = np.asarray(origin)
        self.scale = scale

    def tr(self, pos, origin, scale):
        return scale * (pos - self.origin) / self.scale + origin

    def __call__(self, i):
        if i == 0:
            nodes = []
            nodes.append(self.anim.caption("Let's start with the reference triangle"))
            for j, v in enumerate(self.cell.vertices):
                nodes += plt.plot(v[0], v[1], 'ko', markersize=20)
                nodes.append(self.anim.ax.annotate('(%s, %s)' % (0, j), xy=v, xytext=(10, 10),
                                                   textcoords='offset points', color="black"))

                j0 = min(j, (j+1) % 3)
                j1 = max(j, (j+1) % 3)
                v0 = self.cell.vertices[j0]
                v1 = self.cell.vertices[j1]
                dx = v1 - v0
                nodes.append(self.anim.ax.annotate("", v0 + .95 * dx, v0 + .05 * dx, arrowprops={"color": "blue",
                                                                                                 "headlength": 20}))
                dx_t = np.array([-dx[1], dx[0]])
                dx_t *= np.sign(np.dot(dx_t, (1, 1))/np.sqrt(np.dot(dx_t, dx_t)))
                nodes.append(self.anim.ax.annotate('(%s, %s)' % (1, j), xy=(v0 + v1)/2, xytext=15 * dx_t,
                                                   textcoords='offset points', color="blue"))
                nodes.append(self.anim.ax.annotate('(%s, %s)' % (2, 0), xy=(0.25, 0.25), xytext=(0, 0),
                                                   textcoords='offset points', color="red"))
                self.nodes = nodes[1:]

        else:
            nodes = []
        return nodes

    def redraw(self, origin, scale):
        for node in self.nodes:
            if isinstance(node, Annotation):
                node.xy = self.tr(node.xy, origin, scale)
                if hasattr(node, "xyann"):
                    node.xyann = self.tr(node.xyann, origin, scale)
            elif isinstance(node, Line2D):
                newpos = self.tr(node.get_xydata(), origin, scale)
                node.set_xdata(newpos[:, 0])
                node.set_ydata(newpos[:, 1])
            else:
                raise TypeError("Don't know how to morph : %s" % node)
        self.origin = origin
        self.scale = scale

    @property
    def frames(self):
        return int(round(1 * self.anim.fps))


class MorphScene(Scene):
    def __init__(self, scene, origin, scale, duration):
        super(MorphScene, self).__init__(scene.anim)

        self.scene = scene
        self.origin = origin
        self.scale = scale
        self.origin0 = scene.origin
        self.scale0 = scene.scale
        self.duration = duration

    def __call__(self, i):
        ii = i / self.frames
        origin = ii * (self.origin - self.origin0) + self.origin0
        scale = ii * (self.scale - self.scale0) + self.scale0
        self.scene.redraw(origin, scale)

    @property
    def frames(self):
        return int(round(self.duration * self.anim.fps))


a = Animation(fps=30)

cell = ReferenceTriangle

a.add_scene(Title(a, "Numbering a global function space"))
rt = DrawReferenceTriangle(cell, (0., 0.), 1., a)
a.add_scene(rt)
a.add_scene(MorphScene(rt, (1., 1.), 1., 3))
a.save("global_numbering.mp4")
