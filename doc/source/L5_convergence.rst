.. default-role:: math

Convergence of finite element approximations
============================================

In this section we develop tools to prove convergence of finite
element approximations to the exact solutions of PDEs.

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490669563"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=5d2d1721-725f-43ef-bcdd-ac8f01056006>`_

Weak derivatives
----------------

Consider a triangulation `\mathcal{T}` with recursively refined
triangulations `\mathcal{T}_h` and corresponding finite element spaces
`V_h`.  Given stable finite element variational problems, we have a
sequence of solutions `u_h` as `h\to 0`, satisfying the
`h`-independent bound

.. math::
      
   \|u_h\|_{H^1(\Omega)} \leq C.

What are these solutions converging to? We need to find a Hilbert
space that contains all `V_h` as `h\to0`, that extends the `H^1` norm
to the `h\to 0` limit of finite element functions.

Our first task is to define a derivative that works for all finite
element functions, without reference to a mesh. This requires some
preliminary definitions, starting by considering some very smooth
functions that vanish on the boundaries together with their
derivatives (so that we can integrate by parts as much as we like).

.. proof:definition:: Compact support on \(\Omega\)

   A function `u` has compact support on `\Omega` if there exists `\epsilon>0`
   such that `u(x)=0` when `\min_{y\in\partial\Omega}|x-y|<\epsilon`.

.. proof:definition:: \(C^\infty_0(\Omega)\)
   
   We denote by `C^\infty_0(\Omega)` the subset of `C^\infty(\Omega)`
   corresponding to functions that have compact support on
   `\Omega`.

Next we will define a space containing the generalised derivative.

.. proof:definition:: \(L^1_{loc}\)
		      
   For triangles `K \subset \mathrm{int}\,(\Omega)`, we define

   .. math::

      \|u\|_{L^1(K)} = \int_K |u|\, d x,

   and

   .. math::

      L^1_K = \left\{u:\|u\|_{L^1(K)}<\infty\right\}.

   Then

   .. math::

      L^1_{loc} = \left\{
      f: f \in L^1(K) \quad \forall K\subset\mathrm{int}\,(\Omega)
      \right
      \}.

Finally we are in a position to introduce the generalisation of the
derivative itself.
      
.. proof:definition:: Weak derivative
		      
   The weak derivative `D_w^\alpha f\in L^1_{loc}(\Omega)` of a function `f\in L^1_{loc}(\Omega)` is defined by

   .. math::
   
      \int_\Omega \phi D_w^\alpha f \, d x = (-1)^{|\alpha|}
      \int_\Omega D^\alpha \phi f \, d x, \quad \forall \phi\in C^\infty_0(\Omega).

Not that we do not see any boundary terms since `\phi` vanishes at the
boundary along with all derivatives.
      
Now we check that the derivative agrees with our finite element derivative
definition.

.. proof:lemma::

   Let `V` be a `C^0` finite element space. Then, for `u\in V`, the finite
   element derivative of u is equal to the weak
   derivative of `u`.

.. proof:proof:: 

   Taking any `\phi\in C_0^\infty(\Omega)`, we have

   .. math::

      \int_\Omega
      \phi \frac{\partial}{\partial x_i}|_{FE}u \, d x  = \sum_{K}\int_K \phi \frac{\partial u}{\partial x_i}\, d x,
      
      &= \sum_K\left(-\int_K \frac{\partial \phi}{\partial x_i} u \, d x + \int_{\partial K}
      \phi n_i u \, d S\right),

      &= -\sum_K\int_K \frac{\partial\phi}{\partial x_i} u \, d x = -\int_\Omega
      \frac{\partial \phi}{\partial x_i} u \, d x,

   as required.

.. proof:exercise::

   Let `V` be a `C^1` finite element space. For `u\in V`, show that the finite
   second derivatives of u is equal to the weak
   second derivative of `u`.

.. proof:exercise::


   Let `V` be a discontinuous finite element space. For `u\in V`, show
   that the weak derivative does not coincide with the finite element
   derivative in general (find a counter-example).
   
.. proof:lemma:: 

   For `u\in C^{|\alpha|}(\Omega)`, the usual ``strong'' derivative
   `D^\alpha` of u is equal to the weak derivative `D_w^\alpha` of `u`.

.. proof:exercise::

   Prove this lemma.

Due to these equivalences, we do not need to distinguish between
strong, weak and finite element first derivatives for `C^0` finite
element functions. All derivatives are assumed to be weak from now on.


Sobolev spaces
--------------

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490880876"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=ab4667ea-fb50-461e-940f-ac8f010c13fa>`_

