.. default-role:: math

Finite element spaces: local to global
======================================

In this section, we discuss the construction of general finite element
spaces. Given a triangulation `\mathcal{T}` of a domain `\Omega`, finite
element spaces are defined according to

#. the form the functions take (usually polynomial) when restricted to each cell (a triangle, in the case considered so far),
#. the continuity of the functions between cells.

We also need a mechanism to explicitly build a basis for the finite
element space. We first do this by looking at a single cell, which we
call the local perspective. Later we will take the global perspective,
seeing how function continuity is enforced between cells.

Ciarlet's finite element
------------------------

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490693460"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e79807c3-c73b-42ec-b5f9-ac8d00c7b4c6>`_

The first part of the definition is formalised by Ciarlet's definition
of a finite element.

.. proof:definition:: Ciarlet's finite element

   Let

   #. the element domain `K\subset \mathbb{R}^n` be some bounded closed set with piecewise smooth boundary,
   #. the space of shape functions `\mathcal{P}` be a finite dimensional space of functions on `K`, and
   #. the set of nodal variables `\mathcal{N}=(N_0,\ldots,N_k)` be a basis for the dual space `P'`.

   Then `(K,\mathcal{P},\mathcal{N})` is called a finite element.

For the cases considered in this course, `K` will be a polygon such as a triangle, square, tetrahedron or cube, and `P` will be a space of polynomials. Here, `P'` is the dual space to `P`, defined as the space of linear functions from `P` to `\mathbb{R}`. Examples of dual functions to `P` include:

#. The evaluation of `p\in P` at a point `x\in K`.
#. The integral of `p\in P` over a line `l\in K`.
#. The integral of `p\in P` over `K`.
#. The evaluation of a component of the derivative of `p\in P` at a point `x\in K`.

.. proof:exercise::
   
   Show that the four examples above are all linear functions from `P` to `\mathbb{R}`.

.. proof:exercise::
   
   For a domain `K` and shape space `P`, is the following
   functional a nodal variable? Explain your answer.

   .. math::

      N_0(p) = \int_K p^2 \,d x.
   
Ciarlet's finite element provides us with a standard way to define a basis for the `P`, called the nodal basis.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490693258"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=9d432870-a298-4e6e-b495-ac8d00cc6411>`_

.. proof:definition:: (local) nodal basis
		      
   Let `(K,\mathcal{P},\mathcal{N})` be a finite element. The nodal basis is the basis `\{\phi_0,\phi_2,\ldots,\phi_k\}` of `\mathcal{P}` that is dual to `\mathcal{N}`, i.e.

   .. math::

      N_i(\phi_j) = \delta_{ij}, \quad 0\leq i,j \leq k.

We now introduce our first example of a Ciarlet element.

.. _1d_lagrange:

.. proof:definition:: The 1-dimensional Lagrange element
		    
   The 1-dimensional Lagrange element `(K,\mathcal{P},\mathcal{N})` of
   degree `k` is defined by

   #. `K` is the interval `[a,b]` for `-\infty<a<b<\infty`.
   #. `\mathcal{P}` is the (`k+1`)-dimensional space of degree `k` polynomials on `K`,
   #. `\mathcal{N}=\{N_0,\ldots,N_k\}` with

   .. math::
      
      N_i(v) = v(x_i), \, x_i = a + (b-a)i/k, \quad \forall v\in \mathcal{P},\,
      i=0,\ldots,k.

.. _exe-1d-lagrange-basis:
      
.. proof:exercise:: 

   Show that the nodal basis for `\mathcal{P}` is given by
   
   .. math::
      
      \phi_i(x) = \frac{\prod_{j=0,j\ne i}^k (x-x_j)}{\prod_{j=0,j\ne i}^k (x_i-x_j)}, \quad i=0,\ldots,k.

..
  end of week 2 material
      
Vandermonde matrix and unisolvence
----------------------------------

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490693083"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f3fb54fb-f83e-41b8-a537-ac8d00d03589>`_

