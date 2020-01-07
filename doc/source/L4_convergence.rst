.. default-role:: math

Convergence of finite element approximations
============================================

In this section we develop tools to prove convergence of finite
element approximations to the exact solutions of PDEs.

Weak derivatives
----------------

Consider a triangulation `\mathcal{T}` with recursively refined
triangulations `\mathcal{T}_h` and corresponding finite element spaces
`V_h`.  Given stable finite element variational problems, we have a
sequence of solutions `u_h` as `h\to 0`, satisfying the
`h`-independent bound

.. math::
      
   \|u_h\|_{H^1(\Omega)} \leq C.

What are these solutions converging to? We need to find a Hilbert
space that contains all `V_h` as `h\to0`, that extends the `H^1` norm
to the `h\to 0` limit of finite element functions.

Our first task is to define a derivative that works for all finite
element functions, without reference to a mesh. This requires some
preliminary definitions, starting by considering some very smooth
functions that vanish on the boundaries together with their
derivatives (so that we can integrate by parts as much as we like).

.. proof:definition:: Compact support on `\Omega`

   A function `u` has compact support on `\Omega` if there exists `\epsilon>0`
   such that `u(x)=0` when `\min_{y\in\partial\Omega}|x-y|<\epsilon`.

.. proof:definition:: `C^\infty_0(\Omega)`
   
   We denote by `C^\infty_0(\Omega)` the subset of `C^\infty(\Omega)`
   corresponding to functions that have \emph{compact support} on
   `\Omega`.

Next we will define a space containing the generalised derivative.

.. proof:definition:: `L^1_{loc}`
		      
   For triangles `K \subset \interior(\Omega)`, we define

   .. math::

      \|u\|_{L^1(K)} = \int_K |u|\diff x,

   and

   .. math::

      L^1_K = \left\{u:\|u\|_{L^1(K)}<\infty\right\}.

   Then

   .. math::

      L^1_{loc} = \left\{
      f: f \in L^1(K) \quad \forall K\subset\interior(\Omega)
      \right
      \}.
