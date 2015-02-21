.. default-role:: math

================================================
 Assembling and solving finite element problems
================================================


Having constructed functions in finite element spaces and integrated
them, over the domain, we now have the tools in place to actually
assemble and solve a simple finite element problem. To avoid having to
explicitly deal with boundary conditions, we choose in the first
instance to solve a Helmholtz problem, find `u` in some finite element
space `V` such that:

.. math::
   :label: helmholtz

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
   :label: eq_lhs

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

   \mathbf{f}_{M(c, \hat{i})} \stackrel{+}{=} \int_c \Phi_{\hat{i}}\, \left(\sum_{\hat{k}}\,f_{\hat{k}}\,\Phi_{\hat{k}}\right)\,|J|\,\mathrm{d} X \qquad \forall 0 \leq \hat{i} < N

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

   \mathbf{f}_{M(c, \hat{i})} \stackrel{+}{=} \left(\sum_q \Phi(X_q)_{\hat{i}}\, \left(\sum_{\hat{k}}\,f_{\hat{k}}\,\Phi(X_q)_{\hat{k}}\right)\,w_q\,\right) |J| \qquad \forall 0 \leq \hat{i} < N,\, \forall c


Assembling the left hand side matrix
------------------------------------

The left hand side matrix follows a similar pattern, however there are
two new complications. First, we have two unbound indices (`i` and
`j`), and second, the integral involves derivatives. We will address
the question of derivatives first.


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

Using the :ref:`definition of the Jacobian <integration>`, and
using `\nabla_x` and `\nabla_X` to indicate the global and local
gradient operators respectively, we can equivalently write this
expression as:

.. math::
   :label:

   \nabla_x \phi_{M(c,i)}(x) = J^{-\mathrm{T}}\nabla_X\Phi_i(X)

where `J^{-\mathrm{T}} = (J^{-1})^\mathrm{T}` is the transpose of the
inverse of the cell Jacobian matrix.

The assembly algorithm
~~~~~~~~~~~~~~~~~~~~~~

We can start by pulling back :eq:`eq_lhs` to local coordinates:

.. math::
   :label:

   \mathrm{A}_{ij} = 0.

   \mathrm{A}_{M(c, \hat{i}),M(c, \hat{j})} \stackrel{+}{=}
    \int_c\left( \left(J^{-T}\nabla_X \Phi_{\hat{i}}\right)
      \cdot \left(J^{-T}\nabla_X \Phi_{\hat{j}}\right) + \Phi_{\hat{i}}\Phi_{\hat{j}}\,|J|\right) \mathrm{d} X
      \quad\forall 0\leq \hat{i},\hat{j}\leq N,\, \forall c

We can now employ a suitable quadrature rule, `\{X_q\}, \{w_q\}`, to
calculate the integral:

.. math::
   :label:

   \mathrm{A}_{M(c, \hat{i}),M(c, \hat{j})} \stackrel{+}{=}
   \sum_q \left(J^{-T}\nabla_X \Phi_i(X_q)\right)
   \cdot \left(J^{-T}\nabla_X \Phi_j(X_q)\right) + \Phi_i(X_q)\Phi_j(X_q)\,|J|\,w_q
   \quad\forall 0\leq \hat{i},\hat{j}\leq N,\, \forall c

Some readers may find this easier to read using index notation over
the geometric dimensions:

.. math::
   :label:

   \mathrm{A}_{M(c, \hat{i}),M(c, \hat{j})} \stackrel{+}{=}
   \sum_q \left(\sum_{\alpha\beta\gamma}J^{-1}_{\beta\alpha}\left(\nabla_X \Phi_i(X_q)\right)_\beta\,
   J^{-1}_{\gamma\alpha}\left(\nabla_X \Phi_j(X_q)\right)_\gamma\right) + \Phi_i(X_q)\Phi_j(X_q)\,|J|\,w_q
   \quad\forall 0\leq \hat{i},\hat{j}\leq N,\, \forall c


The method of manufactured solutions
------------------------------------

When the finite element method is employed to solve Helmholtz problems
arising in science and engineering, the value forcing function `f`
will come from the application data. However for the purpose of
testing numerical methods and software, it is exceptionally useful to
be able to find values of `f` such that an analytic solution to the
partial differential equation is known. It turns out that there is a
straightforward algorithm for this process. This algorithm is known as
the *method of manufactured solutions*. It has but two steps:

