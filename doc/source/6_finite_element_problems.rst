.. default-role:: math

================================================
 Assembling and solving finite element problems
================================================

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/Dn_xGn2WayY>`_

Having constructed functions in finite element spaces and integrated
them over the domain, we now have the tools in place to actually
assemble and solve a simple finite element problem. To avoid having to
explicitly deal with boundary conditions, we choose in the first
instance to solve a Helmholtz problem [#helmholtz]_, find `u` in some finite element
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
   - \underbrace{\int_\Gamma v \nabla u \cdot \mathbf{n}\, \mathrm{d} s}_{=0} = 
   \int_\Omega v f\, \mathrm{d} x \qquad \forall v \in V

If we write `\{\phi_i\}_{i=0}^{n-1}` for our basis for `V`, and recall that
it is sufficient to ensure that :eq:`weak_helmholtz` is satisfied for
each function in the basis then the problem is now, find coefficients `u_i` such that:

.. math::
   :label:

   \int_\Omega \sum_{j}\left(\nabla \phi_i \cdot \nabla (u_j\phi_j) + \phi_i u_j\phi_j\right)\, \mathrm{d} x
   = \int_\Omega \phi_i\, \sum_k f_k\phi_k\, \mathrm{d} x \qquad \forall\, 0\leq i < n 

Since the left hand side is linear in the scalar coefficients `u_j`, we can move them out of the integral:

.. math::
   :label:

   \sum_{j}\left(\int_\Omega \nabla \phi_i \cdot \nabla \phi_j + \phi_i\phi_j\, \mathrm{d} x\, u_j\right)
   = \int_\Omega \phi_i\,\sum_k f_k\phi_k\, \mathrm{d} x \qquad \forall\, 0\leq i < n 

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

   \mathbf{f}_i = \int_\Omega \phi_i\,\sum_k f_k\phi_k\, \mathrm{d} x


Assembling the right hand side
------------------------------

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/H-eLGYwzpcI>`_

The assembly of these integrals exploits the same decomposition
property we exploited previously to integrate functions in finite
element spaces. For example, :eq:`eq_rhs` can be rewritten as:

.. math::
   :label:

   \mathbf{f}_i = \sum_c \int_c \phi_i \,\sum_k f_k\phi_k\,  \mathrm{d} x

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

   \mathbf{f}_{M(c, \hat{i})} \stackrel{+}{=} \int_c \Phi_{\hat{i}}\, \left(\sum_{\hat{k}}\,f_{M(c,\hat{k})}\,\Phi_{\hat{k}}\right)\,|J|\,\mathrm{d} X \qquad \forall 0 \leq \hat{i} < N

Where `M` is the cell-node map for the finite element space `V`, `N`
is the number of nodes per element in `V`, and
`\{\Phi_{\hat{i}}\}_{\hat{i}=0}^{N-1}` are the local basis
functions. In other words, we visit each cell and conduct the integral
for each local basis function, and add that integral to the total for
the corresponding global basis function.

By choosing a suitable quadrature rule, `\{X_q\}, \{w_q\}`, we can
write this as:

.. math::
   :label: rhs_index

   \mathbf{f}_{M(c, \hat{i})} \stackrel{+}{=} \left(\sum_q \Phi(X_q)_{\hat{i}}\, \left(\sum_{\hat{k}}\,f_{M(c,\hat{k})}\,\Phi(X_q)_{\hat{k}}\right)\,w_q\,\right) |J| \qquad \forall 0 \leq \hat{i} < N,\, \forall c


Assembling the left hand side matrix
------------------------------------

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/yQ5vJpCeJaU>`_


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

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/e20G9pjr7IA>`_


We can start by pulling back :eq:`eq_lhs` to local coordinates:

.. math::
   :label:

   \mathrm{A}_{ij} = 0.

   \mathrm{A}_{M(c, \hat{i}),M(c, \hat{j})} \stackrel{+}{=}
    \int_c\left( \left(J^{-T}\nabla_X \Phi_{\hat{i}}\right)
      \cdot \left(J^{-T}\nabla_X \Phi_{\hat{j}}\right) + \Phi_{\hat{i}}\Phi_{\hat{j}}\right)|J|\, \mathrm{d} X
      \quad\forall 0\leq \hat{i},\hat{j}< N,\, \forall c

We now employ a suitable quadrature rule, `\{X_q\}, \{w_q\}`, to
calculate the integral:

.. math::
   :label: lhs_assemble

   \mathrm{A}_{M(c, \hat{i}),M(c, \hat{j})} \stackrel{+}{=}
   \sum_q \bigg(\left(J^{-T}\nabla_X \Phi_{\hat{i}}(X_q)\right)
   \cdot \left(J^{-T}\nabla_X \Phi_{\hat{j}}(X_q)\right) + \Phi_{\hat{i}}(X_q)\Phi_{\hat{j}}(X_q)\bigg)|J|\,w_q
   \quad\forall 0\leq \hat{i},\hat{j}< N,\, \forall c

Some readers may find this easier to read using index notation over
the geometric dimensions:

