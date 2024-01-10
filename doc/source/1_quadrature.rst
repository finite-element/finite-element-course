.. default-role:: math

.. _quadrature:

Numerical quadrature
====================

.. only:: html

    .. dropdown:: A video recording of the following material is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495171130"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=62cf7d17-d154-4450-b540-ac9f00c206d6>`__

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
`f(X)` over an element `e` can be approximated as
a weighted sum of function values evaluated at particular points:

.. math::
   :label: quadrature

   \int_e f(X)  = \sum_{q} f(X_q) w_q + O(h^n)

we term the set `\{X_q\}` the set of *quadrature points* and the
corresponding set `\{w_q\}` the set of *quadrature weights*. A set of
quadrature points and their corresponding quadrature weights together
comprise a *quadrature rule* for `e`. For an arbitrary function `f`,
quadrature is only an approximation to the integral. The global
truncation error in this approximation is invariably of the form
`O(h^n)` where `h` is the diameter of the element.

If `f` is a polynomial in `X` with degree `p` such that
`p\leq n-2` then it is easy to show that integration using a
quadrature rule of degree `n` results in exactly zero error. 

.. _degree-of-precision:
.. proof:definition::

   The *degree of precision* of a quadrature rule is the largest `p`
   such that the quadrature rule integrates all polynomials of degree
   `p` without error.


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

.. only:: html

    .. dropdown:: A video recording of the following material is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495171317"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=74f63ac3-31ab-457d-9f45-ac9f00c1c738>`__

We noted above that a few one dimensional quadrature rules are commonly
taught in introductory integration courses. The first of these is the
midpoint rule:

.. math::
   :label: midpoint

   \int_0^h f(X) \mathrm{d} X = hf(0.5h) + O(h^3)

In other words, an approximation to the integral of
`f` over an interval can be calculated by multiplying the value
of `f` at the mid-point of the interval by the length of the
interval. This amounts to approximating the function over the integral
by a constant value.

If we improve our approximation of `f` to a straight line over
the interval, then we arrive at the trapezoidal (or trapezium) rule:

.. math::
   :label: trapezoidal

   \int_0^h f(X) \mathrm{d} X = \frac{h}{2}f(0) + \frac{h}{2}f(h) + O(h^4)

while if we employ a quadratic function then we arrive at Simpson's rule:

.. math::
   :label: 

   \int_0^h f(X) \mathrm{d} X = \frac{h}{6}f(0) + \frac{2h}{3}f\left(\frac{h}{2}\right) + \frac{h}{6}f(h) + O(h^5)


Reference cells
---------------

.. only:: html

    .. dropdown:: A video recording of the following material is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495171380"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=b2e8bfb6-89c2-4d92-8e3a-ac9f00c1c7a3>`__

As a practical matter, we wish to write down quadrature rules as
arrays of numbers, independent of `h`. In order to achieve this,
we will write the quadrature rules for a single, *reference
cell*. When we wish to actually integrate a function over cell, we
will change coordinates to the reference cell. We will return to the
mechanics of this process later, but for now it means that we need
only consider quadrature rules on the reference cells we choose.

A commonly employed one dimensional reference cell is the unit
interval `[0,1]`, and that is the one we shall adopt here (the
other popular alternative is the interval `[-1, 1]`, which some
prefer due to its symmetry about the origin).

In two dimensions, the cells employed most commonly are triangles and
quadrilaterals. For simplicity, in this course we will only consider
implementing the finite element method on triangles. The choice of a
reference interval implies a natural choice of reference triangle. For
the unit interval the natural correspondence is with the triangle with
vertices `[(0,0), (1,0), (0,1)]`, though different choices of
vertex numbering are possible.

Reference cell topology
~~~~~~~~~~~~~~~~~~~~~~~

A cell is composed of *topological entities*, that is to say vertices, edges,
faces and so forth. The topology of the cell is given by the connectivity of
its entities, for example which vertices make up each edge. It is useful to
define some terms to describe the cell topology:

.. proof:definition:: 
   
   The *dimension* of a cell is the maximal dimension of the topological 
   entities that make up the cell.