#. Choose a function `\tilde{u}` which satisfies the boundary
   conditions of the PDE.
#. Substitute `\tilde{u}` into the left hand side of
   :eq:`helmholtz`. Set `f` equal to the result of this calculation,
   and now `\tilde{u}` is a solution to :eq:`helmholtz`.

To illustrate this algorithm, suppose we wish to construct `f` such that:

.. math::
   :label:

   \tilde{u} = \cos(4\pi x_0) x_1^2(1 - x_1)^2

is a solution to :eq:`helmholtz`. It is simple to verify that
`\tilde{u}` satisfies the boundary conditions. We then note that:

.. math::
   :label:

   - \nabla^2 \tilde{u} + \tilde{u} = \left((16 \pi^2 + 1) (x_1 - 1)^2 x_1^2 - 12 x_1^2  +12 x_1  - 2\right) \cos(4 \pi x_0)

If we choose:

.. math::
   :label: f_def

   f = \left((16 \pi^2 + 1) (x_1 - 1)^2 x_1^2 - 12 x_1^2  +12 x_1  - 2\right) \cos(4 \pi x_0)

then `\tilde{u}` is a solution to :eq:`helmholtz`.


Errors and convergence
----------------------

The `L^2` error
~~~~~~~~~~~~~~~

When studying finite element methods we are freqently concerned with
convergence in the `L^2` norm. That is to say, if `V` and `W` are
finite element spaces defined over the same mesh, and `f\in V, g\in W`
then we need to calculate:

.. math::
   :label:

   \sqrt{\int_\Omega (f-g)^2 \mathrm{d} x} = \sqrt{\sum_c\int_c \left(\left(\sum_i f_{M_V(c,i)}\Phi_i\right) - \left(\sum_j g_{M_W(c,j)}\Psi_j\right)\right)^2|J|\mathrm{d} X}
   
where `M_V` is the cell-node map for the space `V` and `M_W` is the
cell-node map for the space `W`. Likewise `\{\Phi_i\}` is the local
basis for `V` and `\{\Psi_j\}` is the local basis for `W`.

A complete quadrature rule for this integral will, due to the square
in the integrand, require a degree of precision equal to twice the
greater of the polynomial degrees of `V` and `W`.


Numerically estimating convergence rates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the approximation results from the theory part of the course, we
know that the error term in the finite element solution of the
Helmholtz equation is expected to have the form `\mathcal{O}(h^{p+1})`
where `h` is the mesh spacing and `p` is the polynomial degree of the
finite element space employed. That is to say if `\tilde{u}` is the
exact solution to our PDE and `u_h` is the solution to our finite
element problem, then for sufficiently small `h`:

.. math::
   :label:

   \|u_h - \tilde{u}\|_{L^2} < c h^{p+1}

for some `c>0` not dependent on `h`. Indeed, for sufficiently small
`h`, there is a `c` such that we can write:

.. math::
   :label:

   \|u_h - \tilde{u}\|_{L^2} \approx c h^{p+1}

Suppose we solve the finite element problem for two different (fine)
mesh spacings, `h_1` and `h_2`. Then we have:

.. math::
   :label:

   \|u_{h_1} - \tilde{u}\|_{L^2} \approx c h_1^{p+1}

   \|u_{h_2} - \tilde{u}\|_{L^2} \approx c h_2^{p+1}

or equivalently:

.. math::
   :label:

   \frac{\|u_{h_1} - \tilde{u}\|_{L^2}}{\|u_{h_2} - \tilde{u}\|_{L^2}}
   \approx \left(\frac{h_1}{h_2}\right)^{p+1}

By taking logarithms and rearranging this equation, we can produce a
formula which, given the analytic solution and two numerical
solutions, produces an estimate of the rate of convergence:

.. math::
   :label:

   q = \frac{\ln\left(\displaystyle\frac{\|u_{h_1} - \tilde{u}\|_{L^2}}{\|u_{h_2} - \tilde{u}\|_{L^2}}\right)}
   {\ln\left(\displaystyle\frac{h_1}{h_2}\right)}


Implementing finite element problems
------------------------------------

