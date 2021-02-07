.. default-role:: math

Stokes equation (Mastery topic)
===============================

Strong form of the equations
----------------------------

In this section we consider finite element discretisations of the Stokes
equation of a viscous fluid, given by

.. math::

   -\mu\nabla\cdot\epsilon(u) + \nabla p = f, \quad \nabla\cdot u = 0,
    \quad \epsilon(u) = \frac{1}{2}\left( \nabla u + \nabla u^T\right),

where `u` is the (vector-valued) fluid velocity, `p` is the pressure,
`\mu` is the viscosity and `f` is a (vector-valued) external force
applied to the fluid. This model gives the motion of a fluid in the
high viscosity limit and has applications in industrial, geological
and biological flows. For less viscous fluids we use the Navier-Stokes
equation which consists of the Stokes equations plus additional
nonlinear terms. To understand discretisations of the Navier-Stokes
equations it is necessary to first understand discretisations of the
Stokes equation. There are several relevant boundary conditions for
the Stokes equation, but for now we shall consider the "no slip"
boundary condition `u=0` on the entire boundary `\partial\Omega`. Note
that `\nabla u` is a 2-tensor (i.e. a matrix-valued function), with

.. math::

   (\nabla u)_{ij} = \frac{\partial u_i}{\partial x_j},
   (\nabla u^T)_{ij} = (\nabla u)_{ij}.

Note that under the incompressibility constraint `\nabla\cdot u =0`, we
can write `\nabla\cdot\epsilon(u)=\nabla^2 u`. However, this leads to
various issues in the finite element discretisation, and makes it harder
to apply stress-free boundary conditions.

Under no slip boundary conditions, the pressure `p` only appears in
Stokes equation inside a gradient, hence we can only expect to solve
these equations for `p` up to an additive constant. To fix that constant,
with no slip boundary conditions we additionally require

.. math::

   \int_\Omega p d\,x = 0.

Variational form of the equations
---------------------------------

