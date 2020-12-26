.. default-role:: math

==================
Nonlinear problems
==================

The finite element method may also be employed to numerically solve
*nonlinear* PDEs. In order to do this, we can apply the classical
technique for solving nonlinear systems: we employ an iterative scheme
such as Newton's method to create a sequence of linear problems whose
solutions converge to the correct solution to the
nonlinear problem.

.. note::

    This chapter forms the mastery component of the module in some years, but
    not 2020/2021. It is presented here for reference. None of the material here
    forms part of the module this year.

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

   \int_\Omega \nabla v_0 \cdot (u + 1) \nabla u \, \mathrm{d} x = \int_\Omega v_0g \, \mathrm{d} x \qquad \forall v_0 \in V_0

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

The general weak form of a non-linear problem is, find `u\in V` such that:

.. math::
   :label:

   f(u; v) = 0 \qquad \forall v \in V

The use of a semicolon is a common convention to indicate that `f` is
assumed to be linear in the arguments after the semicolon, but might
be nonlinear in the arguments before the semicolon. In this case,
we observe that `f` may be nonlinear in `u` but is (by
construction) linear in `v`.

The function `f` is called the *residual* of the nonlinear system. In
essence, `f(u; v) = 0 \ \forall v\in V` if and only if `u` is a weak
solution to the PDE. Since the residual is linear in `v`, it suffices
to define the residual for each `\phi_i` in the basis of `V`. For
`\phi_i\in V_0`, the residual is just the weak form of the equation,
but what do we do for the boundary? The simple answer is that we need
a linear functional which is zero if the boundary condition is
satisfied at this test function, and nonzero otherwise. The simplest
example of such a functional is:

.. math::
   :label:

   f(u; \phi_i) = \phi^*_i(u) - \phi^*_i(b)

where `\phi^*_i` is the node associated with basis function `\phi_i`. For
point evaluation nodes, `\phi^*_i(u)` is the value of the proposed solution
at node point `i` and `\phi^*_i(b)` is just the boundary condition
evaluated at that same point.

So for our model problem, we now have a full statement of the residual in terms of a basis function `\phi_i`:

.. math::
   :label: residual

   f(u; \phi_i) = \begin{cases}
      \displaystyle\int_\Omega \nabla \phi_i \cdot \left((u + 1) \nabla u\right) - \phi_i g \, \mathrm{d} x & \phi_i\in V_0\\
      \phi^*_i(u) - \phi^*_i(b) & \phi_i\in V_\Gamma
   \end{cases}

.. hint::
   
   Evaluating the residual requires that the boundary condition be
   evaluated at the boundary nodes. A simple (if slightly inefficient)
   way to achieve this is to interpolate the boundary condition onto a
   function `\hat{b}\in V`.
   
   
Linearisation and Gâteaux Derivatives
-------------------------------------

Having stated our PDE in residual form, we now need to linearise the
problem and thereby employ a technique such as Newton's method. In
order to linearise the residual, we need to differentiate it with
respect to `u`. Since `u` is not a scalar real variable, but is
instead a function in `V`, the appropriate form of differentiation is
the Gâteaux Derivative, given by:

.. math::
   :label:
      
   J(u; v, \hat{u}) = \lim_{\epsilon\rightarrow 0}\frac{f(u+\epsilon\hat{u}; v)-f(u; v)}{\epsilon}.

Here, the new argument `\hat{u}\in V` indicates the "direction" in
which the derivative is to be taken. Let's work through the Gâteaux
Derivative for the residual of our model problem. Assume first that
`v\in V_0`. Then:

.. math::
   :label:

   \begin{split}
   J(u; v, \hat{u}) &= \lim_{\epsilon\rightarrow 0}\frac{\displaystyle\int_\Omega \nabla v \cdot \left((u +\epsilon\hat{u} + 1) \nabla (u + \epsilon\hat{u})\right) - vg \, \mathrm{d} x - \displaystyle\int_\Omega \nabla v \cdot \left((u + 1) \nabla u\right) - vg \, \mathrm{d} x}{\epsilon}\\
   &= \lim_{\epsilon\rightarrow 0}\frac{\displaystyle\int_\Omega \nabla v \cdot \left(\epsilon\hat{u} \nabla u + (u + 1) \nabla (\epsilon\hat{u}) + \epsilon\hat{u} \nabla (\epsilon\hat{u})\right) \, \mathrm{d} x}{\epsilon}\\
   &= \int_\Omega \nabla v \cdot \left(\hat{u} \nabla u + (u + 1) \nabla \hat{u} \right) \, \mathrm{d} x.\\
   \end{split}

