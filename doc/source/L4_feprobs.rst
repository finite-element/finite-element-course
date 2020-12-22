.. default-role:: math

Finite element problems: solvability and stability
===================================================

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490671279"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=fd348dc9-840d-41ac-8906-ac8f00b77a93>`_

In section 1, we saw the example of a finite element approximation
for Poisson's equation in the unit square, which we now recall below.

.. proof:definition::
  
   The finite element approximation `u_h \in \mathring{V}_h` to the
   solution `u_h` of Poisson's equation is defined by
   
   .. math::
      :label: eq:fe_poisson
	    
      \int_\Omega \nabla v \cdot \nabla u_h \, d x =
      \int_\Omega vf \, d x, \quad \forall v\in \mathring{V}_h.

A fundamental question is whether the solution `u_h` exists and is
unique. This question is of practical interest because if these
conditions are not satisfied, then the matrix-vector system for the
basis coefficients of `u_h` will not be solvable. To answer this
question for this approximation (and others for related equations), we
will use some general mathematical machinery about linear problems
defined on Hilbert spaces. It will turn out that this machinery will
also help us show that the approximation `u_h` converges to the exact
solution `u` (and in what sense).

Finite element spaces and other Hilbert spaces
----------------------------------------------

In the previous sections, we introduced the concept of finite element
spaces, which contain certain functions defined on a domain `\Omega`.
Finite element spaces are examples of vector spaces (hence the use
of the word "space").

.. proof:definition:: Vector space

   A vector space over the real numbers `\mathbb{R}` is a set `V`,
   with an addition operator `+:V\times V\to V`, plus a scalar
   multiplication operator `\times:\mathbb{R}\times V \to V`, such
   that:

  #. There exists a unique zero element `e\in V` such that:
    * `k\times e = e` for all `k\in \mathbb{R}`,
    * `0\times v = e` for all `v \in V`,
    * `e+v = v` for all `v \in V`.

  #. `V` is closed under addition and multiplication, i.e.,
    `a\times u + v\in V` for all `u,v\in V`, `a\in \mathbb{R}`.

.. proof:lemma::

   Let `V` be a finite element space. Then `V` is a vector space.

.. proof:proof::
   
   First, we note that the zero function `u(x):=0` is in `V`, and
   satisfies the above properties. Further, let `u,v\in V`, and
   `a\in\mathbb{R}`. Then, when restricted to each triangle `K_i`,
   `u+av\in P_i`. Also, for each shared mesh entity, the shared nodal
   variables agree, i.e. `N_{i,j}[u+av]=N_{i,j}[u+av]`, by linearity of
   nodal variables. Therefore, `u+av\in V`.

We now introduce bilinear forms on vector spaces. Bilinear forms are
important because they will represent the left hand side of finite
element approximations of linear PDEs.


.. proof:definition:: Bilinear form
		      
   A bilinear form `b(\cdot,\cdot)` on a vector space `V` is a mapping
   `b:V\times V\to \mathbb{R}`, such that

   #. `v\to b(v,w)` is a linear map in `v` for all `w`.      
   #. `v\to b(w,v)` is a linear map in `v` for all `w`.

  It is a symmetric bilinear form if in addition, `b(v,w)=b(w,v)`, for all `v,w\in V`.

Here are two important examples of bilinear forms on finite element spaces.
  
.. proof:example::

   Let `V_h` be a finite element space. The following are bilinear
   forms on `V_h`,

   .. math::

      b(u,v) &= \int_\Omega u  v \, d x, 

      b(u,v) &= \int_\Omega \nabla u \cdot \nabla v \, d x.

To turn a vector space into a Hilbert space, we need to select an
inner product.
   
.. proof:definition:: Inner product
		      
   A real inner product, denoted by `(\cdot,\cdot)`, is
   a symmetric bilinear form on a vector space `V` with

   #. `(v,v)\geq 0` `\forall v\in V`,
   #. `(v,v)=0\iff v=0`.

This enables the following definition.

.. proof:definition:: Inner product space
		      
   We call a vector space `(V, (\cdot,\cdot))` equipped with an inner product
   an inner product space.

We now introduce two important examples of inner products for finite
element spaces.

.. proof:definition:: \(L^2\) inner product
		      
   Let `f`, `g` be two functions in `L^2(\Omega)`. The `L^2` inner
   product between `f` and `g` is defined as

   .. math::

      ( f,g)_{L^2} = \int_{\Omega} fg \, d x.

