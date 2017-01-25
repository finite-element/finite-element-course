from __future__ import division
from matplotlib import pyplot as plt
from fe_utils import ReferenceTriangle
import numpy as np
from animation_tools import Animation, Scene, CellScene, Title


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
                return self.ar,
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

a.add_scene(Title(a, "Numbering the entities on a reference triangle."))
a.add_scene(BuildTriangle(cell, a))
a.add_scene(LabelTriangleVertices(cell, a))
a.add_scene(DrawEdges(cell, a))
a.add_scene(LabelEdges(cell, a))
a.add_scene(LabelCell(cell, a))
a.save("reference_element.mp4")