We are now in a position to define a space that contains all `C^0`
finite element spaces. This means that we can consider the limit
of finite element approximations as `h\to 0`.

.. proof:definition:: The Sobolev space \(H^1\)

   `H^1(\Omega)` is the function space defined by

   .. math::

      H^1(\Omega) = \left\{
      u\in L^1_{loc}: \|u\|_{H^1(\Omega)}<\infty\right\}.

Going further, the Sobolev space `H^k` is the space of all functions
with finite `H^k` norm.
      
.. proof:definition:: The Sobolev space \(H^k\)

   `H^k(\Omega)` is the function space defined by
   
   .. math::

      H^k(\Omega) = \left\{
      u\in L^1_{loc}: \|u\|_{H^k(\Omega)}<\infty\right\}

Since `\|u\|_{H^k(\Omega)} \leq \|u\|_{H^l(\Omega)}` for `k<l`,
we have `H^k \subset H^l` for `k<l`.
      
If we are to consider limits of finite element functions in these
Sobolev spaces, then it is important that they are closed, i.e.
limits remain in the spaces.

.. proof:lemma:: \(H^k\) spaces are Hilbert spaces

   The space `H^k(\Omega)` is closed.

   Let `\{u_i\}` be a Cauchy sequence in `H^k`. Then `\{D^\alpha u_i\}`
   is a Cauchy sequence in `L^2(\Omega)` (which is closed), so `\exists
   v^\alpha \in L^2(\Omega)` such that `D^\alpha u_i\to v^\alpha` for
   `|\alpha|\leq k`.  If `w_j\to w` in `L^2(\Omega)`, then for `\phi\in
   C^\infty_0(\Omega)`,

   .. math::

      \int_\Omega (w_j-w)\phi \, d x \leq \|w_j-w\|_{L^2(\Omega)}\|\phi\|_{L^\infty}\to 0.

   We use this equation to get

   .. math::
      
      \int_\Omega v^\alpha \phi \, d x  &= \lim_{i\to \infty} \int_\Omega
      \phi D^\alpha u_i \, d x,
      
      &= \lim_{i\to \infty} (-1)^{|\alpha|}\int_\Omega u_i D^\alpha\phi \, d x ,
 
      &= (-1)^{|\alpha|} \int_\Omega v D^\alpha \phi \, d x,

   i.e. `v^\alpha` is the weak derivative of `u` as required.

We quote the following much deeper results without proof.

.. proof:theorem:: \(H=W\)

   Let `\Omega` be any open set. Then `H^k(\Omega)\cap C^\infty(\Omega)`
   is dense in `H^k(\Omega)`.

The interpretation is that for any function `u\in H^k(\Omega)`,
we can find a sequence of `C^\infty` functions `u_i` converging
to `u`. This is very useful as we can compute many things using
`C^\infty` functions and take the limit.

.. _sobolev:

.. proof:theorem:: Sobolev's inequality

   Let `\Omega` be an `n`-dimensional domain with Lipschitz boundary, let
   `k` be an integer with `k>n/2`. Then there exists a constant
   `C` such that

   .. math::

      \|u\|_{L^\infty(\Omega)} = \mathrm{ess}\sup_{x\in \Omega}|u(x)|
      \leq C\|u\|_{H^k(\Omega)}.

   Further, there is a `C^0` continuous function in the `L^\infty(\Omega)`
   equivalence class of `u`.

Previously we saw this result for continuous functions. Here it is
presented for `H^k` functions, with an extra statement about the
existence of a `C^0` function in the equivalence class. The
interpretation is that if `u\in H^k` then there is a continuous
function `u_0` such that the set of points where `u\neq u_0` has zero
area/volume.

.. proof:corollary:: Sobolev's inequality for derivatives

   Let `\Omega` be a `n`-dimensional domain with Lipschitz boundary, let
   `k` be an integer with `k-m>n/2`. Then there exists a constant
   `C` such that

   .. math::

      \|u\|_{W_\infty^m(\Omega)} :=
      \sum_{|\alpha|\leq m}\|D^\alpha u\|_{L^\infty(\Omega)}
      \leq C\|u\|_{H^k(\Omega)}.

   Further, there is a `C^m` continuous function in the `L^\infty(\Omega)`
   equivalence class of `u`.

.. proof:proof::

   Just apply Sobolev's inequality to the `m` derivatives of `u`.


Variational formulations of PDEs
--------------------------------

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490669306"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=4ac5a081-3109-4b2f-86df-ac8f010fa52c>`_