The `L^2` inner product satisfies condition 2 provided that we
understand functions in `L^2` as being equivalence classes of
functions under the relation `f\equiv g \iff \int_\Omega (f-g)^2\, d
x=0`.

.. proof:definition:: \(H^1\) inner product

   Let `f`, `g` be two `C^0` finite element functions. The `H^1` inner
   product between `f` and `g` is defined as

   .. math::

      ( f,g)_{H^1} = \int_{\Omega} fg + \nabla f\cdot \nabla g \, d x.

The `H^1` inner product satisfies condition 2 since

.. math::

   ( f,f)_{L^2} \leq  ( f,f)_{H^1}.

The Schwarz inequality is a useful tool for bounding the size of inner
products.

.. proof:theorem:: Schwarz inequality
		   
   If `(V,(\cdot,\cdot))` is an inner product space, then

   .. math::

      |(u,v)| \leq (u,u)^{1/2}(v,v)^{1/2}.

   Equality holds if and only if `u=\alpha v` for some `\alpha\in\mathbb{R}`.

.. proof:proof::

   See a course on vector spaces.

Our solvability conditions will make use of norms that measure the
size of elements of a vector space (the size of finite element
functions, in our case).

.. proof:definition:: Norm

   Given a vector space `V`, a norm `\|\cdot\|` is a function from `V` to `\mathbb{R}`, with

   #. `\|v\|\geq 0,\,\forall v \in V`,
   #. `\|v\| = 0 \iff v=0`,
   #. `\|cv\|=|c|\|v\| \,\forall c\in \mathbb{R}, v\in V`,
   #. `\|v+w\| \leq \|v\|+\|w\|`.

For inner product spaces, there is a natural choice of norm.

.. proof:lemma::
   
   Let `(V,(\cdot,\cdot))` be an inner product space. Then `\|v\|=\sqrt{(v,v)}`
   defines a norm on `V`.

.. proof:proof::
   
   From bilinearity we have

   .. math::

      \|\alpha v\| = \sqrt{(\alpha v,\alpha v)} = \sqrt{\alpha^2( v,v)}=|\alpha|\|v\|,

   hence property 3.
   
   `\|v\|=( v,v)^{1/2} \geq 0`, hence property 1.

   If `0=\|v\|=( v,v)^{1/2} \implies (v,v)=0 \implies v=0`, hence property 2.

   We finally check the triangle inequality (property 4).

   .. math::

      \|u+v\|^2  &= (u+v,u+v)
      
      &= (u,u) + 2(u,v) + (v,v)
      
      &= \|u\|^2 + 2(u,v) + \|v\|^2
      
      &\leq \|u\|^2 + 2\|u\|\|v\| + \|v\|^2 \quad \mbox{[Schwarz]},
      
      &= (\|u\|+\|v\|)^2,

   hence `\|u+v\|\leq \|u\|+\|v\|`.

We introduce the following useful term.
   
.. proof:definition:: Normed space

   A vector space `V` with a norm `\|\cdot\|` is called a normed
   vector space, written `(V,\|\cdot\|)`.

To finish our discussion of Hilbert spaces, we need to review the
concept of completeness (which you might have encountered in an
analysis course). This seems not so important since finite element
spaces are finite dimensional, but later we shall consider sequences
of finite element spaces with smaller and smaller triangles, where
completeness becomes important.

Completeness depends on the notion of a Cauchy sequence.

.. proof:definition:: Cauchy sequence

   A Cauchy sequence on a normed vector space `(V,\|\cdot\|)` is a
   sequence `\{v_i\}_{i=1}^{\infty}` satisfying `\|v_j-v_k\|\to 0` as
   `j,k\to \infty`.

This definition leads to the definition of completeness.

.. proof:definition:: Complete normed vector space

   A normed vector space `(V,\|\cdot\|)` is complete if all Cauchy
   sequences have a limit `v\in V` such that `\|v-v_j\|\to 0`
   as `j\to\infty`.

Finally, we reach the definition of a Hilbert space.
   
.. proof:definition:: Hilbert space

   An inner product space `(V,(\cdot,\cdot))` is a Hilbert space if
   the corresponding normed space `(V,\|\cdot\|)` is complete.

All finite dimensional normed vector spaces are complete. Hence, `C^0`
finite element spaces equipped with `L^2` or `H^1` inner products are
Hilbert spaces. Later we shall understand our finite element
spaces as subspaces of infinite dimensional Hilbert spaces.

