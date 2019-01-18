"""Test the entity_node assignment for Lagrange elements"""
import pytest
from fe_utils import LagrangeElement, ReferenceTriangle, ReferenceInterval
from scipy.special import comb
import numpy as np


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(1, 8)])
def test_nodes_per_entity(cell, degree):

    fe = LagrangeElement(cell, degree)

    for d in range(cell.dim+1):
        node_count = comb(degree-1, d)
        for e in fe.entity_nodes[d].values():
            assert len(e) == node_count


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(1, 8)])
def test_nodes_on_correct_entity(cell, degree):

    fe = LagrangeElement(cell, degree)

    for d in range(cell.dim+1):
        for e, nodes in fe.entity_nodes[d].items():
            for n in nodes:
                assert cell.point_in_entity(fe.nodes[n], (d, e))


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(3, 8)])
def test_edge_orientation(cell, degree):
    """Test that the nodes on edges go in edge order"""

    fe = LagrangeElement(cell, degree)

    # Only test edges.
    d = 1

    for e, nodes in fe.entity_nodes[d].items():
        vertices = [np.array(cell.vertices[v]) for v in cell.topology[d][e]]

        # Project the nodes onto the edge.
        p = [np.dot(fe.nodes[n] - vertices[0], vertices[1] - vertices[0])
             for n in nodes]

        assert np.all(p[:-1] < p[1:])


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
