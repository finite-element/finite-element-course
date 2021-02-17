.. default-role:: math

.. _mixed:

==============
Mixed problems
==============

.. note::

   This section is the mastery exercise for this module. This exercise
   is explicitly intended to test whether you can bring together what
   has been learned in the rest of the module in order to go beyond
   what has been covered in lectures and labs.

   This exercise is not a part of the third year version of this module.

As an example of a mixed problem, let's take the Stokes problem presented in
:numref:`stokes` of the analysis part of the course. The weak form of the
Stokes problem presented in :numref:`Definition %s <weak_stokes>` is find
`(u,p)\in V\times Q` such that:

.. math::
    :label:

    a(u,v) + b(v, p) & = \int_\Omega f\cdot v d\, x,
      
    b(u,q) & = 0, \quad \forall (v,q) \in V\times Q,

where

.. math::
    :label:

    a(u,v) & = \int_\Omega \epsilon(u):\epsilon(v)d\, x,

    b(v,q) & = \int_\Omega q \nabla\cdot v d\, x,

    V & =(\mathring{H}^1(\Omega))^n,

    Q & =\mathring{L}^2(\Omega), 

and where `(\mathring{H}^1(\Omega))^n` is the subspace of `H^1(\Omega)^n` for
which all components vanish on the boundary, and `\mathring{L}^2(\Omega)` is
the subspace of `L^2(\Omega)` for which the integral of the function over the
domain vanishes. This last constraint was introduced to remove the null space
of constant pressure functions from the system. This constraint introduces a
little complexity into the implementation. So instead, we will redefine
`\mathring{L}^2(\Omega)` to be the subspace of `L^2(\Omega)` constrained to
take the value 0 at some arbitrary but specified point. For example, one might
choose to require the pressure at the origin to vanish. This is also an
effective way to remove the nullspace, but it is simpler to implement. We will
implement the two-dimensional case (`n=2`).

In choosing a finite element subspace of `V \times Q` we will similarly choose
a simpler to implement, yet still stable, space than was chosen in
:numref:`Analysis Section %s <stokes>`. The space we will use is the lowest order
Taylor-Hood space :cite:`Taylor1973`. This has:

.. math::
    :label:

    V^h & = P2(\Omega)^2

    Q^h & = P1(\Omega)

i.e. quadratic velocity and linear pressure on each cell. We note that 
`Q^h\in H^1(\Omega)` but since `H^1(\Omega) \subset L^2(\Omega)`, this is not
itself a problem. We will impose further constraints on the spaces in the
form of Dirichlet boundary conditions to ensure that the solutions found are in
fact in `V \times Q`.

In addition to the finite element functionality we have already implemented,
there are two further challenges we need to address. First, the implementation
of the vector-valued space `P2(\Omega)^2`m and second, the implementation of
functions and matrices defined over the mixed space `V^h \times Q^h`.

Vector-valued finite elements
-----------------------------

Consider the local representation of `P2(\Omega)^2` on one element. The scalar
`P2` element on one triangle has 6 nodes, one at each vertex and one at each
edge. If we write `\{\Phi_i\}_{i=0}^{5}` for the scalar basis, then a basis
`\{\mathbf{\Phi}_i\}_{i=0}^{11}` for the vector-valued space is given by:

