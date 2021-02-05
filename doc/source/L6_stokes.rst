.. default-role:: math

Stokes equation (Mastery topic)
===============================

In this section we consider finite element discretisations of the Stokes
equation of a viscous fluid, given by

.. math::

   -\mu\nabla\cdot\epsilon(u) + \nabla p = f, \quad \nabla\cdot u = 0,
    \quad \epsilon(u) = \frac{1}{2}\left( \nabla u + \nabla u^T),

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