Note that, as expected, `J` is linear in `\hat{u}`.

Next, we can work out the boundary case by assuming `v=\phi_i`, one of the basis functions of `V_\Gamma`:

.. math::
   :label:

   \begin{split}
   J(u; \phi_i, \hat{u}) &= \lim_{\epsilon\rightarrow 0}\frac{\phi^*_i(u+\epsilon\hat{u}) - \phi^*_i(b) - \left(\phi^*_i(u) - \phi^*_i(b)\right)}{\epsilon}\\
   &= \phi^*_i(\hat{u}) \qquad \textrm{since } \phi^*_i(\cdot) \textrm{ is linear.}
   \end{split}

Once again, we can observe that `J` is linear in `\hat{u}`. Indeed, if
we choose `\hat{u} = \phi_j` for some `\phi_j` in the basis if `V`
then the definition of a nodal basis gives us:

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

   J(u^n; \phi_i, \phi_j) \hat{u}_j = - f(u^n; \phi_i).

For our nonlinear diffusion problem, the matrix `J` is given by:

.. math::
   :label:

   J(u^n; \phi_i, \phi_j) =
   \begin{cases}
   \displaystyle\int_\Omega \nabla \phi_i \cdot \left(\phi_j \nabla u^n + (u^n + 1) \nabla \phi_j \right) \, \mathrm{d} x & \phi_i\in V_0\\
   \delta_{ij} & \phi_i \in V_\Gamma,
   \end{cases}

and the right hand side vector `f` is given by :eq:`residual`. This
matrix, `J`, is termed the *Jacobian matrix* of `f`.

Stopping criteria for Newton's method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since Newton's method is an iterative algorithm, it creates a
(hopefully convergent) sequence of approximations to the correct
solution to the original nonlinear problem. How do we know when to
accept the solution and terminate the algorithm?

The answer is that the update, `\hat{u}` which is calculated at each
step of Newton's method is itself an approximation to the error in the
solution. It is therefore appropriate to stop Newton's method when
this error estimate becomes sufficiently small in the `L^2` norm.

The observant reader will observe that `\hat{u}` is in fact
an estimate of the error in the *previous* step. This is indeed true:
the Newton step is both an estimate of the previous error and a
correction to that error. However, having calculated the error
estimate, it is utterly unreasonable to not apply the corresponding
correction.

.. note::

   Note!
   
   Another commonly employed stopping mechanism is to consider the
   size of the residual `f`. However, the residual is not actually a
   function in `V`, but is actually a linear operator in `V^*`. Common
   practice would be to identify `f` with a function in `V` by simply
   taking the function whose coefficients match those of `f`. The
   `L^2` or `l^2` norm is then taken of this function and this value
   is used to determine when convergence has occured.

   This approach effectively assumes that the Riesz map on `V` is the
   trivial operator which identifies the basis function
   coefficients. This would be legitimate were the inner product on
   `V` the `l^2` dot product. However, since the inner product on `V`
   is defined by an integral, the mesh resolution is effectively
   encoded into `f`. This means that this approach produces
   convergence rates which depend on the level of mesh refinement.
   
   Avoiding this mesh dependency requires the evaluation of an
   operator norm or, equivalently, the solution of a linear system in
   order to find the Riesz representer of `f` in `V`. However, since
   the error-estimator approach given above is both an actual estimate
   of the error in the solution, and requires no additional linear
   solves, it should be regarded as a preferable approach. For a full
   treatment of Newton methods, see :cite:`Deuflhard2011`.


Stopping threshold values
~~~~~~~~~~~~~~~~~~~~~~~~~

What, then, qualifies as a sufficiently small value of our error
estimate? There are two usual approaches:

relative tolerance
   Convergence is deemed to occur when the estimate
   becomes sufficiently small compared with the first error estimate
   calculated.  This is generally the more defensible approach since
   it takes into account the overall scale of the solution. `10^{-6}`
   would be a reasonably common relative tolerance.

absolute tolerance
   Computers employ finite precision arithmetic, so there is a limit
   to the accuracy which can ever be achieved. This is a difficult
   value to estimate, since it depends on the number and nature of
   operations undertaken in the algorithm. A common approach is to set
   this to a very small value (e.g. `10^{-50}`) initially, in order to
   attempt to ensure that the relative tolerance threshold is
   hit. Only if it becomes apparent that the problem being solved is
   in a regime for which machine precision is a problem is a higher
   absolute tolerance set.

