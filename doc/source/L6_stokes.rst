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

.. _eqn_general:

   .. math::

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
finite element discretisations of it, and we can't use C\`ea's Lemma
to estimate numerical errors in the finite element discretisation.
Instead we have to use a more general tool, the inf-sup theorem.

Solveability of mixed problems
------------------------------

.. proof:theorem:: Inf-sup theorem

   Let `c(U,W)` be a continuous bilinear form on a Hilbert space `X`,
   and `F(U)` be a continuous linear form on `X`. Then
   :numref:`Equation {number}<eqn_general>` has a unique solution
   provided that there exists `\gamma>0` such that
   
      .. math::

	 \inf_{U\in X}\sup_{W\in X} \frac{c(U,W)}{\|U\|_X\|W\|_X}
	 \geq \gamma > 0.

   Further, the solution satisfies

      .. math::

	 \|U\|_X \leq \frac{1}{\gamma}.

.. proof:proof::

   We don't give a proof here, but we can provide an idea of why it is
   true (which can be skipped upon first reading).  If we define the
   linear operator `\mathcal{C}:X\to X'` (with `X'` the dual space to
   `X`) by
   
      .. math::

	 (\mathcal{C}U)[W] = C(U,W), \quad \forall W\in X,

   then we can rewrite the problem as

      .. math::

	 \mathcal{C}U = F.

   The inf-sup condition can then be written as

      .. math::

	 \inf_{U \in X} \frac{\|\mathcal{C}U\|_{X'}}{\|U\|_X} \geq \gamma.

   Or, in other words, `\mathcal{C}` is bounding,

      .. math::

	 \|\mathcal{C}(U)\|_{X'} \geq \gamma\|U\|_X, \quad \forall U\in X.

   If `X` were a finite dimensional space, then this would show
   `\mathcal{C}` in injective since otherwise, there exists `U_1,U_2`
   such that

      .. math::

	 \mathcal{C}U_1 = \mathcal{C}U_2 = F
	 \implies \mathcal{C}(U_1-U_2)=0 \implies
	 0 = \|\mathcal{C}(U)\|_{X'} \geq \gamma \|U_1-U_2\|_X,

   i.e. `U_1-U_2=0`, a contradiction. For infinite dimensional Hilbert
   spaces of functions, the story is more complicated, and rests on the
   Closed Range Theorem which is not examinable in this course.
   For symmetric `c(U,W)`, the inf-sup condition is equivalent to the
   dual condition,

      .. math::

	 \inf_{U\in X}\sup_{W\in X} \frac{c(W,U)}{\|U\|_X\|W\|_X} \geq \gamma
	 > 0.

   Defining the transposed operator `C^*:X\to X'` by

      .. math::

	 C^*U[W] = C(W,U), \quad \forall W\in X,

   we similarly find that `C^*` is bounding, hence `C^*` is injective
   (subject to the Close Range Theorem again).
   If `C` is injective and `C^*` is injective,
   then `C` is invertible.

For symmetric, mixed problems in two variables, sufficient conditions
for existence are given by the following result of Franco Brezzi.

.. proof:theorem:: Brezzi's conditions

   Let `C(U,W)` be a continuous bilinear form defined on `X=V\times
   Q`, of the form

   .. math::

      C(U,W) = a(u,v) + b(v,p) + b(u,q), \quad
      U=(u,p), \, W=(v,q),

   and `F` be a continuous linear form on `X`. Define the kernel
   `Z` by

   .. math::

      Z = \left\{u\in V: b(u,q)=0 \forall q\in Q\right\}.

   Assume the following conditions:

   #. There exists `\beta>0` such that

         .. math::

	    \inf_{q\in Q}\sup_{v\in V} \frac{b(v,q)}{\|v\|_V\|q\|_Q}
	    \geq \beta,

   #. `a` is coercive on the kernel `Z`, i.e. there exists `\alpha>0`
      such that

         .. math::

	    a(v,v) \geq \alpha \|v\|^2_V, \quad \forall v\in Z.

   Then there exists a unique solution `(u,p)` to the variational
   problem, and

      .. math::

	 \|u\| \leq \frac{1}{\alpha}\|f\|_V,

	 \|p\|_Q \leq \frac{2 M}{\alpha\beta} \|f\|_V,

   where `M` is the continuity constant of `a`.

.. proof:proof::

   Again we don't give a proof but just provide some arguments as to why
   this might be true. To do this, we again pretend that the system is
   finite dimensional. Since it is then square, it is sufficient to
   show that the linear system has no kernel, i.e.

      .. math::
      
	 a(u,v) + b(v,p) + b(u,q) = 0, \, \forall (u,p)\in V\times Q
	 \implies (u,p)=0.

   First, taking `v=0`, we get

      .. math::

	 b(u,q) = 0\, \forall q \in Q, \implies u \in Z.

   If we take `v \in Z`, then we get the reduced problem

      .. math::

	 a(u,v) = 0, \, \forall v \in Z,

   for `u \in Z`, which has no kernel since `a` is a continuous and
   coercive bilinear form on the kernel `Z`. Hence, `u=0`. Then,
   we are reduced to

      .. math::

	 b(v,p) =0, \forall v\in V.

   Defining the operator `B:V\to Q'` by
	 
      .. math::

	 Bv[p] = b(v,p), \quad \forall p \in Q,

   we can write this as `Bp=0`. As discussed above (subject to
   considering the Closed Range Theorem), the inf-sup condition is
   equivalent to surjectivity of `B^*:Q\to V'`, defined by

      .. math::

	 Bp[v] = b(v,p), \quad \forall v \in V.

   Then we conclude that `B` is injective `Bp=0` implies that `p=0`.

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
spaces `V_h \sub V` and `Q_h \sub Q`. Then we apply the Galerkin
approximation, restricting the numerical solution `(u_h,p_h)` to
`V_h\times Q_h` as well as the test functions `(v_h,q_h)`. If the
bilinear form `c(X,Y)` were coercive, we could immediately get existence,
uniqueness and stability for the finite element discretisation. However,
we don't have it. This means that in particular we may have issues
with the uniqueness of `p_h`. To control these issues, we need to choose
`V_h` and `Q_h` such that we have the discrete inf-sup condition

   .. math::

      \inf_{q\in {Q_h}}\sup_{v\in {V_h}}
      \frac{b(v,q)}{\|v\|_{V_h}\|q\|_{Q_h}} \geq \hat{\beta},

with `\hat{\beta}>0`.