More generally, It is useful computationally to write the nodal basis
in terms of another arbitrary basis `\{\psi_i\}_{i=0}^k`. This
transformation is represented by the Vandermonde matrix.

.. _def-vandermonde:

.. proof:definition:: Vandermonde matrix

   Given a dual basis `\mathcal{N}` and a basis `\{\psi_i\}_{i=0}^k`,
  the Vandermonde matrix is the matrix `V` with coefficients

   .. math::
  
      V_{ij} = N_j(\psi_i).

This relationship is made clear by the following lemma.

.. _lemma-vandermonde:

.. proof:lemma::
      
   The expansion of the nodal basis `\{\phi_i\}_{i=0}^k` in terms
   of another basis `\{\psi_i\}_{i=0}^k` for `\mathcal{P}`,

   .. math::
   
      \phi_i(x) = \sum_{j=0}^k \mu_{ij}\psi_j(x),

   has coefficients `\mu_{ij}`, `0\leq i,j\leq k` given by

   .. math::
   
      \mu = V^{-1},
      
   where `\mu` is the corresponding matrix.

.. proof:proof::
   
   The nodal basis definition becomes

   .. math::
   
      \delta_{ij} =  N_j(\phi_i) = \sum_{l=0}^k\mu_{il}N_j(\psi_l) = \sum_{l=0}^k \mu_{il}V_{lj} = (\mu V)_{ij},

   where `\mu` is the matrix with coefficients `\mu_{ij}`, and `V` is the matrix with coefficients `N_j(\psi_i)`.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490692882"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=6f9d4bb7-4a90-40f7-8eae-ac8d00ce8ac7>`_

.. proof:exercise::

   Consider the following finite element.

   * `K` is the interval `[0,1]`.
   * `P` is the quadratic polynomials on `K`.
   * The nodal variables are:

     .. math::

	N_0[p] = p(0), \, N_1[p]=p(1), \, N_2=\int_0^1 p(x) \,d x.

   Find the corresponding nodal basis.
    
Given a triple `(K,\mathcal{P},\mathcal{N})`, it is necessary to
verify that `\mathcal{N}` is indeed a basis for `\mathcal{P}'`,
i.e. that the Ciarlet element is well-defined. Then the nodal basis is
indeed a basis for `\mathcal{P}` by construction. The following lemma
provides a useful tool for checking this.

.. _dual_condition:

.. proof:lemma:: dual condition

   Let `K,\mathcal{P}` be as defined above, and let `\{N_0,N_1,\ldots,N_k\}\in \mathcal{P}'`. Let `\{\psi_0,\psi_1,\ldots,\psi_k\}` be a basis for `\mathcal{P}`.

   Then the following three statements are equivalent.

   #. `\{N_0,N_1,\ldots,N_k\}` is a basis for `\mathcal{P}'`.
   #. The Vandermonde matrix with coefficients

      .. math::

         V_{ij} = N_j(\psi_i), \, 0\leq i,j\leq k,

      is invertible.
   #. If `v\in\mathcal{P}` satisfies `N_i(v)=0` for `i=0,\ldots,k`, then `v\equiv 0`.

.. proof:proof::

   Let `\{N_0,N_1,\ldots,N_k\}` be a basis for `\mathcal{P}'`. This is
   equivalent to saying that given element `E` of `\mathcal{P}'`, we
   can find basis coefficients `\{e_i\}_{i=0}^k\in \mathbb{R}` such
   that

   .. math::
	   
      E = \sum_{i=0}^k e_iN_i.

   This in turn is equivalent to being able to find a vector
   `e=(e_0,e_1,\ldots,e_k)^T` such that

   .. math::
   
      b_i = E(\psi_i) = \sum_{j=0}^k e_j N_j(\psi_i) = \sum_{j=0}^k e_jV_{ij},

   i.e. the equation `V{e}={b}` is solvable. This means that (1) is
   equivalent to (2).

   On the other hand, we may expand any `v\in \mathcal{P}` according to

   .. math::
   
      v(x) = \sum_{i=0}^k f_i \psi_i(x).

   Then

   .. math::
  
      N_i(v)=0 \iff \sum_{j=0}^k f_jN_i(\psi_j) = 0, \quad i=0,1,\ldots,k,

   by linearity of `N_i`. So (2) is equivalent to

   .. math::
   
      \sum_{j=0}^k f_jN_i(\psi_j) = 0, \quad i=0,1,\ldots,k \implies
    f_j=0, \, j=0,1,\ldots,k,

   which is equivalent to `V^T` being invertible, which is equivalent to
   `V` being invertible, and so (3) is equivalent to (2).
   
