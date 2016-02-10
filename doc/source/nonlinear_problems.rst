.. default-role:: math

==================
Nonlinear problems
==================

The finite element method may also be employed to numerically solve
*nonlinear* PDEs. In order to do this, we can employ the classical
technique for solving nonlinear systems: we employ an iterative scheme
such as Newton's method to create a sequence of linear problems whose
solutions enable us to converge on the correct solution to the
nonlinear problem.

.. note::

   This section is the mastery exercise for this module. This exercise
   is explicitly intended to test whether you can bring together what
   has been learned in the rest of the module in order to go beyond
   what has been covered in lectures and labs.


A model problem
---------------

As a simple case of a non-linear PDE, we can consider a steady
non-linear diffusion equation. This is similar to the Poisson problem,
except that the diffusion rate now depends on the value of the
solution:

.. math::
   :label: diffusion

   -\nabla\cdot\left((u+1)\nabla u\right) = g

   u = b \textrm{ on } \Gamma

where `g` and `b` are given functions defined over `\Omega` and
`\Gamma` respectively.
   
We can create the weak form of :eq:`diffusion` by integrating by parts
and taking the boundary conditions into account. The problem becomes,
find `u\in V` such that:

.. math::
   :label: weakdiffusion

   \int_\Omega \nabla v_0 \cdot (u + 1) \nabla u \, \mathrm{d} x = \int_\Omega vg \qquad \forall v_0 \in V_0

   u_\Gamma = b.

Once more, `V_0` is the subspace of `V` spanned by basis functions which
vanish on the boundary, `V = V_0 \oplus V_\Gamma`, and `u = u_0 +
u_\Gamma` with `u_0\in V_0` and `u_\Gamma\in V_\Gamma`. This is
corresponds directly with the weak form of the Poisson equation we
already met. However, :eq:`weakdiffusion` is still nonlinear in `u` so
we cannot simply substitute `u = u_i\phi_i` in order to obtain a
linear matrix system to solve.
   
Residual form
-------------

The general form of a non-linear problem is, find `u\in V` such that:

.. math::
   :label:

   f(u; v) = 0 \qquad \forall v \in V

The use of a semicolon is a common convention to indicate that `f` is
assumed to be linear in the arguments after the semicolon, but might
be nonlinear in the arguments before the semicolon. In this case,
we're observing that `f` may be nonlinear in `u` but is (by
construction) linear in `v`.

The function `f` is called the *residual* of the nonlinear system. In
essence, if `u` is not a solution to the nonlinear problem, then `f(u;
v)` will be nonzero for some `v\in V`. Since the residual is linear in
`v`, it suffices to define the residual for each `\phi_i` in the basis
of `V`. For `\phi_i\in V_0`, the residual is just the weak form of the
equation, but what do we do for the boundary? The simple answer is
that we need a linear functional which is zero if the boundary
condition is satisfied at this test function, and nonzero
otherwise. The simplest example of such a functional is:

.. math::
   :label:

   f(u; \phi_i) = n_i(u) - n_i(b)

where `n_i` is the node associated with basis function `\phi_i`. For
point evaluation nodes, `n_i(u)` is the value of the proposed solution
at node point `i` and `n_i(b)` is just the boundary condition
evaluated at that same point.

So for our model problem, we now have a full statement of the residual in terms of a basis function `\phi_i`:

.. math::
   :label: residual

   f(u; \phi_i) = \begin{cases}
      \displaystyle\int_\Omega \nabla \phi_i \cdot \left((u + 1) \nabla u\right) - vg \, \mathrm{d} x & \phi_i\in V_0\\
      n_i(u) - n_i(b) & \phi_i\in V_\Gamma
   \end{cases}

   
Linearisation and Gâteaux Derivatives
-------------------------------------

The residual is the tool we need in order to be able to linearise our
problem and thereby employ a technique such as Newton's method. In
order to linearise the residual, we need to differentiate it with
respect to `u`. Since `u` is not a scalar real variable, but is
instead a function in `V`, the appropriate derivative is the Gâteaux
Derivative, given by:

.. math::
   :label:
      
   J(u; v, \hat{u}) = \lim_{\epsilon\rightarrow 0}\frac{f(u+\epsilon\hat{u}; v)-f(u; v)}{\epsilon}

where the new argument `\hat{u}\in V` indicates the "direction" in
which the derivative is to be taken. Let's work through the Gâteaux
Derivative for the residual of our model problem. Assume first that
`v\in V_0`. Then:

