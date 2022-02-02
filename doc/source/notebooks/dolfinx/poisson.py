# %%
# !wget "https://fem-on-colab.github.io/releases/fenicsx-install-real.sh" -O "/tmp/fenicsx-install.sh" && bash "/tmp/fenicsx-install.sh"
# !wget "https://fem-on-colab.github.io/releases/gmsh-install.sh" -O "/tmp/gmsh-install.sh" && bash "/tmp/gmsh-install.sh"
# !apt install libgl1-mesa-glx xvfb
# !pip install pyvista

# %% [markdown]
#
# # Poisson equation
#
# This notebook is based on the introductory DOLFINx demo `demo_poisson.py`. In
# addition, it attempts to describe some of the 'magic' behind-the-scenes in a
# modern automatic finite element code.
#
# ## Equation and problem definition
#
# We we solve the Poisson equation subject to both Dirichlet and Neumann
# boundary conditions
#
# $$
# \begin{align}
#    - \nabla^{2} u &= f \quad {\rm in} \ \Omega, \\
#                 u &= 0 \quad {\rm on} \ \Gamma_{D}, \\
#                 \nabla u \cdot n &= g \quad {\rm on} \ \Gamma_{N}. \\
# \end{align}
# $$
#
# Here, $f$ and $g$ are input data and $n$ denotes the outward directed
# boundary normal. The most standard variational form of Poisson equation
# reads: find $u \in V$ such that
#
# $$a(u, v) = L(v) \quad \forall \ v \in V,$$
#
# where $V$ will be a P1 finite element space and the bilinear and linear
# forms are defined as
#
# $$
# \begin{align}
# a(u, v) &= \int_{\Omega} \nabla u \cdot \nabla v \, {\rm d}
# x, \\
# L(v)    &= \int_{\Omega} f v \, {\rm d} x
# + \int_{\Gamma_{N}} g v \, {\rm d} s.
# \end{align}
# $$
#
# We shall consider the following definitions of the input functions, the
# domain, and the boundaries:
#
# * $\Omega = [0,1] \times [2,1]$ (a rectangle)
# * $\Gamma_{D} = \{(0, y) \cup (1, y) \subset \partial \Omega\}$
#   (Dirichlet boundary)
# * $\Gamma_{N} = \{(x, 0) \cup (x, 1) \subset \partial \Omega\}$
#   (Neumann boundary)
# * $g = \sin(5x)$ (normal derivative on $\Gamma_N$)
# * $f = 10\exp(-((x - 0.5)^2 + (y - 0.5)^2) / 0.02)$ (source term in $\Omega$)
#
# ## Implementation
#
# This description goes through the implementation of a solver for the above
# described Poisson equation step-by-step.
#
# First, the necessary modules are imported:

# %%
import numpy as np

import ufl
from dolfinx import fem, io, mesh, plot
from ufl import ds, dx, exp, grad, inner, sin

from mpi4py import MPI
from petsc4py.PETSc import ScalarType

# %% [markdown]
# We begin by defining a mesh of the domain and a finite element function space
# $V$ defined on the mesh. We create a rectangular mesh using built-in function
# provided by method `create_rectangle`. In order to create a mesh consisting
# of 32 x 16 rectangles with each rectangle divided into two triangles, we do as
# follows:


# %%
rectangle_mesh = mesh.create_rectangle(
    comm=MPI.COMM_WORLD,
    points=((0.0, 0.0), (2.0, 1.0)),
    n=(32, 16),
    cell_type=mesh.CellType.triangle
)

V = fem.FunctionSpace(rectangle_mesh, ("Lagrange", 1))

# %% [markdown]
# The second argument to `FunctionSpace` is a tuple consisting of ``(family,
# degree)``, where `family` is the finite element family, and ``degree``
# specifies the polynomial degree. Thus, in this case, our space `V` consists
# of first-order continuous Lagrange finite element functions.
#
# Next, we want to consider the Dirichlet boundary condition. A simple Python
# function, returning a boolean, can be used to define the boundary for the
# Dirichlet boundary condition ($\Gamma_D$). The function should return `True`
# for those points on the boundary and `False` for the points outside. In our
# case, we want to say that the points $(x, y)$ such that $x = 0$ or
# $x = 1$ are on $\Gamma_D$.