.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490692719"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=97d9a7b6-7837-4591-9180-ac8e0099484c>`_
   
This result leads us to introducing the following terminology.

.. proof:definition:: Unisolvence.

   We say that `\mathcal{N}` determines `\mathcal{P}` if it satisfies
   condition 3 of :numref:`Lemma {number}<dual_condition>`. If
   this is the case, we say that `(K,\mathcal{P},\mathcal{N})` is
   unisolvent.

We can now go and directly apply this lemma to the 1D Lagrange elements.
   
.. proof:corollary::
   
   The 1D degree `k` Lagrange element is a finite element.

.. proof:proof::
   
   Let `(K,\mathcal{P},\mathcal{N})` be the degree `k` Lagrange
   element. We need to check that `\mathcal{N}` determines
   `\mathcal{P}`. Let `v\in \mathcal{P}` with `N_i(v)=0` for all
   `N_i\in \mathcal{N}`. This means that

   .. math::
   
      v(a+(b-a)i/k)=0, \, i=,0,1,\ldots,k,

   which means that `v` vanishes at `k+1` points in `K`. Since `v` is
   a degree `k` polynomial, it must be zero by the fundamental theorem
   of algebra.

.. proof:exercise::

   Consider the following proposed finite element.

   * `K` is the interval `[0,1]`.
   * `P` is the linear polynomials on `K`.
   * The nodal variables are:

     .. math::

	N_0[p] = p(0.5), N_1=\int_0^1 p(x) \,d x.

   Is this finite element unisolvent? Explain your answer.

   
2D and 3D finite elements
-------------------------

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490692347"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e5501a7d-81f1-47f1-8000-ac8d00ce89fb>`_

We would like to construct some finite elements with 2D and 3D domains
`K`. The fundamental theorem of algebra does not directly help us
there, but the following lemma is useful when checking that
`\mathcal{N}` determines `\mathcal{P}` in those cases.

.. proof:lemma::

   Let `p(x):\mathbb{R}^d\to\mathbb{R}` be a polynomial of degree `k\geq 1`
   that vanishes on a hyperplane `\Pi_L` defined by

   .. math::
   
      \Pi_L = \left\{ x: L(x)=0\right\},

   for a non-degenerate affine function `L(x):\mathbb{R}^d\to
   \mathbb{R}`.  Then `p(x)=L(x)q(x)` where `q(x)` is a polynomial of
   degree `k-1`.