We can now consider linear variational problems defined on `H^k`
spaces, by taking a bilinear form `b(u,v)` and linear form
`F(v)`, seeking `u\in H^k` (for chosen `H^k`) such that

.. math::

   b(u,v) = F(v), \quad \forall v \in H^k.

Since `H^k` is a Hilbert space, the Lax-Milgram theorem can be used to
analyse, the existence of a unique solution to an `H^k` linear
variational problem.

For example, the Helmholtz problem solvability is immediate.

.. proof:theorem:: Well-posedness for (modified) Helmholtz)

   The Helmholtz variational problem on `H^1` satisfies the conditions
   of the Lax-Milgram theorem.

.. proof:proof::

   The proof for `C^0` finite element spaces extends immediately
   to `H^1`.

Next, we develop the relationship between solutions of the Helmholtz
variational problem and the strong-form Helmholtz equation,

.. math::

   u - \nabla^2 u = f, \quad \frac{\partial u}{\partial n} = 0, \mbox{ on } \partial\Omega.

The basic idea is to check that when you take a solution of the
Helmholtz variational problem and integrate by parts (provided that
this makes sense) then you reveal that the solution solves the strong
form equation. Functions in `H^k` make boundary values hard to
interpret since they are not guaranteed to have defined values on the
boundary.  We make the following definition.

.. proof:definition:: Trace of \(H^1\) functions

   Let `u\in H^1(\Omega)` and choose `u_i\in C^\infty(\Omega)` such
   that `u_i\to u`. We define the trace `u|_{\partial\Omega}`
   on `\partial\Omega` as the limit of the restriction of `u_i` to
   `\partial\Omega`. This definition is unique from the uniqueness of
   limits.

We can extend our trace inequality for finite element functions directly
to `H^1` functions.

.. proof:lemma:: Trace theorem for \(H^1\) functions
		 
   Let `u \in H^1(\Omega)` for a polygonal domain `\Omega`. Then the
   trace `u|_{\partial\Omega}` satisfies 

   .. math::

      \|
      u\|_{L^2(\partial\Omega)} \leq C\|u\|_{H^1(\Omega)}.  

The interpretation of this result is that if `u\in H^1(\Omega)` then
`u|_{\partial\Omega}\in L^2(\partial\Omega)`.
      
.. proof:proof::
   
   Adapt the proof for `C^0` finite element functions, choosing `u\in
   C^\infty(\Omega)`, and pass to the limit in `H^1(\Omega)`. 

This tells us when the integration by parts formula makes sense.
   
.. proof:lemma::
   
   Let `u\in H^2(\Omega)`, `v\in H^1(\Omega)`. Then

   .. math::
      \int_\Omega (-\nabla^2 u)v \, d x
      = \int_\Omega \nabla u\cdot\nabla v \, d x - \int_{\partial \Omega}
      \frac{\partial u}{\partial n} v\, d S.

.. proof:proof::

   First note that `u\in H^2(\Omega)\implies \nabla u \in (H^1(\Omega))^d`.
   Then

   .. math

      \| v\nabla u\|_{H^1(\Omega)} \leq  \|v\|_{H^1(\Omega)}\|\nabla u\|_{H^1(\Omega)}
      \implies v\nabla u \in H^1(\Omega).

   Then, take `v_i\in C^\infty(\Omega)` and `u_i\in C^\infty(\Omega)` converging
   to `v` and `u`, respectively, and `v_i\nabla u_i\in C^\infty(\Omega)` converges
   to `v\nabla u`. These satisfy the equation;
   we obtain the result by passing to the limit.

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490668791"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=11a1d9f5-c1e9-41c1-9207-ac8f01127eac>`_
   
Now we have everything we need to show that solutions of the strong
form equation also solve the variational problem. It is just a matter
of substituting into the formula and applying integration by parts.
   
.. proof:lemma::

   For `f\in L^2`,
   let `u\in H^2(\Omega)` solve

   .. math::
      
      u - \nabla^2 u = f, \quad \frac{\partial u}{\partial n} = 0 \mbox{ on } \partial\Omega,

   in the `L^2` sense, i.e. `\|u-\nabla^2 u - f\|_{L^2}=0`. Then
   `u` solves the variational form of the Helmholtz equation.

.. proof:proof::
   
   `u\in H^2\implies \|u\|_{H^2}<\infty\implies \|u\|_{H^1}<\infty\implies
   u\in H^1`. Multiplying by test function `v\in H^1`, and using the
   previous proposition gives

   .. math::
      
      \int_\Omega uv + \nabla u\cdot\nabla v\, d x = \int_\Omega fv \, d x, 
      \quad \forall v \in H^1(\Omega),

   as required.

