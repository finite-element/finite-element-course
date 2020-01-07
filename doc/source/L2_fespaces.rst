.. default-role:: math

Finite element spaces: local to global
======================================

In this section, we discuss the construction of general finite element
spaces. Given a triangulation `\mathcal{T}` of a domain `\Omega`, finite
element spaces are defined according to

#. the form the functions take (usually polynomial) when restricted
  to each cell (a triangle, in the case considered so far),
#. the continuity of the functions between cells.

We also need a mechanism to explicitly build a basis for the finite
element space. We first do this by looking at a single cell, which we
call the local perspective. Later we will take the global perspective,
seeing how function continuity is enforced between cells.

The first part of the definition is formalised by Ciarlet's definition
of a finite element.

.. proof:definition:: Ciarlet's finite element

   Let
   #. the \emph{element domain} `K\subset \mathbb{R}^n` be some
    bounded closed set with piecewise smooth boundary,
   #. the \emph{space of shape functions} `\mathcal{P}` be a
    finite dimensional space of functions on `K`, and
   #. the \emph{set of nodal variables} `\mathcal{N}=(N_0,\ldots,N_k)`
     be a basis for the dual space `P'`.

   Then `(K,\mathcal{P},\mathcal{N})` is called a finite element.

For the cases considered in this course, `K` will be a polygon such as
a triangle, square, tetrahedron or cube, and `P` will be a space of
polynomials. Here, `P'` is the dual space to `P`, defined as the space of
linear functions from `P` to `\mathbb{R}`. Examples of dual functions
to `P` include:
#. The evaluation of `p\in P` at a point `x\in K`.
#. The integral of `p\in P` over a line `l\in K`.
#. The integral of `p\in P` over `K`.
#. The evaluation of a component of the derivative of `p\in P`
  at a point `x\in K`.

.. proof:exercise::
   Show that the four examples above are all linear functions from
  `P` to `\mathbb{R}`.

Ciarlet's finite element provides us with a standard way to define
a basis for the `P`, called the nodal basis.

.. proof:definition:: (local) nodal basis
   Let `(K,\mathcal{P},\mathcal{N})` be a finite element.
   The \emph{nodal basis} is the
   basis `\{\phi_0,\phi_2,\ldots,\phi_k\}` of `\mathcal{P}`
   that is dual to `\mathcal{N}`, \emph{i.e.}

   .. math::

      N_i(\phi_j) = \delta_{ij}, \quad 0\leq i,j \leq k.