.. math::
    :label: vector_basis

    \mathbf{\Phi}_i(X) = \Phi_{i\,//\,2}(X)\,\mathbf{e}_{i\,\%\,2}

where `//` is the integer division operator, `\%` is the modulus operator, and
`{\mathbf{e}_0, \mathbf{e}_1}` is the standard basis for `\mathbb{R}^2`. That is to say, we
interleave `x` and `y` component basis functions.

.. note::

    Maybe nodal diagram here.

We can practically implement vector function spaces by implementing a new class
:class:`fe_utils.finite_elements.VectorFiniteElement`. The constructor
(:meth:`~object.__init__`) of this new class should take a
:class:`~fe_utils.finite_elements.FiniteElement` and construct the
corresponding vector element. For current purposes we can assume that the
vector element will always have a vector dimension equal to the element
geometric and topological dimension (i.e. 2 if the element is defined on a
triangle). We'll refer to this dimension as `d`.

Implementing :class:`VectorFiniteElement`
.........................................

:class:`VectorFiniteElement` needs to implement as far as possible the same
interface as :class:`~fe_utils.finite_elements.FiniteElement`. Let's think
about how to do that.

:data:`cell`, :data:`degree`
    Same as for the input :class:`~fe_utils.finite_elements.FiniteElement`.
:data:`entity_nodes`
    There will be twice as many nodes, and the node ordering is such that each
    node is replaced by a `d`-tuple. For example the scalar triangle P1
    entity-node list is:

    .. code-block:: python3

        {
            0 : {0 : [0], 1 : [1], 2 : [2]},
            1 : {0 : [], 1 : [], 2 : []},
            2 : {0 : []}
        }
    
    The vector version is achieved by looping over the scalar version and
    returning a mapping with the pair `2n, 2(n+1)` in place of node `n`:

    .. code-block:: python3

        {
            0 : {0 : [0, 1], 1 : [2, 3], 2 : [4, 5]},
            1 : {0 : [], 1 : [], 2 : []},
            2 : {0 : []}
        }
:data:`nodes_per_entity`:
    Each entry will be `d` times that on the input
    :class:`~fe_utils.finite_elements.FiniteElement`.

Tabulation
..........

In order to tabulate the element, we can use :eq:`vector_basis`. We first
call the tabulate method from the input
:class:`~fe_utils.finite_elements.FiniteElement`, and we use this and
:eq:`vector_basis` to produce the array to return. Notice that the array
will both have a basis functions dimension which is `d` times longer than the
input element, and will also have an extra dimension to account for the
multiplication by `\mathbf{e}_{i\,\%\,d}`. This means that the tabulation array
with :data:`grad=False` will now be rank 3, and that with :data:`grad=True`
will be rank 4. Make sure you keep track of which rank is which!
The :class:`VectorFiniteElement` will need to keep a reference to the
input :class:`~fe_utils.finite_elements.FiniteElement` in order to facilitate
tabulation. 

Nodes
.....

Even though we didn't need the nodes of the :class:`VectorFiniteElement` to
construct its basis, we will need them to implement interpolation. In
:numref:`Definition %s <nodalbasis>` we learned that
the nodes of a finite element are related to the corresponding nodal basis by:

.. math::
    :label:

    \mathbf{\Phi}^*_i(\mathbf{\Phi}_j) = \delta_{ij}

From :eq:`vector_basis` and assuming, as we have throughout the course,
that the scalar finite element has point evaluation nodes given by:

.. math::
    :label:

    \Phi_i(v) = v(X_i),

it follows that:

.. math::
    :label: vectornodes

    \mathbf{\Phi}^*_i(v) & = \Phi^*_{i\,//\,d}(\mathbf{e}_{i\,\%\,d}\cdot v)

    & = \mathbf{e}_{i\,\%\,d}\cdot v(X_{i\,//\,d})

.. hint::

    To see that this is the correct nodal basis, choose
    :math:`v=\mathbf{\Phi}_j` in :eq:`vectornodes` and substitute
    :eq:`vector_basis` for :math:`\mathbf{\Phi}_j`.

This means that the correct :data:`VectorFiniteElement.nodes` attribute is
the list of nodal points from the input
:class:`~fe_utils.finite_elements.FiniteElement` but with each point repeated
`d` times. It will also be necessary to add another attribute, perhaps
:data:`node_weights` which is a rank 2 array whose `i`-th row is the correct
canonical basis vector to contract with the function value at the `i`-th node (`\mathbf{e}_{i\,\%\,d}`).


Vector-valued function spaces
-----------------------------

Assuming we correctly implement :class:`VectorFiniteElement`, 
:class:`~fe_utils.function_spaces.FunctionSpace` should work out of the box.
In particular, the global numbering algorithm only depends on having a correct
local numbering so this should work unaltered. Indeed, one way to check your
:class:`VectorElement` implementation is to use
:file:`plot_function_space_nodes` and check that you have two adjacent
numbers printed over each other at each node location.

Functions in vector-valued spaces
---------------------------------

The general form of a function in a vector-valued function space is:

.. math::
    :label:

    f = f_i \mathbf{\Phi}_i(X).

That is to say, the basis functions are vector valued and their coefficients
are still scalar. This means that if the :class:`VectorFiniteElement` had a
correct entity-node list then the core functionality of the existing
:class:`~fe_utils.function_spaces.Function` will automatically be correct. In
particular, the array of values will have the correct extent. However,
interpolation and plotting of vector valued fields will require some
adjustment.

Interpolating into vector-valued spaces
.......................................

Since the form of the nodes of a :class:`VectorFiniteElement` is different from
that of a scalar element, there will be some changes required in the
:meth:`~fe_utils.function_spaces.Function.interpolate()` method. Specifically,
in these two lines:

.. code-block:: python3

    node_coords = np.dot(coord_map, vertex_coords)

    self.values[fs.cell_nodes[c, :]] = [fn(x) for x in node_coords]

The first of these lines may need adjusting because :data:`coord_map` is the
result of tabulating the :class:`VectorFiniteElement` and, depending on where
the additional rank was added to the tabulation matrix, the :func:`np.dot` may
need to be replaced by a different tensor contraction.

The second line will need to take into account the dot product with the
canonical basis from :eq:`vectornodes`. These changes will need to be made
conditional on the class of finite element passed in, so that the code doesn't
break in the scalar element case.

Plotting functions in vector-valued spaces
..........................................

.. note:: 

    Quiver plots.

Mixed function spaces
---------------------

The Stokes' equations are defined over the mixed function space `W = V \times Q`.
Here "mixed" simply means that there are two solution variables, and therefore
two solution spaces. Functions in `W` are pairs `(u, p)` where `u\in V` and
`p\in Q`. If `\{\phi_i\}_{i=0}^{n-1}` is a basis for `V` and
`\{\psi_j\}_{j=0}^{m-1}` then a basis for `W` is given by:

.. math::

    \{\omega_i\}_{i=0}^{n+m-1}=\{(\phi_i, 0)\}_{i=0}^{n-1} \cup \{(0,
    \psi_{j-n})\}_{j=n}^{n+m-1}.
    
This in turn enables us to write `w\in W` in the form `w=w_i\omega_i` as we
would expect for a function in a finite element space.