Now we go the other way, showing that solutions of the variational
problem also solve the strong form equation. To do this, we need to
assume a bit more smoothness of the solution, that it is in `H^2`
instead of just `H^1`.
   
.. proof:theorem::
   
   Let `f\in L^2(\Omega)` and suppose that `u\in H^2(\Omega)` solves the
   variational Helmholtz equation on a polygonal domain `\Omega`. Then
   `u` solves the strong form Helmholtz equation with zero Neumann
   boundary conditions.

.. proof:proof::

   Using integration by parts for `u\in H^2`, `v\in C^\infty_0(\Omega)\in
   H^1`, we have

   .. math::
   
      \int_\Omega (u-\nabla^2 u -f)v\, d x = \int_\Omega uv + \nabla u\cdot\nabla
      v - vf \, d x = 0.

   It is a standard result that `C^\infty_0(\Omega)` is dense in `L^2(\Omega)`
   (i.e., every `L^2` function can be approximated arbitrarily closely by
   a `C^\infty_0` function),
   and therefore we can choose a sequence of v converging to `u-\nabla^2 u - f`
   and we obtain `\|u-\nabla^2 u -f \|_{L^2(\Omega)}=0`.

   Now we focus on showing the boundary condition is satisfied.
   We have

   .. math::
      0 = \int_\Omega uv + \nabla u \cdot \nabla v - fv \, d x

      &= \int_\Omega uv + \nabla u \cdot \nabla v - (u-\nabla^2u)v \, d x

      &= \int_{\partial\Omega} \frac{\partial u}{\partial n}v\, d S.

   We can find arbitrary `v\in L_2(\partial\Omega)`, hence
   `\|\frac{\partial u}{\partial n}\|_{L^2(\partial\Omega)}=0`.

Galerkin approximations of linear variational problems
------------------------------------------------------

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490668756"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=63ad7174-ffe3-44bf-bd94-ac8f011498d9>`_

Going a bit more general again, assume that we have a well-posed
linear variational problem on `H^k`, connected to a strong form
PDE. Now we would like to approximate it. This is done in general
using the Galerkin approximation.
   
.. proof:definition:: Galerkin approximation

   Consider a linear variational problem of the form:

   find `u \in H^k` such that

   .. math::

      b(u,v) = F(v), \quad \forall v \in H^k.
		      
   For a finite element space `V_h\subset V=H^k(\Omega)`, the Galerkin
   approximation of this `H^k` variational problem
   seeks to find `u_h\in V_h` such that

   .. math::

      b(u_h,v) = F(v), \quad \forall v \in V_h.

We just restrict the trial function `u` and the test function `v` to
the finite element space. `C^0` finite element spaces are subspaces of
`H^1`, `C^1` finite element spaces are subspaces of `H^2` and so on.

If `b(u,v)` is continuous and coercive on `H^k`, then it is also
continuous and coercive on `V_h` by the subspace property. Hence,
we know that the Galerkin approximation exists, is unique and is
stable. This means that it will be possible to solve the matrix-vector
equation.

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490668557"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=5c5e4671-ddb4-4cf2-afce-ac8f01165ff0>`_

..
  end of Week 9 material
    
Moving on, if we can solve the equation, we would like to know if it is
useful. What is the size of the error `u-u_h`? For Galerkin approximations
this question is addressed by Céa's lemma.

.. _thm-cea:

.. proof:theorem:: Céa's lemma.
   
   Let `V_h\subset V`, and let `u` solve a linear variational problem
   on `V`, whilst `u_h` solves the equivalent Galerkin approximation
   on `V_h`. Then

   .. math::
      \|u-u_h\|_V \leq \frac{M}{\gamma}\min_{v\in V_h}
      \|u-v\|_V,

   where `M` and `\gamma` are the continuity and coercivity constants
   of `b(u,v)`, respectively.

.. proof:proof::

   We have

   .. math::
   
      b(u,v) = F(v) \quad \forall v \in V, 
      b(u_h,v)  = F(v) \quad \forall v \in V_h.

   Choosing `v\in V_h\subset V` means we can use it in both equations,
   and subtraction and linearity lead to the ``Galerkin orthogonality''
   condition

   .. math::
   
      b(u-u_h,v) = 0, \quad \forall v\in V_h.

   Then, for all `v\in V_h`,

   .. math::
      
      \gamma\|u-u_h\|^2_V &\leq b(u-u_h,u-u_h),
   
      &= b(u-u_h,u-v) + \underbrace{b(u-u_h,v-u_h)}_{=0},

      &\leq M\|u-u_h\|_V\|u-v\|_V.

   So,

   .. math::

      \gamma\|u-u_h\|_V \leq M|u-v\|_V.
      
   Minimising over all `v` completes the proof.