Linear forms on Hilbert spaces
------------------------------

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490671029"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=723914b3-4d55-476e-a8ef-ac8f00bca305>`_

We will now build some structures on Hilbert spaces that allow us to
discuss variational problems on them, which includes finite element
approximations such as the Poisson example discussed so far.

Linear functionals are important as they will represent the right-hand
side of finite element approximations of PDEs.

.. proof:definition:: Continuous linear functional

   Let `H` be a Hilbert space with norm `|\cdot|_H`.

   #. A functional `L` is a map from `H` to `\mathbb{R}`.
   #. A functional `L:H\to \mathbb{R}` is linear if `u,v\in H`, `\alpha\in \mathbb{R}` `\implies L(u+\alpha v)=L(u)+\alpha L(v)`.
   #. A functional `L:H\to\mathbb{R}` is continuous if there exists `C>0` such that

      .. math::

	 |L(u)-L(v)| \leq C\|u-v\|_H \quad \forall u,v\in H.

It is important that linear functionals are "nice" in the following sense.
      
.. proof:definition:: Bounded functional

   A functional `L:H\to\mathbb{R}` is bounded if there exists `C>0` such that

   .. math::

      |L(u)| \leq C\|u\|_H, \quad \forall u\in H.

For linear functionals we have the following relationship between boundedness
and continuity.
      
.. proof:lemma:: 

   Let `L:H\to\mathbb{R}` be a linear functional. Then `L` is continuous if and only if it is bounded.

.. proof:proof::

   `L` bounded `\implies L(u)\leq C\|u\|_{H} \implies |L(u)-L(v)| = |L(u-v)| \leq C\|u-v\|_{H} \, \forall u,v\in H,` i.e. `L` is continuous.

   On the other hand, `L` continuous `\implies |L(u-v)| \leq C\|u-v\|_{H}
   \quad \forall u,v\in H`. Pick `v=0`, then `|L(u)| = |L(u-0)| \leq
   C|u-0|_H = C|u|_H`, i.e. `L` is bounded.

We can also interpret bounded linear functionals as elements of a vector space.

.. proof:definition:: Dual space

   Let `H` be a Hilbert space. The dual space `H'` is the space of continuous (or bounded) linear functionals `L:H\to \mathbb{R}`.

This dual space can also be equipped with a norm.

