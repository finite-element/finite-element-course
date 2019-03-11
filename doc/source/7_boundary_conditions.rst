.. default-role:: math

=============================
Dirichlet boundary conditions
=============================

The Helmholtz problem we solved in the previous part was chosen to
have homogeneous Neumann or *natural* boundary conditions, which can
be implemented simply by cancelling the zero surface integral. We can
now instead consider the case of Dirichlet, or *essential* boundary
conditions. Instead of the Helmholtz problem we solved before, let us
now specify a Poisson problem with homogeneous Dirichlet conditions, find `u` in
some finite element space `V` such that:

.. math::
   :label: poisson

   -\nabla^2 u = f

   u = 0  \textrm{ on }\Gamma 

In order to implement the Dirichlet conditions, we need to decompose
`V` into two parts:

.. math::
   :label:

   V = V_0 \oplus V_\Gamma

where `V_\Gamma` is the space spanned by those functions in the basis
of `V` which are non-zero on `\Gamma`, and `V_0` is the space spanned
by the remaining basis functions (i.e.  those basis functions which
vanish on `\Gamma`). It is a direct consequence of the nodal nature of
the basis that the basis functions for `V_\Gamma` are those
corresponding to the nodes on `\Gamma` while the basis for `V_0` is
composed of all the other functions.

We now write the weak form of :eq:`poisson`, find `u=u_0 + u_\Gamma`
with `u_0 \in V_0` and `u_\Gamma \in V_\Gamma` such that:

.. math::
   :label:

   \int_\Omega \nabla v_0 \cdot \nabla (u_0+u_\Gamma) \, \mathrm{d} x
   - \underbrace{\int_\Gamma v_0 \nabla (u_0+u_\Gamma) \cdot
   \mathbf{n}\, \mathrm{d} s}_{=0} = \int_\Omega v_0\, f\, \mathrm{d} x
   \qquad \forall v_0 \in V_0

   u_\Gamma = 0 \qquad \textrm{ on } \Gamma

There are a number of features of this equation which require some explanation:

#. We only test with functions from `V_0`. This is because it is only
   necessary that the differential equation is satisfied on the interior
   of the domain: on the boundary of the domain we need only satisfy the
   boundary conditions.
#. The surface integral now cancels because `v_0` is guaranteed to be
   zero everywhere on the boundary.
#. The `u_\Gamma` definition actually implies that `u_\Gamma=0`
   everywhere, since all of the nodes in `V_\Gamma` lie on the boundary.

This means that the weak form is actually:

.. math::
   :label: weakpoisson

   \int_\Omega \nabla v_0 \cdot \nabla u \, \mathrm{d} x
    = \int_\Omega v_0\, f\, \mathrm{d} x
   \qquad \forall v_0 \in V_0

   u_\Gamma = 0 


An algorithm for homogeneous Dirichlet conditions
-------------------------------------------------

The implementation of homogeneous Dirichlet conditions is actually
rather straightforward. 

#. The system is assembled completely ignoring the Dirichlet conditions. 
   This results in a global matrix and vector which are correct on the rows
   corresponding to test functions in `V_0`, but incorrect on the `V_\Gamma` rows.
#. The global vector rows corresponding to boundary nodes are set to 0.
#. The global matrix rows corresponding to boundary nodes are set to 0.
#. The diagonal entry on each matrix row corresponding to a boundary node is set to 1.

This has the effect of replacing the incorrect boundary rows of the
system with the equation `u_i = 0` for all boundary node numbers `i`.

.. hint::

   This algorithm has the unfortunate side effect of making the global
   matrix non-symmetric. If a symmetric matrix is required (for
   example in order to use a symmetric solver), then forward
   substition can be used to zero the boundary columns in the matrix,
   but that is beyond the scope of this module.

Implementing boundary conditions
--------------------------------

Let:

.. math::

   f = \left(16 \pi^2 (x_1 - 1)^2 x_1^2 - 2 (x_1 - 1)^2 - 8 (x_1 - 1) x_1 - 2 x_1^2\right) \sin(4 \pi x_0)

With this definition, :eq:`weakpoisson` has solution:

.. math::

   u = \sin(4 \pi x_0) (x_1 - 1)^2 x_1^2

.. proof:exercise::

   ``fe_utils/solvers/poisson.py`` contains a partial implementation of
   this problem. You need to implement the :func:`assemble`
   function. You should base your implementation on your
   ``fe_utils/solvers/helmholtz.py`` but take into account the difference
   in the equation, and the boundary conditions. The
   :func:`fe_utils.solvers.poisson.boundary_nodes` function in ``fe_utils/solvers/poisson.py`` is
   likely to be helpful in implementing the boundary conditions. As
   before, run::

     python fe_utils/solvers/poisson.py --help
     
   for instructions (they are the same as for
   ``fe_utils/solvers/helmholtz.py``). Similarly,
   ``test/test_12_poisson_convergence.py`` contains convergence tests
   for this problem.


Inhomogeneous Dirichlet conditions
----------------------------------

The algorithm described here can be extended to inhomogeneous systems
by setting the entries in the global vector to the value of the
boundary condition at the corresponding boundary node. This additional
step is required for the mastery exercise, but will be explained in
more detail in the next section.