Interpolation error in `H^k` spaces
-----------------------------------

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490668426"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=b473bf39-8d5b-4d2f-b051-ac8f01192b68>`_

The interpretation of Céa's lemma is that the error is proportional to
the minimal error in approximating `u` in `V_h`. To do this, we can
simply choose `v = \mathcal{I}_hu` in Céa's lemma, to get

.. math::
   \|u-u_h\|_V \leq \frac{M}{\gamma}\min_{v\in V_h}
   \|u-v\|_V \leq \frac{M}{\gamma}\|u - \mathcal{I}_hu\|_V.

Hence, Céa's lemma reduces the problem of estimating the error in the
numerical solution to estimating error in the interpolation of the
exact solution.  We have already examined this in the section on
interpolation operators, but in the context of continuous
functions. The problem is that we do not know that the solution `u` is
continuous, only that it is in `H^k` for some `k`.

We now quickly revisit the results of the interpolation section to
extend them to `H^k` spaces. The proofs are mostly identical, so we just
give the updated result statements and state how to modify the proofs.

Firstly we recall the averaged Taylor polynomial. Since it involves
only integrals of the derivatives, we can immediately use weak
derivatives here.

.. proof:definition:: Averaged Taylor polynomial with weak derivatives

   Let `\Omega\subset \mathbb{R}^n` be a domain with diameter `d`, that
   is star-shaped with respect to a ball `B` with radius `\epsilon`,
   contained within `\Omega`. For `f\in H^{k+1}(\Omega)` the
   averaged Taylor polynomial `Q_{k,B}f\in \mathcal{P}_k` is defined
   as

   .. math::
   
      Q_{k,B} f(x) = \frac{1}{|B|}\int_{B} T^kf(y,x) \, d y,

   where `T^kf` is the Taylor polynomial of degree `k` of `f`,

   .. math::
      T^k f(y,x) = \sum_{|\alpha|\leq k} D^\alpha f(y)\frac{(x-y)^\alpha}{\alpha!},

   evaluated using weak derivatives.

This definition makes sense since the Taylor polynomial coefficients
are in `L^1_{loc}(\Omega)` and thus their integrals over `B` are defined.

The next step was to examine the error in the Taylor polynomial.

.. proof:theorem::
   
   Let `\Omega\subset \mathbb{R}^n` be a domain with diameter `d`, that
   is star-shaped with respect to a ball `B` with radius `\epsilon`,
   contained within `\Omega`. There exists a constant `C(k,n)` such that
   for `0\leq |\beta| \leq k+1` and all `f \in H^{k+1}(\Omega)`,

   .. math::

      \|D^\beta(f-Q_{k,B}f)\|_{L^2} \leq C\frac{|\Omega|^{1/2}}{|B|^{1/2}}
      d^{k+1-|\beta|}\|\nabla^{k+1}f\|_{L^2(\Omega)}.

.. proof:proof::

   To show this, we assume that `f\in C^\infty(\Omega)`, in which case
   the result of :numref:`Theorem {number}<taylorerror>` applies. Then
   we obtain the present result by approximating `f` by a sequence of
   `C^\infty(\Omega)` functions and passing to the limit.
   
We then repeat the following corollary.

.. proof:corollary::
   
   Let `K_1` be a triangle with diameter `1`.
   There exists a constant `C(k,n)` such that

   .. math::
      
      \|f-Q_{k,B}f\|_{H^k(K_1)} \leq C|\nabla^{k+1}f|_{H^{k+1}(K_1)}.

.. proof:proof::

   Same as :numref:`Lemma {number}<unittaylorerr>`.
      
The next step was the bound on the interpolation operator. Now we just
have to replace `C^{l,\infty}` with `W^l_\infty` as derivatives may not
exist at every point.


