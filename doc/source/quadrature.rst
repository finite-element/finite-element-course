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
element. The integer :math:`n` is termed the *degree* of the
quadrature rule.

Exact and incomplete quadrature
-------------------------------

If :math:`f` is a polynomial in `X` with degree :math:`p` such that
:math:`p\leq n-1` then it is easy to show that integration using a
quadrature rule of degree :math:`n` results in exactly zero error. In
this case we refer to the quadrature as *exact* or *complete*. In any
other case we refer to the quadrature as *incomplete*.

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

Note that these error terms are *local* truncation errors which depend
on the interval of integration being of the variable length
:math:`h`. If any of these rules is employed to integrate :math:`f`
over a fixed interval :math:`(a,b)` by dividing into subintervals of
length :math:`h`, then summing over the :math:`(b-a)/h` intervals will
result in a *global* truncation error one degree lower than the local
truncation error.

Quadrature rules on reference elements
--------------------------------------

As a practical matter, we wish to write down quadrature rules as
arrays of numbers, independent of :math:`h`. In order to achieve this,
we will write the quadrature rules for a single, *reference
element*. When we wish to actually integrate a function over cell, we
will change coordinates to the reference cell. We write :math:`x` for the coordinates in the 


Implementing quadrature rules in Python
---------------------------------------
