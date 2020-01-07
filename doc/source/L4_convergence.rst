.. default-role:: math

Convergence of finite element approximations
============================================

In this section we develop tools to prove convergence of finite
element approximations to the exact solutions of PDEs.

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

.. proof:definition:: Compact support on `\Omega`

   A function `u` has compact support on `\Omega` if there exists `\epsilon>0`
   such that `u(x)=0` when `\min_{y\in\partial\Omega}|x-y|<\epsilon`.

.. proof:definition:: `C^\infty_0(\Omega)`
   
   We denote by `C^\infty_0(\Omega)` the subset of `C^\infty(\Omega)`
   corresponding to functions that have \emph{compact support} on
   `\Omega`.

Next we will define a space containing the generalised derivative.

.. proof:definition:: `L^1_{loc}`
		      
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

To discuss higher order derivatives, we introduce the multi-index.

.. proof:definition:: Multi-index.

   For `d`-dimensional space, a multi-index `\alpha=(\alpha_1,\ldots,\alpha_d)`
   assigns the number of partial derivatives in each Cartesian direction.
   We write `|\alpha|=\sum_{i=1}^d\alpha_i`.

This means we can write mixed partial derivatives, for example if
`\alpha=(1,2)` then

.. math::

   D^\alpha u = \frac{\partial^3 u}{\partial x\partial y^2}.

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
      
      = \sum_K\left(-\int_K \frac{\partial \phi}{\partial x_i} u \, d x + \int_{\partial K}
      \phi n_i u \, d S\right),

      = -\sum_K\int_K \frac{\partial\phi}{\partial x_i} u \, d x = -\int_\Omega
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

.. proof:proof::

   Exercise. [very similar to previous proof]

Due to these equivalences, we do not need to distinguish between
strong, weak and finite element first derivatives for `C^0` finite
element functions. All derivatives are assumed to be weak from now on.

Sobolev spaces
--------------

We are now in a position to define a space that contains all `C^0`
finite element spaces. This means that we can consider the limit
of finite element approximations as `h\to 0`.

.. proof:definition:: The Sobolev space `H^1`

   `H^1(\Omega)` is the function space defined by

   .. math::

      H^1(\Omega) = \left\{
      u\in L^1_{loc}: \|u\|_{H^1(\Omega)}<\infty\right\}.

To generalise this we first need to define some higher derivative norms.

.. proof:definition:: `H^k` seminorm and norm

   The `H^k` seminorm is defined as

   .. math::

      |u|_{H^k}^2 = \sum_{|\alpha|=k}\int_\Omega |D^\alpha u|^2 \, dx,

   where the sum is taken over all multi-indices of size `k` i.e. all the
   derivatives are of degree `k`.

   The `H^k` norm is defined as

   .. math::

      \|u\|_{H^k}^2 = \sum_{i=0}^k |u|_{H^i}^2.

   where we conventionally write `|u|_{H^0}=\|u\|_{L^2}`.

The Sobolev space `H^k` is then the space of all functions
with finite `H^k` norm.
      
.. proof:definition:: The Sobolev space `H^k`

   `H^k(\Omega)` is the function space defined by
   
   .. math::

      H^k(\Omega) = \left\{
      u\in L^1_{loc}: \|u\|_{H^k(\Omega)}<\infty\right\}
      
If we are to consider limits of finite element functions in these
Sobolev spaces, then it is important that they are closed, i.e.
limits remain in the spaces.

.. proof:lemma:: `H^k` spaces are Hilbert spaces

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
      
      \int_\Omega v^\alpha \phi \, d x  = \lim_{i\to \infty} \int_\Omega
      \phi D^\alpha u_i \, d x,
      
      = \lim_{i\to \infty} (-1)^{|\alpha|}\int_\Omega u_i D^\alpha\phi \, d x ,
 
      = (-1)^{|\alpha|} \int_\Omega v D^\alpha \phi \, d x,

   i.e. `v^\alpha` is the weak derivative of `u` as required.

We quote the following much deeper results without proof.

.. proof:theorem:: `H=W`

   Let `\Omega` be any open set. Then `H^k(\Omega)\cap C^\infty(\Omega)`
is dense in `H^k(\Omega)`.

The interpretation is that for any function `u\in H^k(\Omega)`,
we can find a sequence of `C^\infty` functions `u_i` converging
to `u`. This is very useful as we can compute many things using
`C^\infty` functions and take the limit.

.. proof:theorem:: Sobolev's inequality

   Let `\Omega` be an `n`-dimensional domain with Lipschitz boundary, let
   `k` be an integer with `k>n/2`. Then there exists a constant
   `C` such that

   .. math::

      \|u\|_{L^\infty(\Omega)} = \ess\sup_{x\in \Omega}|u(x)|
      \leq C\|u\|_{H^k(\Omega)}.

   Further, there is a `C^0` continuous function in the `L^\infty(\Omega)`
   equivalence class of `u`.

   The interpretation is that if `u\in H^k` then there is a continuous
   function `u_0` such that the set of points where `u\neq u_0` has
   zero area/volume.

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

We can now consider linear variational problems defined on `H^k`
spaces, by taking a bilinear form `b(u,v)` and linear form
`F(v)`, seeking `u\in H^k` (for chosen `H^k`) such that

.. math::

   b(u,v) = F(v), \quad \forall v \in H^k.

Since `H^k` is a Hilbert space, the Lax-Milgram theorem can be used to
analyse, the existence of a unique solution to an `H^k` linear
variational problem. For example, the Helmholtz problem solveability
is immediate.

.. proof:theorem:: Well-posedness for (modified) Helmholtz)

   The Helmholtz variational problem on `H^1` satisfies the conditions
of the Lax-Milgram theorem.

.. proof:proof::

   The proof for `C^0` finite element spaces extends immediately
   to `H^1`.

Functions in `H^k` make boundary conditions hard to interpret
since they are not guaranteed to have defined values on the boundary.
We make the following definition.

.. proof:definition:: Trace of `H^1` functions

   Let `u\in H^1(\Omega)` and choose `u_i\in C^\infty(\Omega)` such
   that `u_i\to u`. We define the \emph{trace} `u|_{\partial\Omega}`
   on `\partial\Omega` as the limit of the restriction of `u_i` to
   `\partial\Omega`. This definition is unique from the uniqueness of
   limits.

We can extend our trace inequality for finite element functions directly
to `H^1` functions.

.. proof:lemma:: Trace theorem for `H^1` functions
		 
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