To proceed to the finite element discretisation, we need to find an
appropriate variational formulation of the Stokes equations. Defining
`V=(\mathring{H}^1(\Omega))^n` (i.e. vector valued functions in physical
dimension `n` with each Cartesian component in `\mathring{H}^1(\Omega)`,
which is the subspace of `H^1(\Omega)` consisting of functions that
vanish on the boundary, and `Q=\mathring{L}^2(\Omega)`, with

.. math::

   \mathring{L}^2(\Omega)=
   \left\{p\in L^2(\Omega): \int_\Omega p = 0\right\}.

.. proof:definition::

   The variational formulation of the Stokes equation seeks `(u,p)\in
   V\times Q` such that

   .. math::

      a(u,v) + b(v, p) & = \int_\Omega f\cdot v d\, x,
      
      b(u,q) & = 0, \quad \forall (v,q) \in V\times Q,

   where

   .. math::

      a(u,v) = \int_\Omega \epsilon(u):\epsilon(v)d\, x,

      b(v,q) = \int_\Omega q \nabla\cdot v d\, x.

.. proof:exercise::

   Show that if `(u,p)` solve the variational formulation of the
   Stokes equations, and further that `u\in H^2(\Omega)`, `p\in
   H^1(\Omega)`, then `(u,p)` solves the strong form of the Stokes
   equations.

We call this type of problem a "mixed problem" defined on a "mixed
function space" `V\times Q`, since we solve simultaneously for `u\in
V` and `p\in Q`. If we define `X=V\times Q`, and define `U=(u,p)\in X`
(as well as `W=(v,q)\in X`, then we can more abstractly write the
problem as finding `U\in X` such that

   .. math::
      :label: eqn_general

      c(U,W) = F(W),
      
where for the case of Stokes equation,

   .. math::

      c(U,W) = a(u,v) + b(v,p) + b(u,q), \quad F(W)=\int_{\Omega}f\cdot v d\, x.


There is a challenge with Stokes equation which is that it is not
coercive, i.e. there does not exist a constant `C>0` such that

   .. math::
   
      \|U\|^2_X \leq Cc(U,U), \quad \forall U\in X,

where here we use the product norm

   .. math::

      \|U\|^2_X = \|u\|_{H^1(\Omega)}^2 + \|p\|_{L^2(\Omega)}^2.

This means that we can't use the Lax Milgram Theorem to show existence
and uniqueness of solutions for the variational formulation or any
finite element discretisations of it, and we can't use Céa's Lemma
to estimate numerical errors in the finite element discretisation.
Instead we have to use a more general tool, the inf-sup theorem.

The inf-sup condition
---------------------

The critical tool in mixed problems is the inf-sup condition for a
bilinear form on `V\times Q`, which says that there exists `\beta>0`
such that

   .. math::

      \inf_{0\neq q\in Q}\sup_{0 \neq v\in V} \frac{b(v,q)}{\|v\|_V\|q\|_Q}
      \geq \beta.

For brevity, we will drop the `\neq 0` condition in subsequent formulae.
To understand this condition, we consider the map `B:V\to Q'`
given by

   .. math::

      Bv[p] = b(v,p), \, \forall p \in Q,

and the transpose operator `B^*:Q\to V'`, by

   .. math::

      B^*p[v] = b(v,p), \quad \forall v \in V.

Here, `Bv` is the map `B` applied to `v`, i.e. an element of the dual space
`Q'` which maps elements of `Q` to `\mathbb{R}`. `B^*p` is the image of
the map `B^*` applied to `p`, i.e. an element of the dual space `V'`
which maps elements of `V` to `\mathbb{R}`.

The norm of `B^*v` is

   .. math::

      \|B^*q\|_{V'} = \sup_{v\in V}\frac{b(v,q)}{\|v\|_V}.

Which allows us to rewrite the inf-sup condition as

   .. math::

      \inf_{q\in Q} \frac{\|B^*q\|_{V'}}{\|q\|_Q} \geq \beta,

which is also equivalent to

   .. math::

      \|B^*q\|_{V'} \geq \beta\|q\|_Q, \, \forall q\in Q.

This tells us that the map `B^*` is injective, since if there
exist `q_1,q_2` such that `B^*q_1=B^*q_2`, then `B^*(q_1-q_2)=0
\implies 0 = \|B^*(q_1-q_2) \geq \beta\|q_1-q_2\|_Q`, i.e.
`q_1=q_2`.

In finite dimensions (such as for our finite element spaces),
injective `B^*` is equivalent to surjective `B` (via the rank-nullity
theorem). In infinite dimensions, such as the case
`\mathring{H}^1\times \mathring{L}^2` that we are considering for
Stokes equation, the situation is more complicated and is governed by
the Closed Range Theorem (which we allude to here but do not prove),
which states that for Hilbert spaces and continuous bilinear forms
`b(v,q)`, injective `B^*` is indeed equivalent to surjective `B`.

The Closed Range Theorem (and the rank-nullity theorem, its finite
dimensional version) further characterises these maps using perpendicular
spaces.

.. proof:definition:: Perpendicular space

   For a subspace `Z\subset Q` of a Hilbert space `Q`, the
   perpendicular space `Z^\perp` of `Z` in `Q` is

      .. math::

	 Z^{\perp} = \left\{ q\in Q: \langle q,p \rangle_Q = 0, \,
	 \forall p \in Q\right\}.

In finite dimensions, we have that `B^*` defines a one-to-one mapping
from `(\mathrm{Ker}B^*)^\perp\subset Q` (the perpendicular space to
the kernel `\mathrm{Ker}B^*` of `B^*`) to `\mathrm{Im}(B^*)` (the
image space of `B^*`). This is also true in infinite dimensions under
the conditions of the Closed Range Theorem.

This means that for any `F\in \mathrm{Im}(B^*)`, we can find `q
\in (\mathrm{Ker}B^*)^\perp` such that `B^*q=F`. Further, we have

   .. math::

      \|F\|_{V'} \geq \beta\|q\|_Q,

via the inf-sup condition.

Finally, it is useful to characterise `\mathrm{Im}(B^*)`. In
`\mathbb{R}^n`, we are used to the rank-nullity theorem telling us
that `\mathrm{Im}(B^*)=(\mathrm{Ker} B^*)^\perp`. However, here `B^*` maps
to `V'`, not `V`, so this does not make sense. When considering
maps between dual spaces, we have to generalise this idea to polar
spaces.

.. proof:definition:: Polar space

   For `Z` a subspace of a Hilbert space `Q`, the polar space `Z^0`
   is the subspace of `Q'` of continuous linear functionals that
   vanish on `Z` i.e.

      .. math::

	 Z^0 = \left\{ F\in Q': F[q]=0\, \forall q\in Z\right\}.

Then the dual space version of the rank-nullity theorem (and the
Closed Range Theorem for infinity dimensional Hilbert spaces) tells
us that

   .. math::

      \mathrm{Im}(B^*) = (\mathrm{Ker} B^*)^0.

Equipped with this tool, we can look at solveability of mixed problems.
      
Solveability of mixed problems
------------------------------

For symmetric, mixed problems in two variables, sufficient conditions
for existence are given by the following result of Franco Brezzi.

.. proof:theorem:: Brezzi's conditions

   Let `a(u,v)` be a continuous bilinear form defined on `V\times V`,
   and `b(v,q)` be a continuous bilinear form defined on `V\times Q`.
   Consider the variational problem for `(u,p)\in V\times Q`,

   .. math::

      a(u,v) + b(v,p) + b(u,q) = F[v], \, \forall v \in V,

      b(u,q) = G[q], \, \forall q\in Q,

   for `F` and `G` continuous linear forms on `V` and `Q` respectively.
   
   Define the kernel
   `Z` by

   .. math::

      Z = \left\{u\in V: b(u,q)=0 \forall q\in Q\right\}.

   Assume the following conditions:

   #. `a(u,v)` is coercive on the kernel `Z` with coercivity constant
      `\alpha`.
   
   #. There exists `\beta>0` such that the inf-sup condition for
      `b(v,q)` holds.

   Then there exists a unique solution `(u,p)` to the variational
   problem and

      .. math::

	 \|u\| \leq \frac{1}{\alpha}\|f\|_V,

	 \|p\|_Q \leq \frac{2 M}{\alpha\beta} \|f\|_V,

   where `M` is the continuity constant of `a`.

.. proof:proof::

   To show existence, we first note that the inf-sup condition implies
   that `B` is surjective, so we can always find `u_g\in V` such that
   `Bu_g = g`. Now we write `u=u_g+u_0`, and we have the following
   mixed problem,

      .. math::

	 a(u_0,v) + b(v,p) = F[v] - a(u_g, v), \, \forall v \in V,

	 b(u_0,q) = 0.

   Thus, `Bu_0=0`, i.e. `u_0\in Z`. Choosing `v\in Z\subset V`, we get

      .. math::

	 a(u_0,v) = F'[v] = F[v] - a(u_g,v), \, \forall v\in Z,

   for `u_0 \in Z`. Since `a(u,v)` is coercive on `Z`, and `F'` is
   continuous (from continuity of `F` and `a(u,v)`), Lax-Milgram tells
   us that `u_0\in Z` exists and is unique. We now notice that

      .. math::

	 L[v] = F[v] - a(u_g+u_0,v) = 0 \forall v\in Z,

   so `L[v]\in Z^0 = (\mathrm{Ker} B)^0=\mathrm{Im} B^*`. This means that there
   exists `p\in Q` such that `B^*p = L`. Hence, we have found `(u,p)`
   that solve our mixed variational problem.

   To show uniqueness, we need to show that if there exists `(u_1,p_1)`
   and `(u_2,p_2)` that both solve our mixed variational problem,
   then `(u,p)=(u_1-u_2,p_1-p_2)=0`. To that end, we take the difference
   of the equations for the two solutions, and get

      .. math::

	 a(u,v) + b(v,p) = 0, \, \forall v\in V,

	 b(u,q) = 0, \forall q\in Q.

   It is our goal to show that `(u,p)=0`. We have again that `u\in Z`,
   and taking `v=u` gives

      .. math::

	 0 = a(u,u) \geq \alpha\|u\|_V^2 \implies u=0.

   Substituting this into the problem for `(u,p)` gives

      .. math::

	 b(v,p) = 0, \, \forall v\in V.

   Since `b` is injective, this means that `p=0` as required.

   Having shown existence and uniqueness of `(u,p)`, we want to 
   develop the stability bounds. We now assume that `(u,p)` solves
   the variational problem. We first use the surjectivity of
   `B` to find `u_g` such that `Bu_g=G`. This means that

   .. math::

      b(q,u_g) = G[q], \forall q \in Q,

   Then, for all `q\in Q`,

   .. math::

      \|G\|_{Q'} = \sup_{q\in Q}\frac{b(q,u_g)}{\|q\|_Q}

      = \sup_{q\in Q}\frac{b(q,u_g)}{\|q\|_Q\|u_g\|_V}\|u_g\|_V
      
      \geq \beta \|u_g\|,

   by the inf-sup condition. Now we define `u_Z = u - u_g`, so that
   `Bu_Z = Bu - Bu_g = G - G = 0`. Therefore `u_Z\in Z`.

   Then taking `v \in Z`, we have

      .. math::

	 a(u_Z,v) = F[v], \quad \forall v\in Z.

   From the Lax-Milgram theorem we have `\|u_Z\|_V \leq
   \|F\|_{Q'}/\alpha`.  Returning to general `v\in Q`, we rearrange
   the variational problem to get

      .. math::

	 b(p,v) = F'[v] = F[v] - a(u_Z + u_g, v), \quad \forall v \in V.

   As discussed previously, `F'\in Z^0`, hence this equation is solveable
   for `p_f` and we have

      .. math::

	 \|F'\|_{V'} \geq \beta\|p_f\|_Q.

   Rearranging and using the triangle inequality and the estimate for
   `\|u_Z\|_V`, we get

   .. math::

      \|p_f\|_Q \leq \frac{1}{\beta}\left(\|F'\|_{V'}\right)

      \leq \frac{1}{\beta}\left(\|F\|_{V'} + \frac{M}{\alpha}\|F\|_{V'}\right)

      \leq \frac{2M}{\alpha\beta}\|F\|_{V'},

   assuming that `M/\alpha > 1` (otherwise pick a bigger `M`).

Solveability of Stokes equation
--------------------------------------------------

Now we return to our variational formulation of Stokes equation and
consider the Brezzi conditions for it. In the case of Stokes, the
operator `B^*` is the divergence operator. It can be shown (beyond
the scope of this course) that `B^*` maps from the whole of `V` onto
`Q` in this case, so the inf-sup condition holds. It can also be shown
that `a` is coercive on the whole of `V`, i.e. there exists `\alpha>0`
such that

   .. math::

      a(v,v) \geq \alpha \|v\|^2_V.

This result is called the Korn identity (also beyond our scope). Then
of course, `a` is in particular coercive on the divergence-free
subspace `Z`. Then we immediately get solveability of the variational
Stokes problem.

Discretisation of Stokes equations
----------------------------------

To discretise the Stokes equations, we need to choose finite element
spaces `V_h \subset V` and `Q_h \subset Q`. Then we apply the Galerkin
approximation, restricting the numerical solution `(u_h,p_h)` to
`V_h\times Q_h` as well as the test functions `(v_h,q_h)`. If the
bilinear form `c(X,Y)` were coercive, we could immediately get existence,
uniqueness and stability for the finite element discretisation. However,
we don't have it. This means that in particular we may have issues
with the uniqueness of `p_h`. To control these issues, we need to choose
`V_h` and `Q_h` such that we have the discrete inf-sup condition

   .. math::

      \inf_{q\in {Q_h}}\sup_{v\in {V_h}}
      \frac{b(v,q)}{\|v\|_{V}\|q\|_{Q}} \geq \hat{\beta},

with `\hat{\beta}>0`.