.. proof:proof::

   Choose coordinates (by shifting the origin and applying a linear
   transformation) such that `x=(x_1,\ldots,x_d)` with `L(x)=x_d`, so
   `\Pi_L` is defined by `x_d=0`.  Then the general form for a
   polynomial is

   .. math::

      P(x_1,\ldots,x_d) = \sum_{i_d=0}^k
      \left(\sum_{|i_1+\ldots+i_{d-1}|\leq
        k-i_d}c_{i_1,\ldots,i_{d-1},i_d} x_d^{i_d}\prod_{l=1}^{d-1}
      x_{l}^{i_l}\right),

   Then, `p(x_1,\ldots,x_{d-1},0)=0` for all `(x_1,\ldots,x_{d-1})`,
   so

   .. math::
   
      0 = \left(\sum_{|i_1+\ldots+i_{d-1}|\leq k}c_{i_1,\ldots,i_{d-1},0} \prod_{l=1}^{d-1}x_{l}^{i_l}\right)

   which means that

   .. math::
   
      c_{i_1,\ldots,i_{d-1},0} = 0, \quad \forall |i_1+\ldots+i_{d-1}|\leq k.

   This means we may rewrite

   .. math::
  
      P(x) = {L(x)}\underbrace{\left(\sum_{i_d=1}^k\sum_{|i_1+\ldots+i_{d-1}|\leq k - i_d}c_{i_1,\ldots,i_{d-1},i_d} x_d^{i_d-1}\prod_{l=1}^{d-1} x_{l}^{i_l}\right)},

      P(x) = \underbrace{x_d}_{L(x)}\underbrace{\left(\sum_{i_d=0}^{k-1}\sum_{|i_1+\ldots+i_{d-1}|\leq k - i_d}c_{i_1,\ldots,i_{d-1},i_d} x_d^{i_d-1}\prod_{l=1}^{d-1} x_{l}^{i_l}\right)}_{Q(x)},

   with `\deg(Q)=k-1`.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490692245"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=b2674f92-8a03-4685-98e7-ac8e00a15a88>`_

.. proof:exercise::

   The following polynomial vanishes on the line `y=-1-x`. Show that
   it satisfies the result of the previous theorem.

   .. math::

      x^{5} + 5 x^{4} y - x^{4} + 6 x^{3} y^{2} - 4 x^{3} y - 2 x^{2}
      y^{3} - 2 x^{2} y^{2} - 3 x y^{4} + 4 x y^{3} + y^{5} - y^{4}

Equipped with this tool we can consider some finite elements in two
dimensions.

.. proof:definition:: Lagrange elements on triangles

   The triangular Lagrange element of degree `k`
   `(K,\mathcal{P},\mathcal{N})`, denoted `Pk`, is defined as follows.

   #. `K` is a (non-degenerate) triangle with vertices `z_1`, `z_2`, `z_3`.
   #. `\mathcal{P}` is the space of degree `k` polynomials on `K`.
   #. `\mathcal{N}=\left\{N_{i,j}:0\leq i \leq k, \, 0\leq j \leq i\right\}` defined by `N_{i,j}(v)=v(x_{i,j})` where

   .. math::
      
      x_{i,j} = z_1 + (z_2-z_1)\frac{i}{k} + (z_3-z_1)\frac{j}{k}.

We illustrate this for the cases `k=1,2`.
      
.. proof:example:: P1 elements on triangles
		   
   The nodal basis for P1 elements is point evaluation at the three vertices.

.. proof:example:: P2 elements on triangles
		   
   The nodal basis for P2 elements is point evaluation at the three
   vertices, plus point evaluation at the three edge centres.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490692065"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=1d6a0060-361f-4c03-af32-ac8d00cc637e>`_
   
We now need to check that that the degree `k` Lagrange element is a
finite element, i.e. that `\mathcal{N}` determines `\mathcal{P}`. We will
first do this for `P1`.

.. _P1unisolve:

.. proof:lemma::

  The degree `1` Lagrange element on a triangle `K` is a finite element.

.. proof:proof::
  
   Let `\Pi_1`, `\Pi_2`, `\Pi_3` be the three lines containing the
   vertices `z_2` and `z_3`, `z_1` and `z_3`, and `z_1` and `z_3`
   respectively, and defined by `L_1=0`, `L_2=0`, and `L_3=0`
   respectively. Consider a linear polynomial `p` vanishing at `z_1`,
   `z_2`, and `z_3`. The restriction `p|_{\Pi_1}` of `p` to `\Pi_1` is
   a linear function vanishing at two points, and therefore `p=0` on
   `\Pi_1`, and so `p=L_1(x)Q(x)`, where `Q(x)` is a degree 0
   polynomial, i.e. a constant `c`. We also have

   .. math::
   
      0 = p(z_1) = cL_1(z_1) \implies c=0,

   since `L_1(z_1)\neq 0`, and hence `p(x)\equiv 0`. This means
   that `\mathcal{N}` determines `\mathcal{P}`.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490691995"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

