from matplotlib import pyplot as plt
from fe_utils import ReferenceTriangle, LagrangeElement, UnitSquareMesh, FunctionSpace
from argparse import ArgumentParser
import numpy as np

parser = ArgumentParser(description="""Plot the nodes on the function space given.""")
parser.add_argument("resolution", type=int, nargs=1, 
                    help="The number of cells in each direction on the unit square mesh.")
args = parser.parse_args()
resolution = args.resolution[0]

mesh = UnitSquareMesh(resolution, resolution)

fig = plt.figure()
ax = fig.add_subplot(111)

for e in mesh.edge_vertices:
    plt.plot(mesh.vertices[e, 0], mesh.vertices[e, 1], 'k')

colours = ["black", "red", "blue"]

for i, x in enumerate(mesh.vertices):
    ax.annotate('(%s, %s)' % (0, i), xy=x, xytext=(10, 1),
                textcoords='offset points', color=colours[0])

for d in range(1, mesh.dim + 1):
    adj = mesh.adjacency(d, 0)
    for i, e in enumerate(adj):
        x = np.mean(mesh.vertices[e, :], axis=0)

        ax.annotate('(%s, %s)' % (d, i), xy=x, xytext=(10, 1),
                    textcoords='offset points', color=colours[d])

ax.axis(np.add(ax.axis(), [-.1, .1, -.1, .1]))

plt.show()
