.. default-role:: math

.. _stokes:

Stokes equation
===============

.. note::

   This section is the mastery topic for this module. It consists of
   some extra material that is not covered in lectures which will be
   covered in the mastery question on the exam.

   This section is not a part of the third year version of this module.

Strong form of the equations
----------------------------

In this section we consider finite element discretisations of the Stokes
equation of a viscous fluid, given by

.. math::
   :label:

   -2\mu\nabla\cdot\epsilon(u) + \nabla p = f, \quad \nabla\cdot u = 0,
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
   :label:

   (\nabla u)_{ij} = \frac{\partial u_i}{\partial x_j},
   (\nabla u^T)_{ij} = (\nabla u)_{ji}.

Note that under the incompressibility constraint `\nabla\cdot u =0`, we
can write `\nabla\cdot\epsilon(u)=\nabla^2 u`. However, this leads to
various issues in the finite element discretisation, and makes it harder
to apply stress-free boundary conditions.

Under no slip boundary conditions, the pressure `p` only appears in
Stokes equation inside a gradient, hence we can only expect to solve
these equations for `p` up to an additive constant. To fix that constant,
with no slip boundary conditions we additionally require

.. math::
   :label:

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
   :label:

   \mathring{L}^2(\Omega)=
   \left\{p\in L^2(\Omega): \int_\Omega p = 0\right\}.

.. _weak_stokes:

.. proof:definition::

   The variational formulation of the Stokes equation seeks `(u,p)\in
   V\times Q` such that

   .. math::
      :label:

      a(u,v) + b(v, p) & = \int_\Omega f\cdot v d\, x,
      
      b(u,q) & = 0, \quad \forall (v,q) \in V\times Q,

   where

   .. math::
      :label:

      a(u,v) = 2\mu\int_\Omega \epsilon(u):\epsilon(v)d\, x,

      b(v,q) = -\int_\Omega q \nabla\cdot v d\, x.

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
      :label:

      c(U,W) = a(u,v) + b(v,p) + b(u,q), \quad F(W)=\int_{\Omega}f\cdot v d\, x.


There is a challenge with Stokes equation which is that it is not
coercive, i.e. there does not exist a constant `C>0` such that

   .. math::
      :label:
   
      \|U\|^2_X \leq Cc(U,U), \quad \forall U\in X,

where here we use the product norm

   .. math::
      :label:

      \|U\|^2_X = \|u\|_{H^1(\Omega)}^2 + \|p\|_{L^2(\Omega)}^2.

This means that we can't use the Lax Milgram Theorem to show existence
and uniqueness of solutions for the variational formulation or any
finite element discretisations of it, and we can't use Céa's Lemma
to estimate numerical errors in the finite element discretisation.
Instead we have to use a more general tool, the inf-sup theorem.

.. proof:exercise::

   Show that the form `c(\cdot,\cdot)` is not coercive by considering
   the case `v=0`.

The inf-sup condition
---------------------

.. tip::

   The key to understanding this section and the following one is to
   have a good recollection of the definition of dual spaces and dual
   space norms given in the earlier section on
   :ref:`sec-linearforms`. It is a good idea to go back and review
   that section before you carry on.

The critical tool in mixed problems is the inf-sup condition for a
bilinear form on `V\times Q`, which says that there exists `\beta>0`
such that

   .. math::
      :label:

      \inf_{0\neq q\in Q}\sup_{0 \neq v\in V} \frac{b(v,q)}{\|v\|_V\|q\|_Q}
      \geq \beta.

For brevity, we will drop the `\neq 0` condition in subsequent formulae.
To understand this condition, we consider the map `B:V\to Q'`
given by

   .. math::
      :label:

      Bv[p] = b(v,p), \, \forall p \in Q,

and the transpose operator `B^*:Q\to V'`, by

   .. math::
      :label:

      B^*p[v] = b(v,p), \quad \forall v \in V.