# %%
# Create a function that takes an array of points x and returns an array of
# `True` or `False` if the point is or is not on the boundary
def marker(x): return np.logical_or(
    np.isclose(x[0], 0.0), np.isclose(x[0], 2.0))

# %% [markdown]
# To identify the degrees of freedom, we first find the facets (entities of
# dimension 1) that live on the boundary of the mesh, and satisfies our
# criteria for `\Gamma_D`.


# %%
# Define boundary condition on x = 0 or x = 1
facets = mesh.locate_entities_boundary(rectangle_mesh, dim=1, marker=marker)

# %% [markdown]
# Then, we use the function `locate_dofs_topological` to identify all degrees
# of freedom that is located on those facets (including the vertices).

# %%
dofs = fem.locate_dofs_topological(V=V, entity_dim=1, entities=facets)

# %% [markdown]
# The Dirichlet boundary condition can be created using the method
# `dirichletbc`. `dirichletbc` takes three arguments: the value of the boundary
# condition, the degrees of freedom on which the condition applies to, and the
# function space. The final definition of the Dirichlet boundary condition is
# then:

# %%
bc = fem.dirichletbc(value=ScalarType(0), dofs=dofs, V=V)

# %% [markdown]
# Next, we want to express the variational problem.  First, we need to specify
# the trial function `u` and the test function `v`, both living in the function
# space `V`. We do this by defining a `TrialFunction` and a `TestFunction` on
# the previously defined `FunctionSpace` `V`.
#
# Further, the source $f$ and the boundary normal derivative $g$ are involved
# in the variational forms, and hence we must specify these.
#
# With these ingredients, we can write down the bilinear form `a` and
# the linear form `L` (using UFL operators). In summary, this reads

# %%
# Define variational problem
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)
x = ufl.SpatialCoordinate(rectangle_mesh)
f = 10 * exp(-((x[0] - 0.5)**2 + (x[1] - 0.5)**2) / 0.02)
g = sin(5 * x[0])
a = inner(grad(u), grad(v)) * dx
L = inner(f, v) * dx + inner(g, v) * ds

# %% [markdown]
# Next, we initialize a solver using the `LinearProblem` class.
# This class is initialized with the arguments ``a``, ``L``, and ``bc`` as
# follows: In this problem, we use a direct LU solver from PETSc, which is
# defined through the dictionary ``petsc_options``.

# %%
problem = fem.LinearProblem(a, L, bcs=[bc], petsc_options={
                            "ksp_type": "preonly", "pc_type": "lu"})

# %% [markdown]
# Now, we have specified the variational forms and can consider the solution of
# the variational problem. The method `problem.solve()` returns a `Function`
# `uh` containing the solution. A `Function` represents a function living in a
# finite element function space.

# %%
uh = problem.solve()

# %% [markdown]
# The function `u` will be modified during the call to solve. The default
# settings for solving a variational problem have been used. However, the
# solution process can be controlled in much more detail if desired.
#
# A `Function` can be plotted and saved to file. Here, we output the solution
# to an XDMF file for later visualization and also plot it using pyvista

# %%
# Save solution in XDMF format
with io.XDMFFile(rectangle_mesh.comm, "poisson.xdmf", "w") as file:
    file.write_mesh(rectangle_mesh)
    file.write_function(uh)

try:
    import pyvista
    pyvista.set_jupyter_backend("static")
    cells, types, x = plot.create_vtk_mesh(V)
    grid = pyvista.UnstructuredGrid(cells, types, x)
    grid.point_data["u"] = uh.x.array.real
    grid.set_active_scalars("u")

    plotter = pyvista.Plotter(notebook=True)
    plotter.add_mesh(grid, show_edges=True)
    warped = grid.warp_by_scalar()
    plotter.add_mesh(warped)
    plotter.show()
except ImportError:
    print("pyvista not installed")