..
  end of week 3 material
	    
    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=5fbdc104-9b38-4e7f-9c61-ac8d00c7d4ac>`_

.. proof:exercise::

   Let `K` be a rectangle, `P` be the polynomial space spanned by
   `\{1, x, y, xy\}`, let `\mathcal{N}` be the set of dual elements
   corresponding to point evaluation at each vertex of the
   rectangle. Show that `\mathcal{N}` determines the finite element.

.. proof:exercise::

   Let `K` be a triangle, and `P` be the space of quadratic
   polynomials. Let `N` be the set of nodal variables given by point
   evaluation at each edge midpoint together with the nodal variables
   given by integral of the function along each edge. Show that `N`
   does not determine `P`.

This technique can then be extended to degree 2.
   
.. proof:lemma::

   The degree `2` Lagrange element is a finite element.

.. proof:proof::
   
   Let `p` be a degree `2` polynomial with `N_i(p)` for all of the
   degree `2` dual basis elements. Let `\Pi_1`, `\Pi_2`, `\Pi_3`,
   `L_1`, `L_2` and `L_3` be defined as for the proof of Lemma
   . `p|_{\Pi_1}` is a degree 2 scalar polynomial vanishing
   at 3 points, and therefore `p=0` on `\Pi_1`, and so
   `p(x)=L_1(x)Q_1(x)` with `\deg(Q_1)=1`. We also have `0=p|_{\Pi_2}
   =L_1Q_1|_{\Pi_2}`, so `Q_1|_{\Pi_2}=0` and we conclude that
   `p(x)=cL_1(x)L_2(x)`. Finally, `p` also vanishes at the midpoint of
   `L_3`, so we conclude that `c=0` as required.

The technique extends further to degree 3.
   
.. proof:exercise::
   
   Show that the degree `3` Lagrange element is a finite element.

Going beyond degree 3, we have more than 1 nodal variable taking point
evaluation inside the triangle. To deal with this, we use the nested
triangular structure of the Lagrange triangle.

.. _lem-degk-unisolve:

.. proof:lemma::
   
   The degree `k` Lagrange element is a finite element for `k>3`.

.. proof:proof::
   
   We prove by induction. Assume that the degree `k-3` Lagrange
   element is a finite element. Let `p` be a degree `k` polynomial
   with `N_i(p)` for all of the degree `k` dual basis elements. Let
   `\Pi_1`, `\Pi_2`, `\Pi_3`, `L_1`, `L_2` and `L_3` be defined as for
   the proof of :numref:`lemma {number}<P1unisolve>`. The restriction
   `p|_{\Pi_1}` is a degree `k` polynomial in one variable that
   vanishes at `k+1` points, and therefore `p(x)=L_1(x)Q_1(x)`, with
   `\deg(Q_1)=k-1`. `p` and therefore `Q` also vanishes on `\Pi_2`, so
   `Q_1(x)=L_2(x)Q_2(x)`.

   Repeating the argument
   again means that `p(x)=L_1(x)L_2(x)L_3(x)Q_3(x)`, with `\deg(Q_3)=k-3`.
   `Q_3` must vanish on the remaining points in the interior of `K`, which
   are arranged in a smaller triangle `K'` and correspond to the evaluation
   points for a degree `k-3` Lagrange finite element on `K'`. From
   the inductive hypothesis, and using the results for `k=1,2,3`, we conclude
   that `Q_3\equiv=0`, and therefore `p\equiv0` as required.

Some more exotic elements
-------------------------

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490691590"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=495e54dd-23b6-4d92-bcdb-ac8e00ab3829>`_

We now consider some finite elements that involve derivative
evaluation. The Hermite elements involve evaluation of first
derivatives as well as point evaluations.