.. proof:definition::

   A topological entity of *codimension* `n` is a topological
   entity of dimension `d-n` where `d` is the dimension of the
   cell.


Armed with these definitions we are able to define names for
topological entities of various dimension and codimension:

=========== ========= ===========
entity name dimension codimension
=========== ========= ===========
vertex      0
edge        1
face        2
facet                 1
cell                  0
=========== ========= ===========

The cells can be polygons or polyhedra of any shape, however
in this course we will restrict ourselves to 
intervals and triangles. The only other two-dimensional cells
frequently employed are quadrilaterals.

Reference cell entities
~~~~~~~~~~~~~~~~~~~~~~~

The topological entities of each dimension in a cell are distinguished by
giving them unique numbers. We will identify topological entities by an index
pair `(d, i)` where `i` is the index of the entity within the set of
`d`-dimensional entities.

The particular choices of numbering we will use are shown in
:numref:`figreferenceentities`. The numbering is a matter of convention: that
adopted here is that edges share the number of the opposite vertex. The
orientation of the edges is also shown, this is always from the lower numbered
vertex to the higher numbered one.

The :class:`~fe_utils.reference_elements.ReferenceCell` class stores the
local topology of the reference cell. `Read the source
<_modules/fe_utils/reference_elements.html>`__ and ensure that you
understand the way in which this information is encoded.

.. only:: html

  The following animation of the numbering of the topological entities
  on the reference cell may help in understanding this.
          
  .. container:: youtube

    .. youtube:: 7A7JU7bGw0E?modestbranding=1;controls=0;rel=0
       :width: 600px

.. _figreferenceentities:

.. figure:: entities.*
   :width: 50%

   Local numbering and orientation of the reference entities.

.. _secadjacency:


Python implementations of reference elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :class:`~fe_utils.reference_elements.ReferenceCell` class provides
Python objects encoding the geometry and topology of the reference
cell. At this stage, the relevant information is the dimension of the
reference cell and the list of vertices. The topology will become
important in the following chapters. The reference cells we will
require for this course are the
:data:`~fe_utils.reference_elements.ReferenceInterval` and
:data:`~fe_utils.reference_elements.ReferenceTriangle`.

Quadrature rules on reference elements
--------------------------------------

.. only:: html

    .. dropdown:: A video recording of the following material is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495171523"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=adcb767d-5c36-4a7e-92d2-ac9f00c1c7d3>`__

Having adopted a convention for the reference element, we can simply
express quadrature rules as lists of quadrature points with
corresponding quadrature weights. For example Simpson's rule becomes:

.. math::
   :label:
   
   w = \left[ \frac{1}{6}, \frac{2}{3}, \frac{1}{6} \right]

   X = \left[ (0), (0.5), (1)\right].

We choose to write the quadrature points as 1-tuples for consistency
with the `n`\-dimensional case, in which the points will be
`n`\-tuples.

The lowest order quadrature rule on the reference triangle is a single point
quadrature:

.. math::
   :label:

   w = \left[ \frac{1}{2} \right]

   X = \left[ \left(\frac{1}{3}, \frac{1}{3}  \right) \right] 

This rule has a degree of precision of 1.

.. hint::

   The weights of a quadrature rule always sum to the volume of the
   reference element. Why is this?


Legendre-Gauß quadrature in one dimension
-----------------------------------------

The finite element method will result in integrands of different
polynomial degrees, so it is convenient if we have access to
quadrature rules of arbitrary degree on demand. In one dimension the
`Legendre-Gauß quadrature rules
<http://mathworld.wolfram.com/Legendre-GaussQuadrature.html>`__ are a
family of rules of arbitrary precision which we can employ for this
purpose. Helpfully, numpy provides `an implementation
<http://docs.scipy.org/doc/numpy/reference/generated/numpy.polynomial.legendre.leggauss.html>`__
which we are able to adopt. The Legendre-Gauß quadrature rules are
usually defined for the interval `[-1, 1]` so we need to change
coordinates in order to arrive at a quadrature rule for our reference
interval:

.. math::
   :label:
      
   X_q = \frac{X'_q + 1}{2}

   w_q = \frac{w'_q}{2}

where `(\{X'_q\}, \{w'_q\})` is the quadrature rule on the interval
`[-1, 1]` and `(\{X_q\}, \{w_q\})` is the rule on the unit interval.

Legendre-Gauß quadrature on the interval is optimal in the sense that it uses the
minimum possible number of points for each degree of precision.

Extending Legendre-Gauß quadrature to two dimensions
----------------------------------------------------

We can form a unit square by taking the Cartesian product of two unit
intervals: `(0, 1)\otimes (0, 1)`. Similarly, we can form a quadrature
rule on a unit square by taking the product of two interval quadrature
rules:

.. math::
   :label: squarequad

   X_\textrm{sq} = \left\{ (x_p, x_q)\ \middle|\ x_p, x_q \in X \right\}

   w_\textrm{sq} = \left\{ w_p w_q\ \middle|\ w_p, w_q \in w \right\}

where `(X, w)` is an interval quadrature rule. Furthermore, the degree
of accuracy of `(X_\textrm{sq}, w_\textrm{sq})` will be the same as
that of the one-dimensional rule.

However, we need a quadrature rule for the unit triangle. We can
achieve this by treating the triangle as a square with a zero length
edge. The Duffy transform maps the unit square to the unit triangle:

.. math::
   :label:

   (x_\textrm{tri},\ y_\textrm{tri}) = 
     \left(x_\textrm{sq},\ y_\textrm{sq}(1 - x_\textrm{sq})\right)

.. _figduffy:

.. figure:: duffy.*
   :width: 60%

   The Duffy transform maps a square to a triangle by collapsing one side.

By composing the Duffy transform with :eq:`squarequad` we can arrive
at a quadrature rule for the triangle:

.. math::
   :label: triquad

   X_\textrm{tri} =\left\{ \left(x_p, x_q(1 - x_p)\right)\ \middle|\ x_p \in X_h, x_q \in X_v \right\}

   w_\textrm{tri} = \left\{ w_p w_q(1 - x_p)\ \middle|\ w_p \in w_h, w_q \in w_v \right\}

where `(X_v, w_v)` is a reference interval quadrature rule with degree
of precision `n` and `(X_h, w_h)` is a reference interval quadrature
rule with degree of precision `n+1`. The combined quadrature rule
`(X_\textrm{tri}, w_\textrm{tri})` will then be `n`. The additional
degree of precision required for `(X_h, w_h)` is because the Duffy
transform effectively increases the polynomial degree of the integrand
by one.

Implementing quadrature rules in Python
---------------------------------------

.. only:: html

    .. dropdown:: A video recording about how to do this exercise is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495171661"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e5f1084f-c163-46d3-b317-ac9f00c1c772>`__

The :mod:`fe_utils.quadrature` module provides the
:class:`~fe_utils.quadrature.QuadratureRule` class which records
quadrature points and weights for a given
:class:`~fe_utils.reference_elements.ReferenceCell`. The
:func:`~fe_utils.quadrature.gauss_quadrature` function creates
quadrature rules for a prescribed degree of precision and reference
cell.

.. _ex-integrate:

.. proof:exercise::

   The :meth:`~fe_utils.quadrature.QuadratureRule.integrate` method is
   left unimplemented. Using :eq:`quadrature`, implement this method.

   A test script for your method is provided in the ``test`` directory
   as ``test_01_integrate.py``. Run this script to test your code::

      py.test test/test_01_integrate.py

   from the Bash command line. Make sure you commit your modifications and push them
   to your fork of the course repository.

.. hint::

   You can implement
   :meth:`~fe_utils.quadrature.QuadratureRule.integrate` in one line
   using a `list
   comprehension
   <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>`__ and :func:`numpy.dot`.

.. hint::

   Don't forget to activate your Python venv!

.. only:: html

    .. dropdown:: A video recording of the solution to this exercise is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495171917"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=a2b1c67a-a9d3-485b-8784-ac9f00c1dad5>`__