.. math::
   :label: lhs_index

   \mathrm{A}_{M(c, \hat{i}),M(c, \hat{j})} \stackrel{+}{=}
   \sum_q \left(\sum_{\alpha\beta\gamma}J^{-1}_{\beta\alpha}\left(\nabla_X \Phi_{\hat{i}}(X_q)\right)_\beta\,
   J^{-1}_{\gamma\alpha}\left(\nabla_X \Phi_{\hat{j}}(X_q)\right)_\gamma + \Phi_{\hat{i}}(X_q)\Phi_{\hat{j}}(X_q)\right)|J|\,w_q
   \quad\forall 0\leq \hat{i},\hat{j}< N,\, \forall c

A note on matrix insertion
~~~~~~~~~~~~~~~~~~~~~~~~~~

For each cell `c`, the right hand sides of equations
:eq:`lhs_assemble` and :eq:`lhs_index` have two free indices,
`\hat{i}` and `\hat{j}`. The equation therefore assembles a local
`N\times N` matrix corresponding to one integral for each test
function, trial function pair on the current element. This is then
added to the global matrix at the row and column pairs given by the
cell node map `M(c, \hat{i})` and `M(c, \hat{j})`.

.. _figmatrix-insertion:

.. figure:: global_assembly.*
   :width: 70%

   Computing integrals for each local test and trial function produces
   a local dense (in this case, `3\times 3`) matrix. The entries in
   this matrix are added to the corresponding global row and column
   positions in the global matrix.

.. hint::

   One might naïvely expect that if ``nodes`` is the vector of global
   node numbers for the current cell, ``m`` is the matrix of local
   integral values and ``A`` is the global matrix, then the Python
   code might look like::

       A[nodes, nodes] += m # DON'T DO THIS!

   Unfortunately, :mod:`numpy` interprets this as an instruction to
   insert a vector into the diagonal of ``A``, and will complain that
   the two-dimensional right hand side does not match the
   one-dimensional left hand side. Instead, one has to employ the
   :func:`numpy.ix_` function::

       A[np.ix_(nodes, nodes)] += m # DO THIS!

   No such problem exists for adding values into the global right hand
   side vector. If ``l`` is the global right hand side vector and
   ``v`` is the vector of local right hand integrals, then the
   following will work just fine::

       l[nodes] += v


Sparse matrices
~~~~~~~~~~~~~~~

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/YYyDOTrrgzU>`_


Each row of the global matrix corresponds to a single global basis
function. The number of non-zeros in this row is equal to the number
of other basis functions which are non-zero in the elements where the
original basis function is non-zero. The maximum number of non-zeros
on a row may vary from a handful for a low degree finite element to a
few hundred for a fairly high degree element. The important point is
that it is essentially independent of the size of the mesh. This means
that as the number of cells in the mesh increases, the proportion of
the matrix entries on each row which have the value zero increases.

For example, a degree 4 Lagrange finite element space defined on
`64\times 64` unit square triangular mesh has about 66000 nodes. The
full global matrix therefore has more that 4 billion entries and, at 8
bytes per matrix entry, will consume around 35 gigabytes of memory!
However, there are actually only around 23 nonzeros per row, so more
than 99.9% of the entries in the matrix are zeroes.

Instead of storing the complete matrix, sparse matrix formats store
only those entries in the matrix which are nonzero. They also have to
store some metadata to describe where in the matrix the non-zero
entries are stored. There are various different sparse matrix formats
available, which make different trade-offs between memory usage,
insertion speed, and the speed of different matrix
operations. However, if we make the (conservative) assumption that a
sparse matrix takes 16 bytes to store each nonzero value, instead of 8
bytes, then we discover that in the example above, we would use less
than 25 megabytes to store the matrix. The time taken to solving the
matrix system will also be vastly reduced since operations on zeros
are avoided.

.. hint::

   The :mod:`scipy.sparse` package provides convenient interfaces
   which enable Python code to employ a variety of sparse matrix
   formats using essentially identical operations to the dense matrix
   case. The skeleton code already contains commands to construct
   empty sparse matrices and to solve the resulting linear system. You
   may, if you wish, experiment with choosing other sparse formats
   from :mod:`scipy.sparse`, but it is very strongly suggested that
   you do **not** switch to a dense numpy array; unless, that is, you
   particularly enjoy running out of memory on your computer!


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

.. proof:exercise::

   ``fe_utils/solvers/helmholtz.py`` contains a partial implementation of
   the finite element method to solve :eq:`weak_helmholtz` with `f`
   chosen as in :eq:`f_def`. Your task is to implement the
   :func:`~fe_utils.solvers.helmholtz.assemble` function using :eq:`rhs_index`, and
   :eq:`lhs_assemble` or :eq:`lhs_index`. The comments in the
   :func:`~fe_utils.solvers.helmholtz.assemble` function provide some guidance as to the steps
   involved. You may also wish to consult the :func:`~fe_utils.utils.errornorm`
   function as a guide to the
   structure of the code required.

   Run::

      python fe_utils/solvers/helmholtz.py --help

   for guidance on using the script to view the solution, the analytic
   solution and the error in your solution. In addition,
   ``test/test_11_helmholtz_convergence.py`` contains tests that the
   helmholtz solver converges at the correct rate for degree 1, 2 and
   3 polynomials.

   .. warning::

      ``test/test_12_helmholtz_convergence.py`` may take many seconds or
      even a couple of minutes to run, as it has to solve on some
      rather fine meshes in order to check convergence.

.. rubric:: Footnotes

.. [#helmholtz] Strictly speaking this is the positive definite Helmholtz
                problem. Changing the sign on `u` produces the
                indefinite Helmholtz problem, which is significantly
                harder to solve.