.. proof:definition:: Cubic Hermite elements on triangles

   The cubic Hermite element is defined as follows:
   
   #. `K` is a (nondegenerate) triangle,
   #. `\mathcal{P}` is the space of cubic polynomials on `K`,
   #. `\mathcal{N}=\{N_1,N_2,\ldots,N_{10}\}` defined as follows:
      
      * `(N_1,\ldots,N_3)`: evaluation of `p` at vertices,
      * `(N_4,\ldots,N_9)`: evaluation of the gradient of `p` at the 3 triangle vertices.
      * `N_{10}`: evaluation of `p` at the centre of the triangle.

It turns out that the Hermite element is insufficient to guarantee
functions with continuous derivatives between triangles. This problem
is solved by the Argyris element.
	
.. proof:definition:: Quintic Argyris elements on triangles
	 
  The quintic Argyris element is defined as follows:

  #. `K` is a (nondegenerate) triangle,
  #. `\mathcal{P}` is the space of quintic polynomials on `K`,
  #. `\mathcal{N}` defined as follows:
     
     * evaluation of `p` at 3 vertices,
     * evaluation of gradient of `p` at 3 vertices,
     * evaluation of Hessian of `p` at 3 vertices,
     * evaluation of the gradient normal to 3 triangle edges.
       
Global continuity
-----------------

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490691454"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f384b387-f65a-4f9e-a582-ac8e00b8760e>`_

Next we need to know how to glue finite elements together to form
spaces defined over a triangulation (mesh). To do this we need to
develop a language for specifying connections between finite element
functions between element domains.

.. proof:definition:: Finite element space

   Let `\mathcal{T}` be a triangulation made of triangles `K_i`, with
   finite elements `(K_i,\mathcal{P}_i,\mathcal{N}_i)`. A space `V` of
   functions on `\mathcal{T}` is called a finite element space if for
   each `u\in V`, and for each `K_i\in\mathcal{T}`, `u|_{K_i}\in
   \mathcal{P}_i`.
   
Note that the set of finite elements do not uniquely determine a
finite element space, since we also need to specify continuity
requirements between triangles, which we will do in this chapter.

.. proof:definition:: Finite element space
		      
   A finite element space `V` is a `C^m` finite element space if `u\in
   C^m` for all `u\in V`.

The following lemma guides use in how to inspect the continuity of
finite element functions.
   
.. _cty:		      
.. proof:lemma:: Continuity lemma
		 
   Let `\mathcal{T}` be a triangulation on `\Omega`, and let
   `V` be a finite element space defined on `\mathcal{T}`.
   The following two statements are equivalent.
   
   #. `V` is a `C^m` finite element space. 
   #. The following two conditions hold.
      
     * For each vertex `z` in `\mathcal{T}`, let `\{K_i\}_{i=1}^m` be the set of triangles that contain `z`. Then `u|_{K_1}(z)=u|_{K_2}(z)=\ldots = u|_{K_m}(z)`, for all functions `u\in V`, and similarly for all of the partial derivatives of degrees up to `m`.
     * For each edge `e` in `\mathcal{T}`, let `K_1`, `K_2` be the two triangles containing `e`. Then `u|_{K_1}(z) = u|_{K_2}(z)`, for all points `z` on the interior of `e`, and similarly for all of the partial derivatives of degrees up to `m`.

.. proof:proof::
   
   `V` is polynomial on each triangle `K`, so continuity at points on
   the interior of each triangle `K` is immediate. We just need to
   check continuity at points on vertices, and points on the interior
   of edges, which is equivalent to the two parts of the second
   condition.

This means that we just need to guarantee that the polynomial
functions and their derivatives agree at vertices and edges (similar
ideas extend to higher dimensions). We achieve this by assigning nodal
variables (and their associated nodal basis functions) appropriately
to vertices, edges etc. of each triangle `K`. First we need to
introduce this terminology.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490691352"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=22aab3d8-2041-4c42-9d18-ac8e00be66ab>`_