.. math::
   :label:

   \begin{split}
   J(u; v, \hat{u}) &= \lim_{\epsilon\rightarrow 0}\frac{\displaystyle\int_\Omega \nabla v \cdot \left((u +\epsilon\hat{u} + 1) \nabla (u + \epsilon\hat{u})\right) + vg \, \mathrm{d} x - \displaystyle\int_\Omega \nabla v \cdot \left((u + 1) \nabla u\right) + vg \, \mathrm{d} x}{\epsilon}\\
   &= \lim_{\epsilon\rightarrow 0}\frac{\displaystyle\int_\Omega \nabla v \cdot \left(\epsilon\hat{u} \nabla u + (u + 1) \nabla (\epsilon\hat{u}) + \epsilon\hat{u} \nabla (\epsilon\hat{u})\right) \, \mathrm{d} x}{\epsilon}\\
   &= \int_\Omega \nabla v \cdot \left(\hat{u} \nabla u + (u + 1) \nabla \hat{u} \right) \, \mathrm{d} x.\\
   \end{split}

Note that, as expected, `J` is linear in `\hat{u}`.

Next, we can work out the boundary case by assuming `v=\phi_i`, one of the basis functions of `V_\Gamma`:

.. math::
   :label:

   \begin{split}
   J(u; \phi_i, \hat{u}) &= \lim_{\epsilon\rightarrow 0}\frac{n_i(u+\epsilon\hat{u}) - n_i(b) - \left(n_i(u) - n_i(b)\right)}{\epsilon}\\
   &= n_i(\hat{u}) \qquad \textrm{since } n_i(\cdot) \textrm{ is linear.}
   \end{split}

Once again, we can observe that `J` is linear in `\hat{u}`. Indeed, if choose `\hat{u} = \phi_j` for some `phi_j` in the basis if `V` then the definition of a nodal basis gives us:

.. math::
   :label:

   J(u; \phi_i, \phi_j) = \delta_{ij}

A Taylor expansion and Newton's method
--------------------------------------

Since we now have the derivative of the residual with respect to a
perturbation to the prospective solution `u`, we can write the first
terms of a Taylor series approximation for the value of the residual at a perturbed solution `u+\hat{u}`:

.. math::
   :label:

   f(u+\hat{u}; v) = f(u; v) + J(u; v, \hat{u}) +\ldots \qquad \forall v\in V.

Now, just as in the scalar case, Newton's method consists of
approximating the function (the residual) by the first two terms and
solving for the update that will set these terms to zero. In other
words:

.. math::
   :label:

   u^{n+1} = u^n + \hat{u}

where `\hat{u} \in V` is the solution to:

.. math::
   :label: newton_update

   J(u^n; v, \hat{u}) = - f(u^n; v) \qquad \forall v \in V.

In fact, :eq:`newton_update` is simply a linear finite element
problem! To make this explicit, we can expand `v` and `\hat{u}` in
terms of basis functions:

.. math::
   :label:

   J(u^n; \phi_i, \phi_j) \hat{u}_j = - f(u^n; \phi_j).

For our nonlinear diffusion problem, the matrix `J` is given by:

.. math::
   :label:

   J(u^n; \phi_i, \phi_j) =
   \begin{cases}
   \int_\Omega \nabla \phi_i \cdot \left(\phi_j \nabla u^n + (u^n + 1) \nabla \phi_j \right) \, \mathrm{d} x & \phi_i\in V_0\\
   \delta_{ij} & \phi_i \in V_\Gamma,
   \end{cases}

and the right hand side vector `f` is given by :eq:`residual`.

Implementing a nonlinear problem
--------------------------------

.. note::

   This problem is intentionally stated in more general terms than the
   previous ones. It is your responsibility to decide on a code
   structure, to derive a method of manufactured solutions answer, and
   to create the convergence tests which demonstrate that your
   solution is correct.


.. exercise::

   Write a Python program which solves the following problem using
   degree 1 Lagrange elements over the unit square domain.

   .. math::
   
      -\nabla\cdot\left((u^2+1)\nabla u\right) = g

      u = b \textrm{ on } \Gamma

   Select a solution and compute the required forcing function `g` so
   that your solution solves the equations. Make sure your boundary
   condition function `b` is consistent with your chosen solution!

   Provide test code which demonstrates that your solution converges
   at the correct rate.

.. hint::

   You can either implement your own Newton solver, or install the
   :python:`scipy` package and work out how to use the
   :python:`scipy.optimize.newton_krylov` function.

.. hint::

   You'll need to implement some form of stopping criterion for your
   Newton solver iteration. A common criterion is to stop when the
   `L^2` norm of the residual has decreased by a large enough factor.