It is important to realise that both of these criteria involve making
essentially arbitrary judgements about the scale of error which is
tolerable. There is also a clear trade-off between the level of error
tolerated and the cost of performing a large number of Newton
steps. For realistic problems, it is therefore frequently expedient
and/or necessary to tune the convergence criteria to the particular
case.

In making these judgements, it is also important to remember that the
error in the Newton solver is just one of the many sources of error in
a calculation. It is pointless to expend computational effort in an
attempt to drive the level of error in this component of the solver to
a level which will be swamped by a larger error occurring somewhere
else in the process.

Failure modes
~~~~~~~~~~~~~

Just as with the Newton method for scalar problems, Newton iteration
is not guaranteed to converge for all nonlinear problems or for all
initial guesses. If Newton's method fails to converge, then the
algorithm presented so far constitutes an infinite loop. It is
therefore necessary to define some circumstances in which the
algorithm should terminate having failed to find a solution. Two such
circumstances are commonly employed:

maximum iterations
   It is a reasonable heuristic that Newton's method has failed if it
   takes a very large number of iterations. What constitutes "too
   many" is once again a somewhat arbitrary judgement, although if the
   approach takes many tens of iterations this should always be cause
   for reconsideration!

diverged error estimate
   Newton's method is not guaranteed to produce a sequence of
   iterations which monotonically decrease the error, however if the
   error estimate has increased to, say, hundreds or thousands of
   times its initial value, this would once again be grounds for the
   algorithm to fail.

Note that these failure modes are heuristic: having the algorithm
terminate for these reasons is really an instruction to the user to
think again about the problem, the solver, and the initial guess.


Implementing a nonlinear problem
--------------------------------

.. note::

   This problem is intentionally stated in more general terms than the
   previous ones. It is your responsibility to decide on a code
   structure, to derive a method of manufactured solutions answer, and
   to create the convergence tests which demonstrate that your
   solution is correct.

.. proof:exercise::

   The :math:`p`-laplacian is a generalisation of the laplacian from
   a second derivative to an arbitrary derivative. It is nonlinear for
   :math:`p\neq2`.

   Implement :func:`~fe_utils.solvers.mastery.solve_mastery` so that it solves
   the following problem using degree 1 Lagrange elements over the
   unit square domain:

   .. math::
      :label: mastery

      -\nabla\cdot\left(|\nabla u|^{p-2} \nabla u\right) = g

      u = b \textrm{ on } \Gamma

      p = 4

   Select the solution `u=e^{xy}` and compute the required forcing function `g` so
   that your solution solves the equations. Make sure your boundary
   condition function `b` is consistent with your chosen solution!

   For this problem, it is not possible to use the zero function as an
   initial guess for Newton's method. A much better choice is to treat
   the 2-laplacian as an approximation to the 4-laplacian, and
   therefore to solve Poisson's equation first to obtain a good
   initial guess for the 4-laplacian problem.
   
   Your submitted answer will consist of:

   1. A written component containing your derivation of:

      a. The weak form of :eq:`mastery`; and 

      b. the Jacobian; and

      c. the forcing term implied by the specified manufactured solution; and

      d. an explanation of why the zero function cannot be used as an initial guess for the solution.

      A neatly hand-written or a typed submission are equally acceptable.

   2. The code to implement the solution. This should be in
      ``fe_utils.solvers.mastery.py`` in your implementation. A
      convergence test for your code is provided in
      ``test/test_12_mastery_convergence.py``.

      The submission of your mastery exercise, and indeed the entire
      implementation exercise will be on Blackboard. You will submit a
      PDF containing the derivations above, and the git sha1 for the
      commit you would like to have marked.

   .. hint::

      It is an exceptionally useful aid to debugging to have your
      Newton iteration print out the value of the error norm and the
      iteration number for each iteration. If you wish to see the
      printed output while running the test, you can pass the ``-s``
      option to ``py.test``.

   .. hint::

      You could parametrise your code by `p`. By setting `p=2`, you
      reduce your problem to the linear case. You can use the linear
      case to test your code initially, before setting `p=4` for the
      actual exercise. Note that, in the linear case, Newton's method
      will converge in exactly one iteration (although your algorithm
      will have to actually calculate two steps in order to know that
      convergence has occurred).
