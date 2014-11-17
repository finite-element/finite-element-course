Numerical quadrature
====================

The core computational operation with which we are concerned in the
finite element method is the integration of a function over a known
reference element. It's no big surprise, therefore, that this
operation will be at the heart of our finite element implementation.

The usual way to efficiently evaluate arbitrary integrals numerically
is numerical quadrature. This basic idea will already be familiar to
you from undergraduate maths (or maybe even high school calculus) as
it's the generalisation of the trapezoidal rule and Simpson's rule for
integration.

The core idea of quadrature is that the integral of a function
:math:`f(X)` over an element :math:`e` can be approximated as
a weighted sum of function values evaluated at particular points:

.. math::

   \int_e f(X)  = \sum_{q} f(X_q) w_q + O(h^n)

we term the set :math:`\{X_q\}` the set of *quadrature points* and the
corresponding set :math:`\{w_q\}` the set of *quadrature weights*. A
set of quadrature points and their corresponding quadrature weights
together comprise a *quadrature rule*. For an arbitrary function
:math:`f`, quadrature is only an approximiation to the integral. The
global truncation error in this approximation is invariably of the
form :math:`O(h^n)` where :math:`h` is the diameter of the 
element. 

If :math:`f` is a polynomial in `X` with degree :math:`p` such that
:math:`p\leq n-2` then it is easy to show that integration using a
quadrature rule of degree :math:`n` results in exactly zero error. The
largest :math:`p` such that a given quadrature rule integrates all
polynomials of degree :math:`p` without error is termed the *degree of
precision* of the quadrature rule.


Exact and incomplete quadrature
-------------------------------

In the finite element method, integrands are very frequently
polynomial. If the quadrature rule employed for a particular interval
has a sufficiently high degree of precision such that there is no
quadrature error in the integration, we refer to the quadrature as
*exact* or *complete*. In any other case we refer to the quadrature as
*incomplete*.

Typically, higher degree quadrature rules have more quadrature points
than lower degree rules. This results in a trade-off between the
accuracy of the quadrature rule and the number of function
evaluations, and hence the computational cost, of an integration using
that rule. Complete quadrature results in lower errors, but if the
error due to incomplete quadrature is small compared with other errors
in the simulation, particularly compared with the discretisation
error, then incomplete quadrature may be advantageous.

Examples in one dimension
-------------------------

We noted above that a few one dimensional quadrature rules are commonly
taught in introductory integration courses. The first of these is the
midpoint rule:

.. math::

   \int_0^h f(X) \mathrm{d} X = hf(0.5h) + O(h^3)

In other words, an approximation to the integral of
:math:`f` over an interval can be calculated by multiplying the value
of :math:`f` at the mid-point of the interval by the length of the
interval. This amounts to approximating the function over the integral
by a constant value.

If we improve our approximation of :math:`f` to a straight line over
the interval, then we arrive at the trapezoidal (or trapezium) rule:

.. math::

   \int_0^h f(X) \mathrm{d} X = \frac{h}{2}f(0) + \frac{h}{2}f(h) + O(h^4)

while if we employ a quadratic function then we arrive at Simpson's rule:

.. math::

   \int_0^h f(X) \mathrm{d} X = \frac{h}{6}f(0) + \frac{2h}{3}f\left(\frac{h}{2}\right) + \frac{h}{6}f(h) + O(h^5)



Quadrature rules on reference elements
--------------------------------------

As a practical matter, we wish to write down quadrature rules as
arrays of numbers, independent of :math:`h`. In order to achieve this,
we will write the quadrature rules for a single, *reference
element*. When we wish to actually integrate a function over cell, we
will change coordinates to the reference cell. We will return to the
mechanics of this process later, but for now it means that we need
only consider quadrature rules on the reference cells we choose.

A commonly employed one dimensional reference cell is the unit
interval :math:`[0,1]`, and that is the one we shall adopt here (the
other popular alternative is the interval :math:`[-1, 1]`, which some
prefer due to its symmetry about the origin).

Having adopted a convention for the reference element, we can simply
express quadrature rules as lists of quadrature points with
corresponding quadrature weights. For example Simpson's rule becomes:

.. math::
   
   w = \left[ \frac{1}{6}, \frac{2}{3}, \frac{1}{6} \right]

   X = \left[ (0), (0.5), (1)\right].

We choose to write the quadrature points as 1-tuples for consistency
with the :math:`n`\-dimensional case, in which the points will be
:math:`n`\-tuples.

In two dimensions, the cells employed most commonly are triangles and
quadrilaterals. For simplicity, in this course we will only consider
implementing the finite element method on triangles. The choice of a
reference interval implies a natural choice of reference triangle. For
the unit interval the natural correspondence is with the triangle with
vertices :math:`[(0,0), (1,0), (0,1)]`, though different choices of
vertex numbering are possible.

The lowest order quadrature rule on this triangle is a single point
quadrature:

.. math::

   w = \left[ \frac{1}{2} \right]

   X = \left[ \left(\frac{1}{3}, \frac{1}{3}  \right) \right] 

This rule has a degree of precision of 1.


Implementing quadrature rules in Python
---------------------------------------