Here, `Bv` is the map `B` applied to `v`: `Bv` is an element of the
dual space `Q'` which itself maps elements of `Q` to
`\mathbb{R}`. `B^*p` is the image of the map `B^*` applied to `p`:
`B^*p` is an element of the dual space `V'` which itself maps elements
of `V` to `\mathbb{R}`.

The norm of `B^*q` is

   .. math::
      :label:

      \|B^*q\|_{V'} = \sup_{v\in V}\frac{b(v,q)}{\|v\|_V}.

This allows us to rewrite the inf-sup condition as

   .. math::
      :label:

      \inf_{q\in Q} \frac{\|B^*q\|_{V'}}{\|q\|_Q} \geq \beta,

which is also equivalent to

   .. math::
      :label:

      \|B^*q\|_{V'} \geq \beta\|q\|_Q, \, \forall q\in Q.

This tells us that the map `B^*` is injective, since if there
exist `q_1,q_2` such that `B^*q_1=B^*q_2`, then `B^*(q_1-q_2)=0
\implies 0 = \|B^*(q_1-q_2)\|_V \geq \beta\|q_1-q_2\|_Q`, i.e.
`q_1=q_2`.

In finite dimensions (such as for our finite element spaces),
injective `B^*` is equivalent to surjective `B` (via the rank-nullity
theorem). In infinite dimensions, such as the case
`\mathring{H}^1\times \mathring{L}^2` that we are considering for
Stokes equation, the situation is more complicated and is governed by
the Closed Range Theorem (which we allude to here but do not state or prove),
which tells us that for Hilbert spaces and continuous bilinear forms
`b(v,q)`, injective `B^*` is indeed equivalent to surjective `B`.

The Closed Range Theorem (and the rank-nullity theorem, its finite
dimensional version) further characterises these maps using perpendicular
spaces.

.. proof:definition:: Perpendicular space

   For a subspace `Z\subset Q` of a Hilbert space `Q`, the
   perpendicular space `Z^\perp` of `Z` in `Q` is

      .. math::
	 :label:

	 Z^{\perp} = \left\{ q\in Q: \langle q,p \rangle_Q = 0, \,
	 \forall p \in Z\right\}.

In finite dimensions, we have that `B^*` defines a one-to-one mapping
from `(\mathrm{Ker}B^*)^\perp\subset Q` (the perpendicular space to
the kernel `\mathrm{Ker}B^*` of `B^*`) to `\mathrm{Im}(B^*)` (the
image space of `B^*`). This is also true in infinite dimensions under
the conditions of the Closed Range Theorem.

This means that for any `F\in \mathrm{Im}(B^*)`, we can find `q
\in (\mathrm{Ker}B^*)^\perp` such that `B^*q=F`. Further, we have

   .. math::
      :label:

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
	 :label:

	 Z^0 = \left\{ F\in Q': F[q]=0\, \forall q\in Z\right\}.

Then the dual space version of the rank-nullity theorem (and the
Closed Range Theorem for infinity dimensional Hilbert spaces) tells
us that

   .. math::
      :label:

      \mathrm{Im}(B^*) = (\mathrm{Ker} B)^0.

Equipped with this tool, we can look at solveability of mixed problems.
      
Solveability of mixed problems
------------------------------

For symmetric, mixed problems in two variables, sufficient conditions
for existence are given by the following result of Franco Brezzi.

.. _brezzi:

.. proof:theorem:: Brezzi's conditions

   Let `a(u,v)` be a continuous bilinear form defined on `V\times V`,
   and `b(v,q)` be a continuous bilinear form defined on `V\times Q`.
   Consider the variational problem for `(u,p)\in V\times Q`,

   .. math::
      :label:

      a(u,v) + b(v,p) = F[v], \, \forall v \in V,

      b(u,q) = G[q], \, \forall q\in Q,

   for `F` and `G` continuous linear forms on `V` and `Q` respectively.
   
   Define the kernel
   `Z` by

   .. math::
      :label:

      Z = \left\{u\in V: b(u,q)=0 \forall q\in Q\right\}.

   Assume the following conditions:

   #. `a(u,v)` is coercive on the kernel `Z` with coercivity constant
      `\alpha`.
   
   #. There exists `\beta>0` such that the inf-sup condition for
      `b(v,q)` holds.

   Then there exists a unique solution `(u,p)` to the variational
   problem and we have the stability bound

      .. math::
	 :label:

	 \|u\|_V  \leq \frac{1}{\alpha}\|F\|_{V'}
	 + \frac{2M}{\alpha\beta}\|G\|_{Q'},

	 \|p\|_Q \leq \frac{2M}{\alpha\beta}\|F\|_{V'} +
	 \frac{2M^2}{\alpha\beta^2} \|G\|_{Q'},

   where `M` is the continuity constant of `a`.

.. proof:proof::

   To show existence, we first note that the inf-sup condition implies
   that `B` is surjective, so we can always find `u_g\in V` such that
   `Bu_g = g`. Now we write `u=u_g+u_Z`, and we have the following
   mixed problem,

      .. math::
	 :label:

	 a(u_Z,v) + b(v,p) = F[v] - a(u_g, v), \, \forall v \in V,

	 b(u_Z,q) = 0.

   Thus, `Bu_Z=0`, i.e. `u_Z\in Z`. Choosing `v\in Z\subset V`, we get

      .. math::
	 :label: uZ
	    
	 a(u_Z,v) = F'[v] = F[v] - a(u_g,v), \, \forall v\in Z,

   for `u_Z \in Z`. Since `a(u,v)` is coercive on `Z`, and `F'` is
   continuous (from continuity of `F` and `a(u,v)`), Lax Milgram tells
   us that `u_Z\in Z` exists and is unique. We now notice that

      .. math::
	 :label:
	 
	 L[v] = F[v] - a(u_g+u_Z,v) = 0 \forall v\in Z,

   so `L[v]\in Z^0 = (\mathrm{Ker} B)^0=\mathrm{Im} B^*`. This means that there
   exists `p\in Q` such that `B^*p = L`. Hence, we have found `(u,p)`
   that solve our mixed variational problem.

   To show uniqueness, we need to show that if there exists `(u_1,p_1)`
   and `(u_2,p_2)` that both solve our mixed variational problem,
   then `(u,p)=(u_1-u_2,p_1-p_2)=0`. To that end, we take the difference
   of the equations for the two solutions, and get

      .. math::
	 :label:

	 a(u,v) + b(v,p) = 0, \, \forall v\in V,

	 b(u,q) = 0, \forall q\in Q.

   It is our goal to show that `(u,p)=0`. We have again that `u\in Z`,
   and taking `v=u` gives

      .. math::
	 :label:

	 0 = a(u,u) \geq \alpha\|u\|_V^2 \implies u=0.

   Substituting this into the problem for `(u,p)` gives

      .. math::
	 :label:

	 b(v,p) = 0, \, \forall v\in V.

   Since `b` is injective, this means that `p=0` as required.

   Having shown existence and uniqueness of `(u,p)`, we want to 
   develop the stability bounds. We now assume that `(u,p)` solves
   the variational problem. We first use the surjectivity of
   `B` to find `u_g` such that `Bu_g=G`. This means that

   .. math::
      :label:

      b(q,u_g) = G[q], \forall q \in Q,

   Then, for all `q\in Q`,

   .. math::
      :label:

      \|G\|_{Q'} = \sup_{q\in Q}\frac{b(q,u_g)}{\|q\|_Q}

      = \sup_{q\in Q}\frac{b(q,u_g)}{\|q\|_Q\|u_g\|_V}\|u_g\|_V
      
      \geq \beta \|u_g\|,

   by the inf-sup condition.

   From the Lax Milgram theorem applied to :eq:`uZ`, we get

      .. math::
	 :label:

	 \|u_Z\|_V \leq \frac{1}{\alpha}\left(\|F\|_{V'} +
	 \sup_{v\in V}\frac{a(u_g,\cdot)}{\|v\|_V}\right)

	 \leq \frac{1}{\alpha} \|F\|_{V'} + \frac{M}{\alpha}\|u_g\|_{V},

	 \leq \frac{1}{\alpha}\|F\|_{V'} + \frac{M}{\alpha\beta}\|G\|_{Q'},

   where `M` is the continuity constant of `a(\cdot,\cdot)`.

   Then we have

      .. math::
	 :label:

	 \|u\|_V = \|u_Z + u_g \|_V \leq \|u_Z\|_V + \|u_g\|_V,

	 \leq \frac{1}{\alpha}\|F\|_{V'} + \frac{M}{\alpha\beta}\|G\|_{Q'}
	 + \frac{1}{\beta}\|G\|_{Q'},

	 \leq \frac{1}{\alpha}\|F\|_{V'} + \frac{2M}{\alpha\beta}\|G\|_{Q'},

   making use of `M>\alpha` (we have `\alpha \|u\|^2 \leq a(u,u) \leq M\|u\|^2` for any `u \in V`).  This gives the estimate for
   `\|u\|_V`.
   
   To estimate `\|p\|_Q`, we rearrange the variational problem to get

      .. math::
	 :label:

	 b(p,v) = F'[v] = F[v] - a(u, v), \quad \forall v \in V.

   As discussed previously, `F'\in Z^0`, hence this equation is solveable
   for `p` and we have

      .. math::
	 :label:

	 \|F'\|_{V'} \geq \beta\|p\|_Q,

   Hence, 

     .. math::
	:label:

	\|p\|_Q\leq \frac{1}{\beta}\|F\|_{V'} + \frac{M}{\beta}\|u\|_V,

	\leq \frac{1}{\beta}\|F\|_{V'} + \frac{M}{\beta}
	\left(\frac{1}{\alpha}\|F\|_{V'} + \frac{2M}{\alpha\beta}\|G\|_{V'}
	\right),

	\leq \frac{2M}{\alpha\beta}\|F\|_{V'} + \frac{2M^2}{\alpha\beta^2}
	\|G\|_{Q'},

   as required, having used `M>\alpha` again.

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
      :label:

      a(v,v) \geq \alpha \|v\|^2_V.

This result is called Korn's identity (also beyond our scope). Then
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
      :label:

      \inf_{q\in {Q_h}}\sup_{v\in {V_h}}
      \frac{b(v,q)}{\|v\|_{V}\|q\|_{Q}} \geq \beta_h,

with `\beta_h>0`. Note that `\beta_h\neq \beta` in general,
but it does not matter as long as `\beta_h` is independent
of the mesh size parameter `h`.

If the discrete inf-sup condition is satisfied then we just need to
also check whether `a(\cdot,\cdot)` is coercive on the discrete kernel
`Z_h` defined by

   .. math::
      :label:

      Z_h = \left\{u\in V_h:b(u,q)=0 \,\forall q\in Q_h\right\}.

Note that `Z_h\not\subset Z` in general (unless `V_h` and `Q_h` have
been specially chosen to allow that). However, the details do not
matter since we already noted that `a(\cdot,\cdot)` is coercive on all
of `V`, so must be coercive on `Z_h\subset V` in particular. Hence, as
long as the discrete inf-sup condition is satisfied, we immediately
get existence and uniqueness of solutions of the finite element
approximation of Stokes equation from Theorem :ref:`brezzi`, along
with the stability bounds on `(u_h,p_h)`, but with `\beta` replaced
by `\beta_h`.

We are now in a position to estimate errors in the finite element
approximation in a manner very similar to Céa's Lemma.

.. proof:theorem::

   Let `V_h\subset V` and `Q_h\subset Q` be a pair of finite element
   spaces satisfying the discrete inf-sup condition for some
   `\beta_h>0`. Then,

      .. math::
	 :label:

	 \|u_h - u\|_V \leq  \frac{4MM_b}{\alpha\beta_h}E_u + \frac{M_b}{\alpha}E_p,

	 \|p_h - p\|_V \leq \frac{3M^2M_b}{\alpha\beta_h^2}E_u
	 + \frac{3MM_b}{\alpha\beta_h}E_p.

   where `M_b` is the continuity constant of `b(\cdot,\cdot)`, and
   where we have the best approximation errors of `u` and `p` in `V_h`
   and `Q_h` respectively,

      .. math::
	 :label:

	 E_u = \inf_{u_I\in V_h}\|u-u_I\|_V,

	 E_p = \inf_{p_I\in Q_h}\|p-p_I\|_Q.

.. proof:proof::

   Since `V_h\subset V` and `Q_h\subset Q`, we can choose `(v,q)\in
   V_h\times Q_h` in both the original variational problem and the
   finite element variational problem and subtract one from the other,
   to obtain

      .. math::
	 :label:

	 a(u_h-u,v) + b(v,p_h-p) = 0, \quad \forall v\in V_h,

	 b(u_h-u,q) = 0, \quad \forall q\in Q_h.

   This is the mixed finite element version of Galerkin orthogonality
   that we saw earlier in the course. Replacing `u=u-u_I+u_I` and
   `p=p-p_I+p_I` for `(u_I,p_I)\in V_h\times Q_h` and rearranging,
   we get
   
      .. math::
	 :label:

	 a(u_h-u_I,v) + b(v,p_h-p_I) = F_{u_I,p_I}[v] := a(u-u_I,v) + b(v,p-p_I), \quad \forall v\in V_h,

	 b(u_h-u_I,q) = G_{u_I}[q] := b(u-u_I,q), \quad \forall q\in Q_h.

   Hence, from the stability bound,

      .. math::
	 :label:

	 \|u_h-u_I\|_V  \leq \frac{1}{\alpha}\|F_{u_I,p_I}\|_{V'}
	 + \frac{2M}{\alpha\beta_h}\|G_{u_I}\|_{Q'},

	 \|p_h-p_I\|_Q \leq \frac{2M}{\alpha\beta_h}\|F_{u_I,p_I}\|_{V'} +
	 \frac{2M^2}{\alpha\beta_h^2} \|G_{u_I}\|_{Q'}.

   Using continuity of `a(\cdot,\cdot)` and `b(\cdot,\cdot)`, we have

      .. math::
	 :label:

	 \|F_{u_I,p_I}\|_{V'} \leq \sup_{v\in V}\frac{a(u-u_I,v)}{\|v\|_{V}}
	 + \sup_{v\in V}\frac{b(v,p-p_I)}{\|v\|_V}
	 \leq M\|u-u_I\|_V + M_b\|p-p_I\|_Q,

	 \|G_{u_I}\|_{Q'} = \sup_{p\in Q}\frac{b(u-u_I,p)}{\|p\|_Q}
	 \leq M_b\|u-u_I\|_V.

   Substitution then gives 

      .. math::
	 :label:

	 \|u_h-u_I\|_V  \leq \frac{1}{\alpha}\left(M\|u-u_I\|_V +
	 M_b\|p-p_I\|_Q\right)
	 + \frac{2M}{\alpha\beta_h}M_b\|u-u_I\|_V.
	 
   We have

      .. math::
	 \beta_h \leq \inf_{q\in Q_h}\sup_{v\in V_h}\frac{b(v,q)}{\|q\|_Q\|v\|_V} \leq M_b,

   and hence,

      .. math::
	 :label:

	 \|u_h-u_I\|_V\leq \frac{3MM_b}{\alpha\beta_h}\|u-u_I\|_V + \frac{M_b}{\alpha}
	 \|p-p_I\|_Q,

   and

      .. math::
	 :label:
	   
	 \|p_h-p_I\|_Q \leq \frac{2M}{\alpha\beta_h}
	 \left(M\|u-u_I\|_V +
	 M_b\|p-p_I\|_Q\right)
	 +
	 \frac{2M^2}{\alpha\beta_h^2}M_b\|u-u_I\|_V

	 \leq \frac{3M^2M_b}{\alpha\beta_h^2}\|u-u_I\|_V
	 + \frac{2MM_b}{\alpha\beta_h}\|p-p_I\|_Q.
	 
   We then use the triangle inequality to write

      .. math::
	 :label:

	 \|u-u_h\|_V \leq \|u-u_I\|_V + \|u_h-u_I\|_V,

	 \leq  \frac{4MM_b}{\alpha\beta_h}\|u-u_I\|_V + \frac{M_b}{\alpha}
	 \|p-p_I\|_Q,
   
      .. math::
	 :label:

	 \|p-p_h\|_Q \leq \|p-p_I\|_Q + \|p_h-p_I\|_Q,

	 \leq \frac{3M^2M_b}{\alpha\beta_h^2}\|u-u_I\|_V
	 + \frac{3MM_b}{\alpha\beta_h}\|p-p_I\|_Q.

   Finally, taking the infimum over the all `u_I\in V` and all `p_I\in Q`
   gives the result.

This theorem tells us that if we can approximate the solution `(u,p)`
well in `V_h\times Q_h`, then the finite element approximation error
will also be small.

For scalar `H^1` elliptic problems like the Poisson equation that we
studied earlier in the course, finding a suitable `V_h` is easy, as
any continuous finite element space will do. In contrast, for Stokes
equation it is not straightforward to find pairs of finite element
spaces `V_h\times Q_h` that satisfy this discrete inf-sup
condition. For example, the simplest idea of trying `Q_h` to be P1
(linear Lagrange elements on triangles) and `V_h` to be `(P1)^d`
(linear Lagrange elements for each Cartesian component of velocity
from 1 up to the dimension `d`) does not work in general. We call
this combination P1-P1.

.. proof:exercise::

   Consider a square domain divided into 4 smaller and equal squares,
   and then subdivide the squares into right-angled triangles so all
   the hypotenuses meet in the middle (like the UK flag). Show that
   there exists `p\in Q_h` such that `b(v,p)=0` for all `v\in V_h`.
   (Don't forget to include the boundary conditions for `V_h` and the
   mean zero condition for `p`.) Conclude that the inf-sup condition
   does not hold.

We now discuss some examples of finite element pairs that do satisfy
the inf-sup condition with `\beta_h>0` independent of `h`.

The MINI element
----------------

In general, the choice P1-P1 produces `\beta_h\to 0` as `h\to 0`: the
discretisation is not stable. This means that the image of the
divergence applied to `V_h` does not converge to `Q` as `h\to 0`. The
way to fix this is to enrich the `(P1)^d` space for velocity, so that
the image is larger. For the MINI element, this is done by considering
the following finite element, P1+B3.

.. proof:definition:: P1+B3

   The P1+B3 element `(K,P,\mathcal{N})` is given by:

   #. `K` is a triangle.

   #. The shape functions are linear combinations of linear functions
      and cubic "bubble" functions that vanish on the boundary of `K`.

   #. The nodal variables are point evaluations at the vertices plus
      point evaluation at the triangle centre.

We then take `V_h` as the `(P1+B3)^d` continuous finite element space (i.e.
each Cartesian component of the functions in `V_h` is from `P1+B3`.
We choose `P1` for `Q_h`.

To prove that the MINI element satisfies the inf-sup condition, we use
the following result.

.. proof:lemma::  Fortin's trick

   Assume that the inf-sup condition holds for $b(v,q)$ over $V\times Q$
   with inf-sup constant $\beta>0$.
   If there exists a linear operator `\Pi_h:V\to V_h` such that

      .. math::
	 :label:

	 b(v-\Pi_hv,q) = 0, \quad \forall v\in V,\,q\in Q_h,

	 \|\Pi_hv\|_V \leq C_{\Pi}\|v\|_V,

   then the discrete inf-sup condition holds.

.. proof:proof::

   For any `q_h\in Q_h`, we have

      .. math::
	 :label:
	 
	 \sup_{v_h\in V_h}\frac{b(v_h,q_h)}{\|v_h\|_V}
	 \geq \sup_{v\in V}\frac{b(\Pi_hv,q_h)}{\|\Pi_h v\|_V}
	 = \sup_{v\in V}\frac{b(v,q_h)}{\|\Pi_hv\|_V}
	 \geq \sup_{v\in V}\frac{b(v,q_h)}{C_{\Pi}\|v\|_V}
	 \geq \frac{\beta}{C_\Pi}\|q_h\|_Q,

   and rearranging and taking the infimum over `q_h\in Q_h` gives

      .. math::
	 :label:

	 \inf_{q_h\in Q_h}\sup_{v_h\in V_h}\frac{b(v_h,q_h)}{\|q_h\|_Q\|v_h\|_V}
	 =\beta_h := \frac{\beta}{C_\Pi}.

The following lemma gives a practical way to find `\Pi_h`.

.. proof:lemma::

   Assume that there exist two maps `\Pi_1,\Pi_2:V\to V_h`, with

      .. math::
	 :label: pi1pi2

	 \|\Pi_1v\|_V \leq c_1\|v\|_V, \, \forall v\in V,

	 \|\Pi_2(I-\Pi_1)v\|_V \leq c_2\|v\|_V, \, \forall v\in V,

	 b(v-\Pi_2v,q_h) = 0,\, \forall v\in V,\,q_h\in Q_h,

   where the constants `c_1` and `c_2` are independent of `h`. Then
   the operator `\Pi_h`, defined by

      .. math::
	 :label:

	 \Pi_hu = \Pi_1 u + \Pi_2(u - \Pi_1u),

   satisfies the conditions of Fortin's trick.

.. proof:proof::

   We have

      .. math::
	 :label:

	 b(\Pi_hw, q_h) = b(\Pi_2(w-\Pi_1)w, q_h) + b(\Pi_1w,q_h),

	 = b(w-\Pi_1w,q_h) + b(\Pi_1w,q_h)

	 = b(w,q_h),

   which gives the second condition of Fortin's trick, and

      .. math::
	 :label:

	 \|\Pi_hw\|_V \leq
	 \|\Pi_2(w-\Pi_1w)\|_V + \|\Pi_1w\|_V \leq (c_1+c_2)\|w\|_V.

For continuous finite element spaces, the Clement operator (which
we shall not describe here) satifies the condition on `\Pi_1`.
In fact, the Clement operator generally satisfies

   .. math::
      :label: clement

      |v-\Pi_1v|_{H^m(K)} \leq c\left(\sum_{\bar{K'} \cap \bar{K}\neq
      0}h_{K'}^{1-m} \|v\|_{H^1(K)}\right)

where `\bar{K}` is the closure of any triangle `K`, and the sum is
taken over all triangles `K'` that share an edge or a vertex with
triangle `K`.
	 
We now use this technique to prove the discrete inf-sup condition for
the MINI element.

.. proof:theorem::

   The MINI element satisfies the discrete inf-sup condition.

.. proof:proof::

   We can use the Clement operator for `\Pi_1`. `\Pi_2:V \to
   (B_3)^2\subset V_h` (i.e. the subspace of `V_h` of functions that
   vanish on all vertices (and hence all edges) is defined via

      .. math::
	 :label:

	 0 = b(\Pi_2v-v,q_h), \, \forall q_h\in Q_h.

   This is well defined since

      .. math::
	 :label:

	 b(\Pi_2v-v,q_h) = \int_{\Omega} q_h\nabla\cdot(\Pi_2v-v)d\,x

	 = \int_\Omega (v-\Pi_2v)\nabla q_h d\, x,

   where we were allowed to integrate by parts since `v,\Pi_2v,q_h`
   are all in `H^1(\Omega)`. We see that our definition can be
   satisfied by picking `\Pi_2v` to be the function in $(B_3)^2$ such
   that

      .. math::
	 :label:

	 \int_K \Phi_2v d\, x x = \int_K v d\, x x,

   for each triangle $K$.

   It can be shown using an inverse inequality (we will take it
   as read here) that

      .. math::
	 :label:

	 \|\Pi_2v\|_{H^r(K)} \leq ch_K^{-r}\|v\|_{L^2(K)}, \,
	 \forall v \in V, \, r=0,1.

   Combining this with Equation :eq:`clement` gives Equation :eq:`pi1pi2`
   and hence we have shown that `\Pi_h` has the properties needed for
   Fortin's trick.