.. proof:definition:: Dual norm

   Let `L` be a continuous linear functional on `H`, then

   .. math:: 

      \|L\|_{H'} = \sup_{0\neq v\in H}\frac{L(v)}{\|v\|_H}.

There is a simple mapping from `H` to `H'`.

.. proof:lemma:: 

   Let `u\in H`. Then the functional `L_u:H\to \mathbb{R}` defined by

   .. math::

      L_u(v) = (u,v), \quad \forall v\in H,

   is linear and continuous.

.. proof:proof::

   For `v,w\in H`, `\alpha\in\mathbb{R}` we have

   .. math::

      L_u(v+\alpha w) = (u,v+\alpha w) = (u,v) + \alpha(u,v) = L_u(v)
      + \alpha L_u(w).

   Hence `L_u` is linear.

   We see that `L_u` is bounded by Schwarz inequality,

   .. math::
      
      |L_u(v)| = |(u,v)| \leq C\|v\|_H \mbox{ with }C=\|u\|_H.

The following famous theorem states that the converse is also true.

.. proof:theorem:: Riesz representation theorem

   For any continuous linear functional `L` on `H` there exists `u\in H` such that

   .. math::

      L(v) = (u,v)\quad \forall v\in H.

   Further,

   .. math::

      \|u\|_H = \|L\|_{H'}.

.. proof:proof::

   See a course or textbook on Hilbert spaces.

Variational problems on Hilbert spaces
--------------------------------------

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490670887"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=bd3cfdc3-746d-42f4-96b5-ac8f00c44327>`_
We will consider finite element methods that can be formulated in the
following way.

.. proof:definition:: Linear variational problem
		      
   Let `b(u,v)` be a bilinear form on a Hilbert space `V`, and `F` be
   a linear form on `V`. This defines a linear variational problem: find
   `u\in V` such that

   .. math::

      b(u,v) = F(v), \quad \forall v\in V.  

We now discuss some important examples from finite element discretisations
of linear PDEs.
      
.. proof:example:: \(Pk\) discretisation of (modified) Helmholtz problem with Neumann bcs
		   
   For some known function `f`, 

   .. math::
   
      b(u,v) &= \int_\Omega uv + \nabla u \cdot \nabla v \, d x,

      F(v) &= \int_\Omega vf \, d x,

   and `V` is the Pk continuous finite element space on a triangulation
   of `\Omega`.

.. proof:example:: \(Pk\) discretisation of Poisson equation with partial Dirichlet bcs

   For some known function `f`, 

   .. math::
      
      b(u,v) &= \int_\Omega \nabla u \cdot \nabla v \, d x,

      F(v) &= \int_\Omega vf \, d x,

   and `V` is the subspace of the Pk continuous finite element space on a
   triangulation of `\Omega` such that functions vanishes on
   `\Gamma_0\subseteq \partial \Omega`.

.. proof:example:: \(Pk\) discretisation of Poisson equation with pure Neumann bcs

   For some known function `f`, 

   .. math::

      b(u,v) &= \int_\Omega \nabla u \cdot \nabla v \, d x,

      F(v) &= \int_\Omega vf \, d x,

   and `V` is the subspace of the Pk continuous finite element space on a
   triangulation of `\Omega` such that functions satisfy

   .. math::

      \int_\Omega u \, d x = 0.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490670764"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=39973b08-a56a-41e6-b1c8-ac8f00c5b325>`_
      
We now introduce two important properties of bilinear forms that determine
whether a linear variational problem is solvable or not. The first is
continuity.

.. proof:definition:: Continuous bilinear form

   A bilinear form is continuous on a Hilbert space `V` if there exists a
   constant `0<M<\infty` such that

   .. math::

      |b(u,v)| \leq M\|u\|_V\|v\|_V.

The second is coercivity.
      
.. proof:definition:: Coercive bilinear form
		      
   A bilinear form is coercive on a Hilbert space `V` if there exists a
   constant `0<\gamma<\infty` such that

   .. math::

      |b(u,u)| \geq \gamma\|u\|_V\|u\|_V.

These two properties combine in the following theorem providing sufficient
conditions for existence and uniqueness for solutions of linear variational
problems.

.. proof:theorem:: Lax-Milgram theorem

   Let `b` be a bilinear form, `F` be a linear form, and `(V,\|\cdot\|)` be a
   Hilbert space. If `b` is continuous and coercive, and `F` is continuous,
   then a unique solution `u\in V` to the linear variational problem exists,
   with

   .. math::

      \|u\|_V \leq \frac{1}{\gamma}\|F\|_{V'}.

.. proof:proof::

   See a course or textbook on Hilbert spaces.

We are going to use this result to show solvability for finite
element discretisations. In particular, we also want to know that our
finite element discretisation continues to be solvable as the maximum
triangle edge diameter `h` goes to zero. This motivates the following
definition.

.. proof:definition:: Stability

   Consider a sequence of triangulations `\mathcal{T}_h` with corresponding
   finite element spaces `V_h` labelled by a maximum triangle diameter
   `h`, applied to a variational problem with bilinear form `b(u,v)` and
   linear form `L`. For each `V_h` we have a corresponding coercivity constant
   `\gamma_h`.

   If `\gamma_h \to \gamma>0`, and `\|F\|_{V'_h}\to c <\infty`, then
   we say that the finite element discretisation is stable.

With this in mind it is useful to consider `h`-independent definitions
of `\|\cdot\|_V` (such as the `L^2` and `H^1` norms), which is why we
introduced them.

Solvability and stability of some finite element discretisations
-----------------------------------------------------------------

In this section we will introduce some tools for showing coercivity
and continuity of bilinear forms, illustrated with finite element
approximations of some linear PDEs where they may be applied.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490670624"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=eca48c8e-3823-4653-8b4e-ac8f00c7c5ce>`_

We start with the simplest example, for which continuity and
coercivity are immediate.

.. _thm-helm:

.. proof:theorem:: Solving the (modified) Helmholtz problem

   Let `b`, `L` be the forms from the Helmholtz problem, with
   `\|f\|_{L^2}<\infty`.  Let `V_h` be a Pk continuous finite element space
   defined on a triangulation `\mathcal{T}`. Then the finite element
   approximation `u_h` exists and the discretisation is stable
   in the `H^1` norm.

.. proof:proof::
   
   First we show continuity of `F`. We have

   .. math::

      F(v) = \int_\Omega fv \, d x \leq \|f\|_{L^2}\|v\|_{L^2}
      \leq \|f\|_{L^2}\|v\|_{H^1},

   since `\|v\|_{L^2}\leq \|v\|_{H^1}`.

   Next we show continuity of `b`.

   .. math::

      |b(u,v)| = |(u,v)_{H^1}| \leq 1\times\|u\|_{H^1}\|v\|_{H^1},

   from the Schwarz inequality of the `H^1` inner product.
   Finally we show coercivity of `b`.

   .. math::

      b(u,u) = \|u\|^2_{H^1} \geq 1\times\|u\|^2_{H^1},
      
   The continuity and coercivity constants are both 1, independent
   of `h`, so the discretisation is stable.

.. proof:exercise::
   
   Let `V` be a `C^0` finite element space on `[0,1]`, defined
   on a one-dimensional mesh with vertices `0=x_0<x_1<x_2<\ldots<x_{n-1}<x_n=1`. Show that
   `u\in V` satisfies the fundamental theorem of calculus, `i.e.`

   .. math::

      \int_0^1 u' \, d x = u[1] - u[0],
  
  where `u'` is the usual finite element derivative defined in `L^2([0,1])`
  by taking the usual derivative when restricting `u` to any subinterval
  `[x_k,x_{k+1}]`.

.. proof:exercise::
  
  Let

  .. math::
     
     a(u,v) = \int_0^1\left(u'v' + u'v + uv\right)\, d x.

  Let `V` be a `C^0` finite element space on `[0,1]` and let
  `\mathring{V}` be the subspace of functions that vanish at `x=0` and
  `x=1`.  Using the finite element version of the fundamental theorem of
  calculus above, prove that

  .. math::

     a(v,v) = \int_0^1\left((v')^2 + v^2\right)\, d x := \|v\|_{H^1}^2, \quad \forall v\in \mathring{V}.

  Hence conclude that the bilinear form is coercive on `\mathring{V}`.

.. proof:exercise::

   Consider the variational problem with bilinear form

   .. math::
   
      a(u,v) = \int_0^1 (u'v' + u'v + uv)\, d x,

   corresponding to the differential equation

   .. math::
      
      -u'' + u' + u = f.

   Prove that `a(\cdot,\cdot)` is continuous and coercive on a `C^0` finite element space `V` defined on `[0,1]`, with respect to the `H^1` inner product.

   Hints: for continuity, just use the triangle inequality and the
   relationship between `L^2` and `H^1` norms. For coercivity, try completing the square for the integrand in `a`.

..
  End of Week 7 material

For the Helmholtz problem, we have

.. math::
   
   b(u,v) = \int_\Omega uv + \nabla u\cdot \nabla v \, d x = (u,v)_{H^1},

i.e. `b(u,v)` is the `H^1` inner of `u` and `v`, which makes the
continuity and coercivity immediate.
  
For the Poisson problem, we have

.. math::

   b(u,u) = \int_\Omega |\nabla u|^2 \, d x = |u|^2_{H^1} \neq \|u\|^2_{H^1},
   
where we recall the `H^1` seminorm from the interpolation
section. Some additional results are required to show coercivity, as
`b(u,u)` is not the `H^1` norm squared any more. A seminorm has all
the properties of a norm except `|u|= 0 \nRightarrow u=0`, which is
precisely what is needed in the Lax-Milgram theorem.

.. _exe-pure-neumann:

.. proof:exercise::

   Let `\mathcal{T}_h` be a triangulation on the `1\times 1` unit
   square domain `\Omega`, and let `V` be a `C^0` Lagrange finite
   element space of degree `k` defined on `\mathcal{T}_h`. A finite element
   discretisation for the Poisson equation with Neumann boundary conditions
   is given by: find `u \in V` such that

  .. math::
     
     \int_{\Omega} \nabla v \cdot \nabla u \, d x = \int_\Omega v f \, d x,
     \quad \forall v \in V,
  
  for some known function `f`. Show that the bilinear form for this
  problem is not coercive in `V`.

For the Poisson problem, coercivity comes instead from the following
mean estimate.

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490670529"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e17f74a6-97ec-47fd-bcf4-ac8f00c9b784>`_

.. proof:lemma:: Mean estimate for finite element spaces

   Let `u` be a member of a `C^0` finite element space, and define

   .. math::

      \bar{u} = \frac{\int_\Omega u \, d x}{\int_\Omega \, d x}.

   Then there exists a positive constant `C`, independent of the
   triangulation but dependent on (convex) `\Omega`, such that 

   .. math::

      \|u-\bar{u}\|_{L^2} \leq C|u|_{H^1}.

.. Dropdown:: A video recording of the first part of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490670428"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=610a0d00-6e89-4e7f-a7d1-ac8f00cc9fe5>`_

.. Dropdown:: A video recording of the second part of section is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490670299"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=aac8613a-f8f2-474f-bbe5-ac8f00cdbc26>`_
      
.. proof:proof::

   (Very similar to the proof of the estimate for averaged Taylor polynomials.)
   
   Let `x` and `y` be two points in `\Omega`. We note that
   `f(s)=u(y+s(x-y))` is a `C^0`, piecewise polynomial function of
   `s`. Let `s_0 = 0 < s_1 < s_2 < \ldots < s_{k-1} < s_k = 1` denote the points
   where `y+s(x-y)` intersects a triangle edge or vertex. Then
   `f` is a continuous function when restricted to each interval `[s_i,s_{i+1}]`, `i=0,\ldots,k-1`. This means that

   .. math::

      f(s_{i+1}) - f(s_i) &= \int_{s_i}^{s_{i+1}} f'(s) \, ds

      &= \int_{s_i}^{s_{i+1}} (x-y)\cdot\nabla u(y+s(x-y)) \, ds,

   where `\nabla u` is the finite element derivative of `u`. Summing
   this up from `i=0` to `i=k-1`, we obtain

   .. math::
      
      u(x)=u(y) +\int_0^1
      (x-y)\cdot\nabla u(y+s(x-y))\, d s.

   Then

   .. math::
   
      u(x)-\bar{u} &= \frac{1}{|\Omega|}\int_{\Omega}u(x)-u(y)\, d y 

      &= \frac{1}{|\Omega|}\int_{\Omega}(x-y)\cdot \int_{s=0}^1 \nabla u(y + s(x-y)) \, d s\, d y,

   Therefore

   .. math::

      \|u-\bar{u}\|^2_{L^2(\Omega)}  &=  \frac{1}{|\Omega|^2}\int_{\Omega}
      \left(\int_\Omega (x-y)\cdot\int_{s=0}^1 \nabla u(y + s(x-y))\, d s
      \, d y\right)^2 \, d x,
      
      &\leq  \frac{1}{|\Omega|^2}\int_{\Omega}
      \int_\Omega |x-y|^2 \, d y
      \int_\Omega  \int_{s=0}^1 |\nabla u(y + s(x-y))|^2\, d s
      \, d y \, d x,  

      &\leq  C\int_{\Omega}
      \int_\Omega  \int_{s=0}^1 |\nabla u(y + s(x-y))|^2\, d s
      \, d y \, d x.

   We split this final quantity into two parts (to avoid singularities),

   .. math::

      \|u-\bar{u}\|^2_{L^2(\Omega)} \leq C(I + II),

   where

   .. math::
   
      I  &= \int_\Omega \int_{s=0}^{1/2} \int_\Omega
      | \nabla u(y+s(x-y))|^2 \, d y \, d s \, d x,
      
      II  &= \int_\Omega \int_{s=1/2}^2 \int_\Omega
      | \nabla u(y+s(x-y))|^2 \, d x \, d s \, d y,

   which we will now estimate separately.

   To evaluate `I`, change variables `y \to y' = y + s(x-y)`,
   defining `\Omega'_s\subset \Omega` as the image of `\Omega`
   under this transformation. Then,

   .. math::

      I &= \int_\Omega \int_{s=0}^{1/2} \frac{1}{(1-s)^2}
      \int_{\Omega'_s} |\nabla u(y')|^2 \, d y' \, d s \, d x,
      
      &\leq \int_\Omega \int_{s=0}^{1/2} \frac{1}{(1-s)^2}
      \int_{\Omega} |\nabla u(y')|^2 \, d y' \, d s \, d x, 

      &= \frac{|\Omega|}{2} |\nabla u|^2_{H^1(\Omega)}.

   To evaluate `II`, change variables `x \to x' = y + s(x-y)`,
   defining `\Omega'_s\subset \Omega` as the image of `\Omega`
   under this transformation. Then,

   .. math::
   
      II &= \int_\Omega \int_{s=1/2}^2 \frac{1}{s^2}
      \int_{\Omega'_s} |\nabla u(x')|^2 \, d x' \, d s \, d y, 

      &\leq \int_\Omega \int_{s=0}^{1/2} \frac{1}{s^2}
      \int_{\Omega} |\nabla u(x')|^2 \, d x' \, d s \, d y,
   
      &=|\Omega| |\nabla u|^2_{H^1(\Omega)}.

   Combining,

   .. math::
      
      \|u-\bar{u}\|^2_{L^2(\Omega)} \leq C(I + II) = \frac{3C|\Omega|}{2}
      |u|_{H^1(\Omega)}^2,

   which has the required form.

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490670236"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=9652e5bd-ef4a-45e8-9a41-ac8f00ceae9d>`_
   
The mean estimate can now be used to show solvability for the Poisson
problem with pure Neumann conditions.

.. proof:theorem:: Solving the Poisson problem with pure Neumann conditions

   Let `b`, `L`, `V`, be the forms for
   the pure Neumann Poisson problem, with
   `\|f\|_{L^2}<\infty`.  Let `V_h` be a Pk continuous finite element space
   defined on a triangulation `\mathcal{T}`, and define

   .. math::

      \bar{V}_h = \{u\in V_h:\bar{u}=0\}.
      
   Then for `\bar{V}_h`, the finite element approximation `u_h` exists and the
   discretisation is stable in the `H^1` norm.

.. proof:proof::
   
   Using the mean estimate, for `u\in\bar{V}_h`, we have

   .. math::
      
      \|u\|_{L^2}^2=\|u-\underbrace{\bar{u}}_{=0}\|^2_{L^2} \leq C^2|u|_{H^1}^2.

   Hence we obtain the coercivity result,

   .. math::
      
      \|u\|_{H^1}^2 = \|u\|_{L^2}^2 + |u|_{H^1}^2 \leq (1+C^2)|u|_{H^1}^2 = (1+C^2)b(u,u).

   Continuity follows from Schwarz inequality,

   .. math::
      
      |b(u,v)| \leq |u|_{H^1}|v|_{H^1} \leq \|u\|_{H^1}\|v\|_{H^1}.

The coercivity constant is independent of `h`, so the approximation is stable.

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490669992"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=58a9dd17-1ae8-4b9e-9781-ac8f0101a3c3>`_

Proving the coercivity for the Poisson problem with Dirichlet or
partial Dirichlet boundary conditions requires some additional
results. We start by showing that the divergence theorem also applies
to finite element derivatives of `C^0` finite element functions.

.. proof:lemma:: Finite element divergence theorem

   Let `\phi` be a `C^1` vector-valued function.
   and `u\in V` be a member of a `C^0` finite element space.  Then

   .. math::

      \int_{\Omega} \nabla\cdot(\phi u)\, d x = \int_{\partial\Omega}
      \phi\cdot n u\, d S,

   where `n` is the outward pointing normal to `\partial\Omega`.

.. proof:proof::

   .. math::
      
      \int_\Omega\nabla\cdot(\phi u)\, d x  &= \sum_{K\in \mathcal{T}}
      \int_K \nabla\cdot(\phi u)\, d x,
   
      &= \sum_{K\in \mathcal{T}} \int_{\partial K}\phi\cdot n_K u\, d S,

      &= \int_{\partial\Omega} \phi\cdot n u\, d S
      + \underbrace{\int_\Gamma \phi\cdot(n^++n^-)u\, d S}_{=0}.

This allows us to prove the finite element trace theorem, which
relates the `H^1` norm of a `C^0` finite element function to the `L^2`
norm of the function restricted to the boundary.

.. proof:theorem:: Trace theorem for continuous finite elements

   Let `V_h` be a continuous finite element space, defined on a triangulation `\mathcal{T}`, on a polygonal domain `\Omega`. Then

   .. math::

      \|u\|_{L^2(\partial\Omega)} \leq C\|u\|_{H^1(\Omega)},

   where `C` is a constant that depends only on the geometry of
   `\Omega`.

.. proof:proof:: 

   The first step is to construct a `C^1` function `\xi` satisfying
   `\xi\cdot n=1` on `\Omega`. We do this by finding a triangulation
   `\mathcal{T}_0` (unrelated to `\mathcal{T}`), and defining an `C^1`
   Argyris finite element space `V_0` on it. We then choose `\xi` so that
   both Cartesian components are in `V_0`, satisfying the boundary
   condition.

   Then,

   .. math::
   
      \|u\|_{L^2(\partial\Omega)}^2 &=
      \int_{\partial\Omega} u^2 \, d S  = \int_{\partial\Omega}\xi\cdot n u^2\, d S,

      &= \int_\Omega \nabla\cdot (\xi u^2)\, d x,
      
      &= \int_\Omega u^2 \nabla\cdot \xi + 2u\xi\cdot\nabla u \, d x,
      
      &\leq \|u\|_{L^2}^2\|\nabla\cdot\xi\|_{\infty} + 2|\xi|_{\infty}
      \|u\|_{L^2}|u|_{H^1},

   So,

   .. math::
   
      \|u\|_{L^2(\partial\Omega)}^2   &\leq \|u\|_{L^2}^2\|\nabla\cdot\xi\|_{\infty} + |\xi|_{\infty}
      \left(\|u\|_{L^2}^2 + |u|_{H^1}^2\right),
      
      &\leq C\|u\|_{H^1}^2,

   where we have used the geometric-arithmetic mean inequality `2ab \leq
   a^2+b^2`. 

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490669782"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=1bc37dc7-ef3e-43f5-b111-ac8f010287cf>`_
   
We can now use the trace inequality to estabilish solvability for the
Poisson problem with (full or partial) Dirichlet conditions.
      
.. proof:theorem:: Solving the Poisson problem with partial Dirichlet conditions
      
   Let `b`, `L`, `V`, be the forms for
   the (partial) Dirichlet Poisson problem, with
   `\|f\|_{L^2}<\infty`.  Let `V_h` be a Pk continuous finite element space
   defined on a triangulation `\mathcal{T}`, and define

   .. math::

      \mathring{V}_h = \{u\in V_h:u|_{\Gamma_0}\}.

   Then for `\mathring{V}_h`, the finite element approximation `u_h` exists and the discretisation is stable in the `H^1` norm.

.. proof:proof::

   [Proof taken from Brenner and Scott]. We have

   .. math::
   
      \|v\|_{L^2(\Omega)}  &\leq \|v-\bar{v}\|_{L^2(\Omega)} + \|\bar{v}\|_{L^2(\Omega)},
      
      &\leq C|v|_{H^1(\Omega)} + \frac{|\Omega|^{1/2}}{|\Gamma_0|}
      \left|\int_{\Gamma_0}\bar{v}\, d S\right|,
 
      &\leq C|v|_{H^1(\Omega)} + \frac{|\Omega|^{1/2}}{|\Gamma_0|}
      \left(\left|\int_{\Gamma_0}v\, d S + \int_{\Gamma_0}\bar{v}-v\, d S\right|\right).

   We have

   .. math::
   
      \left|
      \int_{\Gamma_0} (v-\bar{v})\, d s
      \right|  \leq |\Gamma_0|^{1/2}\|v-\bar{v}\|_{L^2(\partial\Omega)},
      
      \leq |\Gamma_0|^{1/2}C |v|_{H^1(\Omega)}.

   Combining, we get

   .. math::

      \|v\|_{L^2(\Omega)} \leq C_1|v|_{H^1(\Omega)},

   and hence coercivity,

   .. math::
      
      \|v\|_{H^1(\Omega)}^2 \leq (1+C_1^2)b(v,v).

The coercivity constant is independent of `h`, so the approximation is stable.

.. proof:exercise::
   
   For `f\in L^2(\Omega)`, `\sigma\in C^1(\Omega)`, find a finite element
   formulation of the problem

   .. math::
   
      -\sum_{i=1}^n \frac{\partial}{\partial x_i}\left(\sigma(x)\frac{\partial u}{\partial x_i}\right) = f, 
      \quad \frac{\partial u}{\partial n}=0\mbox{ on }\partial\Omega.

   If there exist `0<a<b` such that `a<\sigma(x)<b` for all `x\in
   \Omega`, show continuity and coercive for your formulation
   with respect to the `H^1` norm.

.. proof:exercise::

   Find a `C^0` finite element formulation for the Poisson equation 

   .. math::
      
      -\nabla^2 u = f, \quad u=g \mbox{ on }\partial \Omega,

   for a function `g` which is `C^2` and whose restriction to
   `\partial\Omega` is in `L^2(\partial\Omega)`.
   Derive conditions under the discretisation 
   has a unique solution.  

In this section, We have developed some techniques for showing that
variational problems arising from finite element discretisations for
Helmholtz and Poisson problems have unique solutions, that are stable
in the `H^1`-norm. This means that we can be confident that we can
solve the problems on a computer and the solution won't become
singular as the mesh is refined. Now we would like to go further and
ask what is happening to the numerical solutions as the mesh is
refined. What are they converging to?

We will address these questions in the next section.

..
  end of Week 8 material
