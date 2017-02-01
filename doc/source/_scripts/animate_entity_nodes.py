from __future__ import division
from matplotlib import pyplot as plt
from fe_utils import ReferenceTriangle
import numpy as np
from animation_tools import Animation, Scene, CellScene, Title, Pause
from matplotlib.text import Annotation
from matplotlib.lines import Line2D
from matplotlib.colors import to_rgb


class DrawReferenceTriangle(CellScene):
    def __init__(self, cell, origin, scale, anim):
        super(DrawReferenceTriangle, self).__init__(cell, anim)

        self.origin = np.asarray(origin)
        self.scale = scale
        self.entities = {i: {} for i in range(3)}

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
                self.entities[0][j] = nodes[-1]
                j0 = min((j+1) % 3, (j+2) % 3)
                j1 = max((j+1) % 3, (j+2) % 3)
                v0 = self.cell.vertices[j0]
                v1 = self.cell.vertices[j1]
                dx = v1 - v0
                nodes.append(self.anim.ax.annotate("", v0 + .95 * dx, v0 + .05 * dx, arrowprops={"color": "blue",
                                                                                                 "headlength": 20}))
                dx_t = np.array([-dx[1], dx[0]])
                dx_t *= np.sign(np.dot(dx_t, (1, 1))/np.sqrt(np.dot(dx_t, dx_t)))
                nodes.append(self.anim.ax.annotate('(%s, %s)' % (1, j), xy=(v0 + v1)/2, xytext=15 * dx_t,
                                                   textcoords='offset points', color="blue"))
                self.entities[1][j] = nodes[-1]
            nodes.append(self.anim.ax.annotate('(%s, %s)' % (2, 0), xy=(0.25, 0.25), xytext=(0, 0),
                                               textcoords='offset points', color="red"))
            self.entities[2][0] = nodes[-1]
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


class DrawP3Triangle(CellScene):
    def __init__(self, cell, origin, scale, anim):
        super(DrawP3Triangle, self).__init__(cell, anim)

        self.origin = np.asarray(origin)
        self.scale = scale

    def tr(self, pos, origin, scale):
        return scale * (pos - self.origin) / self.scale + origin

    def __call__(self, i):
        if i == 0:
            nodes = []
            nodes.append(self.anim.caption("Now the P3 node evaluation points."))

            for j, v in enumerate(self.cell.vertices):
                nodes += plt.plot(v[0], v[1], 'ko', markersize=20)

                j0 = min(j, (j+1) % 3)
                j1 = max(j, (j+1) % 3)
                v0 = self.cell.vertices[j0]
                v1 = self.cell.vertices[j1]
                dx = v1 - v0
                nodes.append(self.anim.ax.annotate("", v0 + .95 * dx, v0 + .05 * dx, arrowprops={"color": "blue",
                                                                                                 "headlength": 20}))
                # dx_t = np.array([-dx[1], dx[0]])
                # dx_t *= np.sign(np.dot(dx_t, (1, 1))/np.sqrt(np.dot(dx_t, dx_t)))

            points = np.array([(ii/3., jj/3) for jj in range(4) for ii in range(4-jj)])
            self.pointlabels = []
            for j, p in enumerate(points):
                nodes += plt.plot(p[0], p[1], 'ko', markersize=20)
                nodes.append(self.anim.ax.annotate('%s' % j, xy=p, xytext=(10, 10),
                                                   textcoords='offset points', color="black"))
                self.pointlabels.append(nodes[-1])

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


def format_dict(d):
    return "{" + ("\n" + " " * 14).join(["%s: %s" % i for i in d.iteritems()]) + "\n}"


class EntityDofScene(Scene):
    entity_dofs = {0: {0: [0], 1: [3], 2: [9]},
                   1: {0: [6, 8], 1: [4, 7], 2: [1, 2]},
                   2: {0: [5]}}

    def __init__(self, delay, rt, p3, a):
        super(EntityDofScene, self).__init__(a)

        self.delay = delay
        self.rt = rt
        self.p3 = p3
        self.current_dofs = {}

    def __call__(self, i):
        if i == 0:
            text = self.anim.ax.annotate("entity_node = " + format_dict({}), xy=(-.4, 0.1), color="black")
            self.anim.caption("The entity node list lists the nodes on each entity in order.")

            def iterator():
                for d in self.entity_dofs:
                    self.current_dofs[d] = {}
                    for e in self.entity_dofs[d]:
                        self.current_dofs[d][e] = []
                        # Make rt.entities[d][e] yellow.
                        entity = self.rt.entities[d][e]
                        ei = 0.
                        ec = np.array(to_rgb(entity.get_color()))
                        entity.set_color((1., 1., 0.))
                        for dof in self.entity_dofs[d][e]:
                            point = self.p3.pointlabels[dof]
                            pi = 0.
                            point.set_color((1., 1., 0.))
                            # Make p3 dof yellow.
                            self.current_dofs[d][e].append(dof)
                            text.set_text("entity_node = " + format_dict(self.current_dofs))
                            yield [text, entity]
                            for i in range(self.delay):
                                ei = min(ei+1., self.delay)
                                pi = min(pi+1., self.delay)
                                entity.set_color(ei/self.delay*ec + (1 - ei/self.delay)*np.array((1., 1., 0)))
                                point.set_color((1 - pi/self.delay)*np.array((1., 1., 0)))
                                yield [text, entity]
            self.iterator = iterator()
        return next(self.iterator, None)

    @property
    def frames(self):
        return int(round(self.delay * (3 + 10)))


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

a.add_scene(Title(a, "Constructing the entity to node mapping"))
rt = DrawReferenceTriangle(cell, (0., 0.), 1., a)
a.add_scene(rt)
a.add_scene(MorphScene(rt, (.8, .8), 0.66, 2.5))
p3 = DrawP3Triangle(cell, (0., 0.), 1., a)
a.add_scene(p3)
a.add_scene(MorphScene(p3, (-.2, .8), 0.66, 2.5))
a.add_scene(Pause(0.5, a))
a.add_scene(EntityDofScene(30, rt, p3, a))
a.save("entity_node.mp4")
