from matplotlib import pyplot as plt
from fe_utils import ReferenceTriangle, LagrangeElement, UnitSquareMesh, FunctionSpace
from argparse import ArgumentParser
import numpy as np

parser = ArgumentParser(description="""Plot the nodes on the function space given.""")
parser.add_argument("resolution", type=int, nargs=1, 
                    help="The number of cells in each direction on the unit square mesh.")
parser.add_argument("degree", type=int, nargs=1)
args = parser.parse_args()
resolution = args.resolution[0]
degree = args.degree[0]

fe = LagrangeElement(ReferenceTriangle, degree)
mesh = UnitSquareMesh(resolution, resolution)
fs = FunctionSpace(mesh, fe)

nodes = np.empty((fs.node_count, ReferenceTriangle.dim))
cg1 = LagrangeElement(ReferenceTriangle, 1)
coord_map = cg1.tabulate(fe.nodes)
for c in range(mesh.entity_counts[-1]):
    # Interpolate the coordinates to the cell nodes.
    vertex_coords = mesh.vertices[mesh.cell_vertices[c, :], :]
    lcoords = np.dot(coord_map, vertex_coords)

    # Insert the resulting cells into the global set.
    nodes[fs.cell_nodes[c, :].astype(int), :] = lcoords

fig = plt.figure()
ax = fig.add_subplot(111)

for e in mesh.edge_vertices:
    plt.plot(mesh.vertices[e, 0], mesh.vertices[e, 1], 'k')

plt.plot(nodes[:, 0], nodes[:, 1], 'bo')

for i, x in enumerate(nodes):
    ax.annotate(str(i), xy=x, xytext=(10, 1), textcoords='offset points')

ax.axis([-.1, 1.1, -.1, 1.1])

plt.show()