.. proof:definition:: local and global mesh entities

   Let `K` be a triangle. The local mesh entities of `K` are the
   vertices, the edges, and `K` itself. The global mesh entities of a
   triangulation `\mathcal{T}` are the vertices, edges and triangles
   comprising `\mathcal{T}`.

Having made this definition, we can now talk about how nodal variables
can be assigned to local mesh entities in a geometric decomposition.
   
.. proof:definition:: local geometric decomposition

   Let `(K,\mathcal{P},\mathcal{N})` be a finite element. We say that
   the finite element has a (local) geometric decomposition if each
   dual basis function `N_i` can be associated with a single mesh
   entity `w\in W` such that for any `f\in\mathcal{P}`, `N_i(f)` can be
   calculated from `f` and derivatives of `f` evaluated on `w`.

.. proof:exercise::

   Consider the finite element defined by:

   #. `K` is the unit interval `[0,1]`
   #. `P` is the space of quadratic polynomials on `K`,
   #. The nodal variables are:

      .. math::
	 
	 N_0[v] = v(0), N_1[v] = v(1), N_2[v] = \int_0^1 v(x)\,d x.

  Find the corresponding nodal basis for `P` in terms of the monomial
  basis `\{1, x, x^2\}`. Provide the `C^0` geometric decomposition for
  the finite element (demonstrating that it is indeed `C^0`).

   
.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490691251"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=9f363ae5-0174-4fe1-94e9-ac8e00e7f271>`_
   
To discuss `C^m` continuity, we need to introduce some further
vocabulary about the topology of `K`.
   
.. proof:definition:: closure of a local mesh entity

   Let `w` be a local mesh entity for a triangle. The closure of `w` is
   the set of local mesh entities contained in `w` (including `w`
   itself).

This allows us to define the degree of continuity of the local
geometric decomposition.
   
.. proof:definition:: \(C^m\) geometric decomposition

   Let `(K,\mathcal{P},\mathcal{N})` be a finite element with
   geometric decomposition `W`. We say that `W` is a `C^m` geometric
   decomposition, if for each local mesh entity `w`, for any `f\in
   \mathcal{P}`, the restriction `f|_w` of `f` (and the restriction
   `D^kf|_w` of the `k`-th derivative of `f` to `w` for `k\leq m`) can
   be obtained from the set of dual basis functions associated with
   entities in the closure of `w`, applied to `f`.

The idea behind this definition is that if two triangles `K_1` and
`K_2` are joined at a vertex, with finite elements
`(K_1,\mathcal{P}_1, \mathcal{N}_1)` and `(K_2, \mathcal{P}_2,
\mathcal{N}_2)`, then if the `\mathcal{N}_1` variables associated with
the vertex applied to a function `u` agree with the corresponding
`\mathcal{N}_2` variables also associated with that vertex also
applied to `u`, then the function `u` will be `C^m` continuous through
the vertex. Similarly, if `K_1` and `K_2` are joined at an edge, then
if the corresponding `\mathcal{N}_1` and `\mathcal{N}_2` nodal
variables associated with that edge agree when applied to `u`, then
`u` will be `C^m` continuous through that edge. We just need to define
these correspondences.

We explore this definition through a couple of exercises.

.. proof:exercise::
   
   Show that the Lagrange elements of degree `k` have `C^0` geometric decompositions.

.. _exer-argyris:
   
.. proof:exercise::
   
   Show that the Argyris element has a `C^1` geometric decomposition.
   
.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490691153"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

