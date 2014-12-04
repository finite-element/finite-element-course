from reference_elements import ReferenceInterval, ReferenceTriangle
import numpy as np


def lagrange_points(cell, degree):
    """Construct the locations of the equispaced Lagrange nodes on cell.
    
    :param cell: the :class:`~.reference_elements.ReferenceCell`
    :param degree: the degree of polynomials for which to construct nodes.

    :returns: the list of coordinate tuples corresponding to the nodes.

    The implementation of this function is left as an :ref:`exercise
    <ex-lagrange-points>`.
    """
    
    raise NotImplementedError


def vandermonde_matrix(cell, degree, nodes, grad=False):
    """Construct the generalised Vandermonde matrix for polynomials of the
    specified degree on the cell provided.

    
    :param cell: the :class:`~.reference_elements.ReferenceCell`
    :param degree: the degree of polynomials for which to construct the matrix.
    :param nodes: a list of coordinate tuples corresponding to the nodes.
    :param grad: whether to evaluate the Vandermonde matrix or its gradient.

    :returns: the generalised :ref:`Vandermonde matrix <sec-vandermonde>`

    The implementation of this function is left as an :ref:`exercise
    <ex-vandermonde>`.
    """

    raise NotImplementedError


class FiniteElement(object):
    def __init__(self, cell, degree, nodes):
        """A finite element defined over cell.
        
        :param cell: the :class:`~.reference_elements.ReferenceCell`
            over which the element is defined.  
        :param degree: the
            polynomial degree of the element. We assume the element
            spans the complete polynomial space.
        :param nodes: a list of coordinate tuples corresponding to 
            the nodes of the element.

        Most of the implementation of this class is left as exercises.
        """
        
        self.cell = cell
        self.degree = degree 
        self.nodes = nodes

        raise NotImplementedError
        
