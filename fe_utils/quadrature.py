from numpy.polynomial.legendre import leggauss
from .reference_elements import ReferenceInterval, ReferenceTriangle
import numpy as np


class QuadratureRule(object):
    def __init__(self, cell, degree, points, weights):
        """A quadrature rule implementing integration of the reference cell
        provided.

        :param cell: the :class:`~.ReferenceCell` over which this quadrature
          rule is defined.
        :param degree: the :ref:`degree of precision <degree-of-precision>`
          of this quadrature rule.
        :points: a list of the position vectors of the quadrature points.
        :weights: the corresponding vector of quadrature weights.
        """

        #: The :class:`~.ReferenceCell` over which this quadrature
        #: rule is defined.
        self.cell = cell
        #: Two dimensional array, the rows of which form the position
        #: vectors of the quadrature points.
        self.points = np.array(points, dtype=np.double)
        #: The corresponding array of quadrature weights.
        self.weights = np.array(weights, dtype=np.double)
        #: The degree of precision of the quadrature rule.
        self.degree = degree

        if self.cell.dim != self.points.shape[1]:
            raise ValueError(
                "Dimension mismatch between reference cell and quadrature points")
        if self.points.shape[0] != len(self.weights):
            raise ValueError(
                "Number of quadrature points and quadrature weights must match")

    def integrate(self, function):
        """Integrate the function provided using this quadrature rule.

        :param function: A Python function taking a position vector as
          its single argument and returning a scalar value.

        The implementation of this method is left as an :ref:`exercise
        <ex-integrate>`.
        """

        raise NotImplementedError


def gauss_quadrature(cell, degree):
    """Return a Gauss-Legendre :class:`QuadratureRule`.

      :param cell: the :class:`~.ReferenceCell` over which this quadrature
        rule is defined.
      :param degree: the :ref:`degree of precision <degree-of-precision>`
        of this quadrature rule.
    """

    if cell is ReferenceInterval:
        # We can obtain the 1D gauss-legendre rule from numpy
        # and change coordinates.

        # Gauss-legendre quadrature has degree = 2 * npoints - 1
        # The extra + 1 deals with truncation.
        npoints = int((degree + 1 + 1) / 2)

        points, weights = leggauss(npoints)

        # Numpy uses the [-1, 1] interval, we need to change to [0, 1]
        points = (points + 1.) / 2.
        # Rescale the weights to sum to 1 instead of 2.
        weights = weights / 2.

        # We expect points to be an n x dim array.
        points.shape = [points.shape[0], 1]

    elif cell is ReferenceTriangle:
        # The 2D rule is obtained using the 1D rule and the Duffy Transform.

        p1 = gauss_quadrature(ReferenceInterval, degree + 1)
        q1 = gauss_quadrature(ReferenceInterval, degree)

        points = np.array([(p[0], q[0] * (1 - p[0]))
                           for p in p1.points
                           for q in q1.points])

        weights = np.array([p * q * (1 - x[0])
                            for p, x in zip(p1.weights, p1.points)
                            for q in q1.weights])

    else:
        raise ValueError("Unknown reference cell")

    return QuadratureRule(cell, degree, points, weights)