..
  end of week 4 material
	    
    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3d816037-2cb7-4eb2-b441-ac8e00ea1551>`_
   
We now use the geometric decomposition to construct global finite
element spaces over the whole triangulation (mesh). We just need to
define what it means for elements of the nodal variables from the
finite elements of two neighbouring triangles to "correspond".

We start by considering spaces of functions that are discontinuous
between triangles, before defining `C^m` continuous subspaces.

.. proof:definition:: Discontinuous finite element space
   
   Let `\mathcal{T}` be a triangulation, with finite elements
   `(K_i,P_i,\mathcal{N}_i)` for each triangle `K_i`.  The associated
   discontinuous finite element space `V`, is defined as
   
   .. math::

      V = \left\{u: u|_{K_i} \in P_i, \, \forall K_i \in \mathcal{T}\right\}.

   This defines families of discontinuous finite element spaces.
   
.. proof:example:: Discontinuous Lagrange finite element space

   Let `\mathcal{T}` be a triangulation, with Lagrange elements of
   degree `k`, `(K_i,P_i,\mathcal{N}_i)`, for each triangle `K_i\in
   \mathcal{T}`. The corresponding discontinuous finite element space,
   denoted `Pk` DG, is called the discontinuous Lagrange finite element
   space of degree `k`.
   
Next we need to associate each nodal variable in each element to a
vertex, edge or triangle of the triangulation `\mathcal{T}_h`,
i.e. the global mesh entitles. The following definition explains how
to choose this association.

.. proof:definition:: Global \(C^m\) geometric decomposition

    Let `\mathcal{T}` be a triangulation with finite elements
    `(K_i,\mathcal{P}_i,\mathcal{N}_i)`, each with a `C^m` geometric
    decomposition. Assume that for each global mesh entity `w`, the
    `n_w` triangles containing `w` have finite elements
    `(K_i,\mathcal{P}_i,\mathcal{N}_i)` each with `M_w` dual basis
    functions associated with `w`.  Further, each of these basis
    functions can be enumerated `N^w_{i,j}\in\mathcal{N}_i`,
    `j=1,\ldots,M_w`, such that
    `N^w_{1,j}(u|_{K_1})=N^w_{2,j}(u|_{K_2})=\ldots =
    N^w_{n_w,j}(u|_{K_n}), \quad, j=1,\ldots,M_w`, for all functions
    `u\in C^m(\Omega)`.

    This combination of finite elements on `\mathcal{T}` together with
    the above enumeration of dual basis functions on global mesh
    entities is called a global `C^m` geometric decomposition.

Now we use this global `C^m` geometric decomposition to build a
finite element space on the triangulation.
   
.. proof:definition:: Finite element space from a global \(C^m\) geometric decomposition

   Let `\mathcal{T}` be a triangulation with finite elements
   `(K_i,\mathcal{P}_i,\mathcal{N}_i)`, each with a `C^m` geometric
   decomposition, and let `\hat{V}` be the corresponding
   discontinuous finite element space. Then the global `C^m`
   geometric decomposition defines a subspace `V` of `\hat{V}`
   consisting of all functions that `u` satisfy
   `N^w_{1,j}(u|_{K_1})=N^w_{2,j}(u|_{K_2})=\ldots = N^w_{n_w,j}(u|_{K_{n_w}}), \quad j=1,\ldots,M_w` for all mesh entities `w\in\mathcal{T}`.

The following result shows that the global `C^m` geometric
decomposition is a useful definition.
   
.. proof:lemma::

   Let `V` be a finite element space defined from a global `C^m` geometric decomposition. Then `V` is a `C^m` finite element space.

.. proof:proof::
   
   From the local `C^m` decomposition, functions and derivatives up
   to degree `m` on vertices and edges are uniquely determined from
   dual basis elements associated with those vertices and edges, and
   from the global `C^m` decomposition, the agreement of dual basis
   elements means that functions and derivatives up to degree `m`
   agree on vertices and edges, and hence the functions
   are in `C^m` from :numref:`Lemma {number}<cty>`.

We now apply this to a few examples, which can be proved as exercises.
   
.. proof:example::
   
   The finite element space built from the `C^0` global decomposition
   built from degree `k` Lagrange element is called the degree `k` continuous Lagrange finite element space, denoted `Pk`.

.. proof:example::
   
   The finite element space built from the `C^1` global decomposition
   built from the quintic Argyris element is called the Argyris finite
   element space.
   
In this section, we have built a theoretical toolbox for the
construction of finite element spaces. In the next section, we move on
to studying how well we can approximate continuous functions as finite
element functions.