.. proof:lemma::
   
   Let `(K_1,\mathcal{P},\mathcal{N})` be a finite element such that
   `K_1` is a triangle with diameter 1, and such that the nodal
   variables in `\mathcal{N}` involve only evaluations of functions or
   evaluations of derivatives of degree `\leq l`, and `\|N_i\|_{W^l_\infty(K_1)'}
   <\infty`, 

   .. math::
   
      \|N_i\|_{W_\infty^l(K_1)'} = \sup_{\|u\|_{W_\infty^l(K_1)}>0}
      \frac{|N_i(u)|}{\|u\|_{W_\infty^l(K_1)}}.

   Let `u\in H^k(K_1)` with
   `k>l+n/2`. Then

   .. math::

      \|\mathcal{I}_{K_1}u\|_{H^k(K_1)} \leq C\|u\|_{H^k(K_1)}.

.. proof:proof::

   Same as :numref:`Lemma {number}<Ibound>`. replacing `C^{l,\infty}`
   with `W^l_\infty`, and using the full version of the Sobolev
   inequality in :numref:`Lemma {number}<sobolev>`.

The next steps then just follow through.

.. proof:lemma::
   
   Let `(K_1,\mathcal{P},\mathcal{N})` be a finite element such that
   `K_1` has diameter `1`, and such that the nodal variables in
   `\mathcal{N}` involve only evaluations of functions or evaluations of
   derivatives of degree `\leq l`, and `\mathcal{P}` contain all
   polynomials of degree `k` and below, with `k>l+n/2`. Let `u\in
   H^{k+1}(K_1)`. Then for `i \leq k`, the local interpolation operator
   satisfies

   .. math::
      |\mathcal{I}_{K_1}u-u|_{H^i(K_1)} \leq C_1|u|_{H^{k+1}(K_1)}.

.. proof:proof::

   Same as :numref:`Lemma {number}<IerrK1>`.
      
.. proof:lemma::

   Let `(K,\mathcal{P},\mathcal{N})` be a finite element such that
   `K` has diameter `d`, and such that the nodal variables in
   `\mathcal{N}` involve only evaluations of functions or evaluations of
   derivatives of degree `\leq l`, and `\mathcal{P}` contains all
   polynomials of degree `k` and below, with `k>l+n/2`. Let `u\in
   H^{k+1}(K)`. Then for `i \leq k`, the local interpolation operator
   satisfies

   .. math::

      |\mathcal{I}_{K}u-u|_{H^i(K)} \leq C_Kd^{k+1-i}|u|_{H^{k+1}(K)}.

   where `C_K` is a constant that depends on the shape of `K` but not
   the diameter.

.. proof:proof::

   Repeat the scaling argument of :numref:`Lemma {number}<scaling>`.

.. proof:theorem::
   
   Let `\mathcal{T}` be a triangulation with finite elements
   `(K_i,\mathcal{P}_i,\mathcal{N}_i)`, such that the minimum aspect
   ratio `r` of the triangles `K_i` satisfies `r>0`, and such that the
   nodal variables in `\mathcal{N}` involve only evaluations of functions
   or evaluations of derivatives of degree `\leq l`, and `\mathcal{P}`
   contains all polynomials of degree `k` and below, with `k>l+n/2`. Let
   `u\in H^{k+1}(\Omega)`.  Let `h` be the maximum over all of the
   triangle diameters, with `0\leq h<1`. Let `V` be the corresponding
   `C^r` finite element space.  Then for `i\leq k` and `i \leq r+1`, the
   global interpolation operator satisfies

   .. math::

      \|\mathcal{I}_{h}u-u\|_{H^i(\Omega)} \leq Ch^{k+1-i}|u|_{H^{k+1}(\Omega)}.

.. proof:proof::
   
   Identical to :numref:`Theorem {number}<Iherr>`.

Convergence of the finite element approximation to the Helmholtz problem
------------------------------------------------------------------------

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490668331"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=913ad682-d5b9-4849-8dc8-ac8f0120d5e8>`_

Now that we have the required interpolation operator results, we
can return to applying Céa's lemma to the convergence of the
finite element approximation to the Helmholtz problem.
   
.. proof:corollary::

   The degree `k` Lagrange finite element approximation `u_h` to the
   solution `u` of the variational Helmholtz problem satisfies

   .. math::

      \|u_h-u\|_{H^1(\Omega)} \leq Ch^k\|u\|_{H^{k+1}(\Omega)}.

.. proof:proof::
      
   We combine Céa's lemma with the previous estimate, since

   .. math::

      \min_{v\in V_h}
      \|u-v\|_{H^1(\Omega)} \leq \|u-\mathcal{I}_hu\|_{H^1(\Omega)}
      \leq Ch^k\|u\|_{H^{k+1}}(\Omega),

   having chosen `i=1`.

.. proof:exercise::

   Consider the variational problem of finding `u\in H^1([0,1])`
   such that

   .. math::

      \int_0^1 vu + v'u' \, d x = \int_0^1 vx \, d x + v(1) - v(0),
      \quad \forall v \in H^1([0,1]).

   After dividing the interval `[0,1]` into `N` equispaced cells and
   forming a `P1` `C^0` finite element space `V_N`, the error
   `\|u-u_h\|_{H^1}=0` for any `N>0`.

   Explain why this is expected.

.. proof:exercise::

   Let `\mathring{H}^1([0,1])` be the subspace of `H^1([0,1])` such
   that `u(0)=0`.  Consider the variational problem of finding `u \in
   \mathring{H}^1([0,1])` with
   
   .. math::

      \int_0^1 v'u' \, d x = \int_0^{1/2} v \, d x, \quad \forall v \in \mathring{H}([0,1]).

   The interval `[0,1]` is divided into `3N` equispaced cells (where `N`
   is a positive integer). After forming a `P1` `C^0` finite element
   space `V_N`, the error `\|u-u_h\|_{H^1}` is found not to converge to
   zero. Explain why this is expected.

.. proof:exercise::

   Let `\Omega` be a convex polygonal 2D domain. Consider the
    following two problems.
 
   #. Find `u \in H^2` such that

      .. math::

	 \|\nabla^2 u + f\|_{L^2(\Omega)} = 0, \quad
	 \|u\|_{L^2(\partial\Omega)}=0,
      
      which we write in a shorthand as

      .. math::
      
	 -\nabla^2 u = f, \quad u|_{\partial\Omega} = 0.

   #. Find `u \in \mathring{H}^1(\Omega)` such that

      .. math::
      
	 \int_\Omega \nabla u \cdot \nabla v \, d x = \int_\Omega f v \, d x,
	 \quad \forall v \in \mathring{H}^1(\Omega),
       
      where `\mathring{H}^1(\Omega)` is the subspace of `H^1(\Omega)`
      consisting of functions whose trace vanishes on the boundary.

   Under assumptions on `u` which you should state, show that a solution
   to problem (1.) is a solution to problem (2.).

   Let `h` be the maximum triangle diameter of a triangulation
   `T_h` of `\Omega`, with `V_h` the corresponding linear Lagrange
   finite element space. Construct a finite element approximation to
   Problem (2.) above.  Briefly give the main arguments as to why the
   `H^1(\Omega)` norm of the error converges to zero linearly in `h`
   as `h\to 0`, giving your assumptions.
   
Céa's lemma gives us error estimates in the norm of the space where
the variational problem is defined, where the continuity and coercivity
results hold. In the case of the Helmholtz problem, this is `H^1`.
We would also like estimates of the error in the `L^2` norm, and
it will turn out that these will have a more rapid convergence rate
as `h\to 0`.

.. Dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490668178"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=256886bb-d6bd-41fa-916a-ac8f0126b14b>`_

To do this we quote the following without proof.

.. proof:theorem:: Elliptic regularity

   Let `w` solve the equation

   .. math::
      
      w - \nabla^2 w = f, \quad \frac{\partial w}{\partial n}=0 \mbox{ on }\partial\Omega,

   on a convex (results also hold for other types of "nice" domains)
   domain `\Omega`, with `f\in L^2`. Then there exists constant `C>0`
   such that

   .. math::
      
      |w|_{H^2(\Omega)} \leq C\|f\|_{L^2(\Omega)}.

Similar results hold for general elliptic operators, such as Poisson's
equation with the types of boundary conditions discussed above.
Elliptic regularity is great to have, because it says that the
solution of the `H^1` variational problem is actually in `H^2`,
provided that `f\in L^2`.

We now use this to obtain the following result, using the
Aubin-Nitsche trick.

.. _thm-L2-estimates:

.. proof:theorem::
   
   The degree `k` Lagrange finite element approximation `u_h` to the
   solution `u` of the variational Helmholtz problem satisfies

   .. math::
      
      \|u_h-u\|_{L^2(\Omega)} \leq Ch^{k+1}\|u\|_{H^{k+1}(\Omega)}.

.. proof:proof::
   
   We use the Aubin-Nitsche duality argument. Let `w` be the
   solution of

   .. math::
   
      w - \nabla^2 w = u - u_h,

   with the same Neumann boundary conditions as for `u`.

   Since `u - u_h \in H^1(\Omega) \subset L^2(\Omega)`, we have
   `w \in H^2(\Omega)` by elliptic regularity.
      
   Then we have (by multiplying by a test function an integrating by
   parts),

   .. math::
      
      b(w,v) = (u-u_h,v)_{L^2(\Omega)}, \quad \forall v\in H^1(\Omega),

   and so

   .. math::
      
      \|u-u_h\|^2_{L^2(\Omega)} &= (u-u_h,u-u_h) = b(w,u-u_h), 
      = b(w-\mathcal{I}_hw,u-u_h) \mbox{ (orthogonality) },
      
      &\leq C\|u-u_h\|_{H^1(\Omega)}\|w-\mathcal{I}_h w\|_{H^1(\Omega)}, 

      &\leq Ch\|u-u_h\|_{H^1(\Omega)} |w|_{H^2(\Omega)} 

      &\leq C_1 h^{k+1} |u|_{H^{k+1}(\Omega)\|u-u_h\|_{L^2(\Omega)}}

   and dividing both sides by `\|u-u_h\|_{L^2(\Omega)}` gives the result.

Thus we gain one order of convergence rate with `h` by using
the `L^2` norm instead of the `H^1` norm.
      
Epilogue
--------
   
This completes our analysis of the convergence of the Galerkin finite
element approximation to the Helmholtz problem. Similar approaches can be
applied to analysis of other elliptic PDEs, using the following programme.

#. Find a variational formulation of the PDE with a bilinear form that
   is continuous and coercive (and hence well-posed by Lax-Milgram) on
   `H^k` for some `k`.
#. Find a finite element space `V_h \subset H^k`. For `H^1`, this requires
   a `C^0` finite element space, and for `H^2`, a `C^1` finite element
   space is required.
#. The Galerkin approximation to the variational formulation is obtained
   by restricting the solution and test functions to `V_h`.
   
#. Continuity and coercivity (and hence well-posedness) for the Galerkin
   approximation is assured since `V_h \subset H^k`. This means that
   the Galerkin approximation is solvable and stable.

#. The estimate of the error estimate in terms of `h` comes from
   Céa's lemma plus the error estimate for the nodal interpolation
   operator.

This course only describes the beginning of the subject of finite
element methods, for which research continues to grow in both theory
and application. There are many methods and approaches that go beyond
the basic Galerkin approach described above. These include

* Discontinuous Galerkin methods, which use discontinuous finite
  element spaces with jump conditions between cells to compensate for
  not having the required continuity. These problems do not fit into the
  standard Galerkin framework and new techniques have been developed to
  derive and analyse them.

* Mixed finite element methods, which consider systems of partial
  differential equations such as the Poisson equation in first-order
  form,

  .. math::

     u - \nabla p = 0, \quad \nabla\cdot u = f.

  The variational forms corresponding to these systems are not coercive,
  but they are well-posed anyway, and additional techniques have been
  developed.

* Non-conforming methods, which work even though `V_h \not\subset
  H^k`. For example, the Crouzeix-Raviart element uses linear functions
  that are only continuous at edge centres, so the functions are not
  in `C^0` and the functions do not have a weak derivative. However,
  using the finite element derivative in the weak form for `H^1` elliptic
  problems still gives a solvable system that converges at the optimal
  rate. Additional techniques have been
  developed to analyse this.

* Interior penalty methods, which work even though `V_h \not\subset
  H^k`. These methods are used to solve `H^k` elliptic problems using
  `H^l` finite element spaces with `l<k`, using jump conditions to
  obtain a stable discretisation. Additional techniques have been
  developed to analyse this.

* Stabilised and multiscale methods for finite element approximation
  of PDEs whose solutions have a wide range of scales, for example
  they might have boundary layers, turbulent structures or other
  phenomena. Resolving this features is often too expensive, so the
  goal is to find robust methods that behave well when the solution is
  not well resolved.  Additional techniques have been developed to
  analyse this.

* Hybridisable methods that involve flux functions that are supported
  only on cell facets.
  
* Currently there is a lot of activity around discontinuous
  Petrov-Galerkin methods, which select optimal test functions to
  maximise the stability of the discrete operator. This means that
  they can be applied to problems such as wave propagation which are
  otherwise very challenging to find stable methods for. Also, these
  methods come with a bespoke error estimator that can allow for
  adaptive meshing starting from very coarse meshes. Another new and
  active area is virtual element methods, where the basis functions
  are not explicitly defined everywhere (perhaps just on the boundary
  of cells). This facilitates the use of arbitrary polyhedra as cells,
  leading to very flexible mesh choices.

All of these methods are driven by the requirements of different physical
applications.

Other rich areas of finite element research include

* the development of bespoke, efficient iterative solver algorithms on
  parallel computers for finite element discretisations of PDEs. Here,
  knowledge of the analysis of the discretisation can lead to solvers
  that converge in a number of iterations that is independent of the
  mesh parameter `h`.

* adaptive mesh algorithms that use analytical techniques to estimate
  or bound the numerical error after the numerical solution has been
  computed, in order to guide iterative mesh refinement in particular
  areas of the domain.

.. end of week 10 material
