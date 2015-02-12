.. default-role:: math

================================================
 Assembling and solving finite element problems
================================================


Having constructed functions in finite element spaces and integrated
them, over the domain, we now have the tools in place to actually
assemble and solve a simple finite element problem. To avoid having to
explicitly deal with boundary conditions, we choose in the first
instance to solve a helmholtz problem, find `u` in some finite element
space `V` such that:

.. math::
   :label:

   - \nabla^2 u + u = f

   \nabla u \cdot \mathbf{n} = 0 \textrm{ on }\Gamma

where `\Gamma` is the domain boundary and `\mathrm{n}` is the outward
pointing normal to that boundary. `f` is a known function which, for
simplicity, we will assume lies in `V`. Next, we form the weak form of
this equation by multiplying by a test function in `V` and integrating
over the domain. We integrate the Laplacian term by parts. The problem
becomes, find `u\in V` such that:

.. math::
   :label: weak_helmholtz

   \int_\Omega \nabla v \cdot \nabla u + vu\, \mathrm{d} x
   - \underbrace{\int_\Gamma \nabla u \cdot \mathbf{n}\, \mathrm{d} s}_{=0} = 
   \int_\Omega v f\, \mathrm{d} x \qquad \forall v \in V

If we write `\{\phi_i\}_{i=0}^{n-1}` for our basis for `V`, and recall that
it is sufficient to ensure that :eq:`weak_helmholtz` is satisfied for
each function in the basis then the problem is now, find coefficients `u_i` such that:

.. math::
   :label:

   \int_\Omega \sum_{j}\left(\nabla \phi_i \cdot \nabla (u_j\phi_j) + \phi_i u_j\phi_j\right)\, \mathrm{d} x
   = \int_\Omega \sum_k\phi_i f_k\phi_k\, \mathrm{d} x \qquad \forall\, 0\leq i < n 

Since the left hand side is linear in the scalar coefficients `u_j`, we can move them out of the integral:

.. math::
   :label:

   \sum_{j}\left(\int_\Omega \nabla \phi_i \cdot \nabla \phi_j + \phi_i\phi_j\, \mathrm{d} x\, u_j\right)
   = \int_\Omega \sum_k\phi_i f_k\phi_k\, \mathrm{d} x \qquad \forall\, 0\leq i < n 

We can write this as a matrix equation:

.. math::
   :label:

   \mathrm{A}\mathbf{u} = \mathbf{f}

where:

.. math::
   :label:

   \mathrm{A}_{ij} = \int_\Omega \nabla \phi_i \cdot \nabla \phi_j + \phi_i\phi_j\, \mathrm{d} x

.. math::
   :label:

   \mathbf{u}_j = u_j

.. math::
   :label: eq_rhs

   \mathbf{f}_i = \int_\Omega \sum_k\phi_i f_k\phi_k\, \mathrm{d} x


Assembling the right hand side
------------------------------

The assembly of these integrals exploits the same decomposition
property we exploited previously to integrate functions in finite
element spaces. For example, :eq:`eq_rhs` can be rewritten as:

.. math::
   :label:

   \mathbf{f}_i = \sum_c \int_c \phi_i f_k\phi_k\,  \mathrm{d} x

This has a practical impact once we realise that only a few basis
functions are non-zero in each element. This enables us to write an
efficient algorithm for right hand side assembly. Assume that at the
start of our algorithm:

.. math::
   :label:

   \mathbf{f}_i = 0.

Now for each cell `c`, we execute:

.. math::
   :label:

   \mathbf{f}_{M(c, \hat{i})} \stackrel{+}{=} \int_c \left(\Phi_{\hat{i}}\, \sum_{\hat{k}}\left(f_{\hat{k}}\,\Phi_{\hat{k}}\right)\, \right) \mathrm{d} X \qquad \forall 0 \leq \hat{i} < N

Where `M` is the cell-node map for the finite element space `V`, `N`
is the number of nodes per element in `V`, and
`\{\Phi_{\hat{i}}\}_{\hat{i}=0}^{N-1}` are the local basis
functions. In other words, we visit each cell and conduct the integral
for each local basis function, and add that integral to the total for
the corresponding global basis function.

By choosing a suitable quadrature rule, `\{X_q\}, \{w_q\}`, we can
write this as:

.. math::
   :label:

   \mathbf{f}_{M(c, \hat{i})} \stackrel{+}{=} \sum_q \left(\Phi(X_q)_{\hat{i}}\, \sum_{\hat{k}}\left(f_{\hat{k}}\,\Phi(X_q)_{\hat{k}}\right)\, \right) |J| \qquad \forall 0 \leq \hat{i} < N


Assembling the left hand side matrix
------------------------------------

The left hand side matrix follows a similar pattern, however there are
two new complications. First, we have two unbound indices (`i` and
`j`), and second, the integral involves derivatives. 

Pulling gradients back to the reference element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On element `c`, there is a straightforward relationship between the
local and global bases:

.. math::
   :label: pullback

   \phi_{M(c,i)}(x) = \Phi_i(X)

We can also, as we showed in :ref:`coordinates`, express the global
coordinate `x` in terms of the local coordinate `X`.

What about `\nabla\phi`? We can write the gradient operator in
component form and apply :eq:`pullback`:

.. math::
   :label: 

   \frac{\partial\phi_{M(c,i)}(x)}{\partial x_\alpha} =
   \frac{\partial\Phi_i(X)}{\partial{x_\alpha}}\quad \forall\, 0\leq \alpha < \dim

However, the expression on the right involves the gradient of a local
basis function with respect to the global coordinate variable `x`. We
employ the chain rule to express this gradient with respect to the
local coordinates, `X`:

.. math::
   :label: 

   \frac{\partial\phi_{M(c,i)}(x)}{\partial x_\alpha} =
   \sum_{\beta=0}^{\dim-1}\frac{\partial X_\beta}{\partial x_\alpha}\frac{\partial\Phi_i(X)}{\partial{X_\beta}}\quad \forall\, 0\leq \alpha < \dim

Using the definition of the Jacobian from :eq:`jacobian_def`, and
using `\nabla_x` and `\nabla_X` to indicate the global and local
gradient operators respectively, we can equivalently write this
expression as:

.. math::
   :label:

   \nabla_x \phi_{M(c,i)}(x) = J^{-\mathrm{T}}\nabla_X\Phi_i(X)

where `J^{-\mathrm{T}} = (J^{-1})^\mathrm{T}` is the transpose of the
inverse of the cell Jacobian matrix.
