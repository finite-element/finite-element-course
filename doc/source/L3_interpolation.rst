.. default-role:: math
.. default-role:: math
		  
Interpolation operators
=======================

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490673290"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f3b6a076-d90c-42c5-90a4-ac8e00ed6b79>`_

In this section we investigate how continuous functions can be
approximated by finite element functions. We start locally,
looking at a single finite element, and then move globally to
function spaces on a triangulation.

Local and global interpolation operators
----------------------------------------

.. proof:definition:: Local interpolator

   Given a finite element `(K,\mathcal{P},\mathcal{N})`, with
   corresponding nodal basis `\{\phi_i\}_{i=0}^k`. Let `v`
   be a function such that `N_i(v)` is well-defined for all `i`.
   Then the local interpolator `\mathcal{I}_K` is an operator
   mapping `v` to `\mathcal{P}` such that

   .. math::
      
      (I_Kv)(x) = \sum_{i=0}^kN_i(v)\phi_i(x).

We now discuss some useful properties of the local interpolator.
      
.. _Ilinear:

.. proof:lemma:: 
  
   The operator `I_K` is linear.

.. proof:exercise::

   Prove :numref:`Lemma {number}<Ilinear>`.

.. _I_same_nodes:
   
.. proof:lemma::

   .. math::
      
      N_i(I_K(v)) = N_i(v), \, \forall\,  0\leq i\leq k.

.. proof:exercise::

   Prove :numref:`Lemma {number}<I_same_nodes>`.
      
.. _I_projection:

.. proof:lemma::
      
   `I_K` is the identity when restricted to `\mathcal{P}`.

.. proof:exercise::

   Prove :numref:`Lemma {number}<I_projection>`.

By combining together the local interpolators in each triangle of the
triangulation, we obtain the global interpolator into the finite
element space.
   
.. proof:definition:: Global interpolator

   Let `V_h` be a finite element space constructed from a triangulation
   `\mathcal{T}_h` with finite elements
   `(K_i,\mathcal{P}_i,\mathcal{N}_i)`, each with a `C^m` geometric
   decomposition. The global interpolator `\mathcal{I}_h` is defined by
   `\mathcal{I}_hu \in V_h` such that
   
   .. math::

      \mathcal{I}_hu|_K = I_Ku

   for each `K \in \mathcal{T}_h`.

Measuring interpolation errors
------------------------------

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490673157"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e811ac32-0c1c-43ee-b661-ac8e00ee051e>`_

Next we look at how well we can approximate continuous functions using
the interpolation operator, i.e. we want to measure the approximation
error `\mathcal{I}_h u - u`. We are interested in integral
formulations, so we want to use integral quantities to measure errors.
We have already seen the `L^2` norm. It is also useful to take
derivatives into account when measuring the error. To discuss higher
order derivatives, we introduce the multi-index.

.. proof:definition:: Multi-index.

   For `d`-dimensional space, a multi-index `\alpha=(\alpha_1,\ldots,\alpha_d)`
   assigns the number of partial derivatives in each Cartesian direction.
   We write `|\alpha|=\sum_{i=1}^d\alpha_i`.

This means we can write mixed partial derivatives, for example if
`\alpha=(1,2)` then

.. math::

   D^\alpha u = \frac{\partial^3 u}{\partial x\partial y^2}.

Now we can define some norms involving derivatives for measuring
errors.

.. proof:definition:: \(H^k\) seminorm and norm

   The `H^k` seminorm is defined as

   .. math::

      |u|_{H^k}^2 = \sum_{|\alpha|=k}\int_\Omega |D^\alpha u|^2 \, dx,

   where the sum is taken over all multi-indices of size `k` i.e. all the
   derivatives are of degree `k`.
   
   The `H^k` norm is defined as

   .. math::

      \|u\|_{H^k}^2 = \sum_{i=0}^k |u|_{H^i}^2.

   where we conventionally write `|u|_{H^0}=\|u\|_{L^2}`.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490673099"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=efbbb34b-ae76-4150-98e2-ac8e00f12d27>`_
   
To help to estimate interpolation errors, we quote the following
important result (which we will return to much later).

.. proof:theorem:: Sobolev's inequality (for continuous functions)

   Let `\Omega` be an `n`-dimensional domain with Lipschitz boundary,
   and let `u` be a continuous function with `k` continuous derivatives,
   i.e. `u \in C^{k,\infty}(\Omega)`.
   Let
   `k` be an integer with `k>n/2`. Then there exists a constant
   `C` (depending only on `\Omega`) such that

   .. math::

      \|u\|_{C^\infty(\Omega)} = \max_{x \in \Omega}|u(x)|
      \leq C\|u\|_{H^k(\Omega)}.

.. proof:proof::

   See a functional analysis course or textbook.

This is extremely useful because it means that we can measure the
`H^k` norm by integrating and know that it gives an upper bound on the
value of `u` at each point. We say that `u` is in `C^\infty(\Omega)`
if `\|u\|_{C^\infty(\Omega)}<\infty`, and Sobolev's inequality tells
us that this is the case if `\|u\|_{H^k(\Omega)}<\infty`.

This result can be easily extended to
derivatives.

.. proof:corollary:: Sobolev's inequality for derivatives (for continuous functions)

   Let `\Omega` be a `n`-dimensional domain with Lipschitz boundary,
   and let `u \in C^{k,\infty}(\Omega)`
   Let
   `k` be an integer with `k-m>n/2`. Then there exists a constant
   `C` (depending only on `\Omega`) such that

   .. math::

      \|u\|_{C^{m,\infty}(\Omega)} :=
      \sum_{|\alpha|\leq m}\max_{x \in \Omega}|D^\alpha u(x)|
      \leq C\|u\|_{H^k(\Omega)}.

.. proof:proof::

   Just apply Sobolev's inequality to the `m` derivatives of `u`.

Approximation by averaged Taylor polynomials
--------------------------------------------

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490673003"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=62d286c0-1efd-4b8a-9570-ac8e00f3835d>`_

The basic tool for analysing interpolation error for continuous
functions is the Taylor series. Rather than taking the Taylor series
about a single point, since we are interested in integral quantities,
it makes sense to consider an averaged Taylor series over some region
inside each cell. This will become important later when we start
thinking about more general types of derivative that only exist in an
integral sense.

.. _def-averaged-taylor:

.. proof:definition:: Averaged Taylor polynomial

   Let `\Omega\subset \mathbb{R}^n` be a domain with diameter `d`, that
   is star-shaped with respect to a ball `B`
   contained within `\Omega`. For `f\in C^{k,\infty}` the
   averaged Taylor polynomial `Q_{k,B}f\in \mathcal{P}_k` is defined
   as

   .. math::
      
      Q_{k,B} f(x) = \frac{1}{|B|}\int_{B} T^kf(y,x) \, d y,

   where `T^kf` is the Taylor polynomial of degree `k` of `f`,

   .. math::
      
      T^k f(y,x) = \sum_{|\alpha|\leq k} D^\alpha f(y)\frac{(x-y)^\alpha}{\alpha!},

      \alpha! = \prod_{i=1}^n \alpha_i!,
      
      x^\alpha = \prod_{i=1}^n x_i^{\alpha_i}.

.. proof:exercise::

   Show that
   
   .. math::
  
      D^\beta Q_{k,B} f = Q_{k-|\beta|,B}  D^\beta f,
  
  where `Q^l_B` is the degree `l` averaged Taylor polynomial of
  `f`, and `D^\beta` is the `\beta`-th derivative where `\beta` is
  a multi-index.
      
..
  End of week 5 material
   
Now we develop an estimate of the error `T^kf - f`.

.. dropdown:: A first video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490672898"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=80896f93-3f64-421e-846e-ac8e00f12c99>`_

.. dropdown:: A second video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490672679"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=cb47271d-b53f-46fc-805b-ac8f00a28be7>`_

.. _taylorerror:

.. proof:theorem::
   
   Let `\Omega\subset \mathbb{R}^n` be a domain with diameter `d`,
   that is star-shaped with respect to a ball `B` contained within
   `\Omega`.  Then there exists a constant `C(k,n)` such that for
   `0\leq |\beta| \leq k+1` and all `f \in C^{k+1,\infty}(\Omega)`,

   .. math::
      
      \|D^\beta(f-Q_{k,B}f)\|_{L^2(\Omega)} \leq C\frac{|\Omega|^{1/2}}{|B|^{1/2}}
      d^{k+1-|\beta|}|f|_{H^{k+1}(\Omega)}.
      
.. proof:proof::

   The Taylor remainder theorem (see a calculus textbook) gives

   .. math::
      
      f(x) - T_kf(y,x) = 
      (k+1)\sum_{|\alpha|=k+1}\frac{(x-y)^\alpha}{\alpha!}
      \int_0^1 D^\alpha f(ty + (1-t)x)t^k\, d t,

   when `f \in C^{k+1,\infty}`.

   Integration over `y` in `B` and dividing by `|B|` gives

   .. math::
      
      f(x) - Q_{k,B}f(x) = \frac{k+1}{|B|}\sum_{|\alpha|=k+1}
      \int_B\frac{(x-y)^\alpha}{\alpha!}\times 
      \int_0^1 D^\alpha f(ty + (1-t)x)t^k\, d t \, d y.

   Then

   .. math::
      
      \int_\Omega |f(x)-Q_{k,B}f(x)|^2\, d x
      &\leq C\frac{d^{2(k+1)}}{|B|^2}
      \sum_{|\alpha|=k+1}\int_\Omega
      \left(
      \int_B\int_0^1 |D^\alpha f(ty+(1-t)x)|t^k \, d t\, d y\right)^2\, d x,
      
      &\leq C_0\frac{d^{2(k+1)}}{|B|^2}
      \sum_{|\alpha|=k+1}\int_\Omega
      \int_B\int_0^1 |D^\alpha f(ty+(1-t)x)|^2 \, d t\, d y 
      \int_B\int_0^1 t^{2k}\, d t\, d y\,\, d x.

   Then

   .. math::
   
      \int_\Omega |f(x)-Q_{k,B}f(x)|^2\, d x 
      \leq C_1\frac{d^{2(k+1)}}{|B|^2}
      \sum_{|\alpha|=k+1}\int_\Omega
      \int_B\int_0^1 |D^\alpha f(ty+(1-t)x)|^2 \, d t\, d y \, d x.

   We will get the result by changing variables and exchanging
   the `t`, `y` and `x` integrals. To avoid a singularity when
   `t=0` or `t=1`,
   for each `\alpha` term we can split the `t` integral
   into `[0,1/2]` and `[1/2,1]`. Call these terms I and II.

   Denote by `g_\alpha` the extension by zero of `D^\alpha f` to
   `\mathbb{R}^n`. Then

   .. math::
      
      I &=  \int_B \int_0^{1/2} \int_{\mathbb{R}^n} |g_\alpha(ty+(1-t)x)|^2
      \, d x \, d t\, d y,
      
      &=  \int_B \int_0^{1/2} \int_{\mathbb{R}^n} |g_\alpha((1-t)x)|^2\, d x \, d t
      \, d y,
      
      &=  \int_B \int_0^{1/2} \int_{\mathbb{R}^n} |g_\alpha(z)|^2
      (1-t)^{-n}
      \, d z \, d t
      \, d y,
   
      &\leq  2^{n-1}|B|\int_\Omega |D^\alpha f(z)|^2\, d z.

   Similarly, for `II`,

   .. math::
      
      II &=  \int_B \int_{1/2}^1 \int_{\mathbb{R}^n} |g_\alpha(ty+(1-t)x)|^2
      \, d x \, d t\, d y,
      
      &=  \int_B \int_{1/2}^1 \int_{\mathbb{R}^n} |g_\alpha(ty)|^2\, d x \, d t
      \, d y, 

      &=  \int_B \int_{1/2}^1 \int_{\mathbb{R}^n} |g_\alpha(z)|^2
      t^{-n}
      \, d z \, d t
      \, d y,
      
      &\leq  2^{n-1}|B|\int_\Omega |D^\alpha f(z)|^2\, d z.


   Hence, we obtain the required bounds for `|\beta|=0`. For higher
   derivatives we use the fact that

   .. math::

      D^\beta Q_{k,B} f(x) = Q_{k-|\beta|,B}D^\beta f(x),

   which immediately leads to the estimate for `|\beta|>0`.

Now we develop this into an estimate that depends on the diameter
of the triangle we are interpolating to.

.. _unittaylorerr:

.. proof:corollary::

   Let `K_1` be a triangle with diameter `1`.
   There exists a constant `C(k,n)` such that

   .. math::
      
      \|f-Q_{k,B}f\|_{H^k(K_1)} \leq C|f|_{H^{k+1}(K_1)}.

.. proof:proof::

   Take the maximum over the constants for the derivative contributions
   of the left-hand side with `d=1` and use the previous result.

Local and global interpolation errors
-------------------------------------

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490672385"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=de44e00c-6a67-43ac-88e1-ac8e00ee04aa>`_

The following exercises give a specific example of the interpolation error
results of this section without directly using the previous estimate
(because they specialise to `L^2`, 1D and linear elements).

.. proof:exercise::

   Let `w\in C^2([0,1])`, with `w(0)=w(1)=0`. Show that

   .. math::
      
      \int_0^1 w(x) \,d x \leq c\int_0^1 w''(x) \,d x.

   Hints: use the Schwarz inequality,

   .. math::

      (\int_0^1 f(x)g(x) \, dx)^2 \leq (\int_0^1 f(x)^2 \, dx)
      (\int_0^1 g(x)^2 \, dx)^2,

   (which we shall discuss in more generality in Section 4), together
   with Rolle's theorem, that says that if `u` has continuous
   derivative then for all `x`, there exists `0\leq \xi \leq 1` such
   that

   .. math::

      u(x) = \int_\xi^x u'(y) \, dy.

.. proof:exercise::

   Using the previous exercise, show that for all `u\in C^2([0,1])`, there
   exists a constant `c` such that

   .. math::

      \int_0^1 (u(x)-\mathcal{I}_{[0,1]}u(x))^2 \, dx
      \leq c\int_0^1 u''(x)^2 \, dx,

   where `\mathcal{I}_{[0,1]}` is the interpolator to the finite element
   with `K=[0,1]`, `P` is the linear polynomials on `K`, and the nodal
   variables are `N_0[p]=p(0)` and `N_1[p]=p(1)`.

.. proof:exercise::

   Using the previous exercise, show that for all `u\in C^2([a,b])`, there
   exists a constant `c` such that

   .. math::

      \int_a^b (u(x)-\mathcal{I}_{[a,b]}u(x))^2 \, dx
      \leq c(b-a)^4\int_a^b u''(x)^2 \, dx,

   where `\mathcal{I}_{[a,b]}` is the interpolator to the finite element
   with `K=[a,b]`, `P` is the linear polynomials on `K`, and the nodal
   variables are `N_0[p]=p(a)` and `N_1[p]=p(b)`.

.. proof:exercise::

   Using the previous exercise, show that for a P1 finite element space
   defined on the interval `[a,b]` with maximum mesh cell width `h`, then
   there exists a constant `c` such that

   .. math::

      \int_a^b (u(x)-\mathcal{I}_{h}u(x))^2 \, dx
      \leq ch^4 \int_a^b u''(x)^2 \, dx,

   where `\mathcal{I}_h` is the global nodal interpolator to the P1
   finite element space.

.. proof:exercise::
   
   Under the same assumptions as the previous exercise, prove the following
   finite element version of Sobolev's inequality,

   .. math::

      \|v\|^2_{C^\infty} \leq C\int_0^1 (v')^2 \, dx,

   for all `v \in V \cap C^1([0,1])`, where `V` is the
   subspace of the P1 finite element space defined on a subdivision
   of the interval `[0,1]` containing only functions `v` with `v(0)=0`.
    
Now we will use the Taylor polynomial estimates to
derive error estimates for the local interpolation operator.
We start by looking at a triangle with diameter 1, and then use
a scaling argument to obtain error estimates in terms of the diameter
`h`. It begins by getting the following bound.

.. _Ibound:

.. proof:lemma::

   Let `(K_1,\mathcal{P},\mathcal{N})` be a finite element such that
   `K_1` is a triangle with diameter 1, and such that the nodal
   variables in `\mathcal{N}` involve only evaluations of functions or
   evaluations of derivatives of degree `\leq l`, and
   `\|N_i\|_{C^{l,\infty}(K_1)'} <\infty`, 

   .. math::

      \|N_i\|_{C^{l,\infty}(K_1)'} = \sup_{\|u\|_{C^{l,\infty}(K_1)}>0}
      \frac{|N_i(u)|}{\|u\|_{C^{l,\infty}(K_1)}} \qquad \qquad
      (\mbox{Dual norm of }N_i)

   Let `k-l > n/2`, and `u\in C^{k,\infty}(\Omega)`.
   Then

   .. math::

      \|\mathcal{I}_{K_1}u\|_{H^k(K_1)} \leq C\|u\|_{H^k(K_1)}.

.. proof:proof::
   
   Let `\{\phi_i\}_{i=1}^n` be the nodal basis for `\mathcal{P}`. Then
   
   .. math::
      
      \| \mathcal{I}_{K_1}u\|_{H^k(K_1)} &\leq \sum_{i=1}^k \|\phi_i\|_{H^k(K_1)}|N_i(u)|
      
      &\leq \underbrace{\sum_{i=1}^k \|\phi_i\|_{H^k(K_1)}\|N_i\|_{C^{l,\infty}(K_1)'}}_{C_0}\|u\|_{C^{l,\infty}(K_1)},
      
      &\leq C \|u\|_{H^k(K_1)},

   where the Sobolev inequality was used in the last line.
   
.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490672190"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=7eecb6d2-3a85-4a5a-b748-ac8f00addb0d>`_
    
Now we can directly apply this to the interpolation operator error
estimate on the triangle with diameter 1. It is the standard trick of
adding and subtracting something, in this case the Taylor polynomial.

.. _IerrK1:

.. proof:lemma::
   
   Let `(K_1,\mathcal{P},\mathcal{N})` be a finite element such that
   `K_1` has diameter `1`, and such that the nodal variables in
   `\mathcal{N}` involve only evaluations of functions or evaluations
   of derivatives of degree `\leq l`, and `\mathcal{P}` contain all
   polynomials of degree `k` and below, with `k>l+n/2`. Let `u\in
   C^{k+1,\infty}(K_1)`. Then for `i \leq k`, the
   local interpolation operator satisfies

   .. math::

      |\mathcal{I}_{K_1}u-u|_{H^i(K_1)} \leq C_1|u|_{H^{k+1}(K_1)}.

.. proof:proof::

   .. math::

      |\mathcal{I}_{K_1}u-u|_{H^i(K_1)}^2 &\leq \|\mathcal{I}_{K_1}u-u\|_{H^k(K_1)}^2
      
      &=
      \|\mathcal{I}_{K_1}u-Q_{k,B}u + Q_{k,B}u - u\|_{H^k(K_1)}^2
      
      &\leq \|Q_{k,B}u-u\|_{H^k(K_1)}^2 + \|\mathcal{I}(u-Q_{k,B}u)\|_{H^k(K_1)}^2,
 
      &\leq \|Q_{k,B}u-u\|_{H^k(K_1)}^2 + C^2\|Q_{k,B}u-u\|_{H^k(K_1)}^2,
      
      &\leq (1+C^2)|u|_{H^{k+1}(K_1)}^2,

   where we used the fact that `\mathcal{I}_{K_1}Q_{k,B}u = Q_{k,B}u` in the
   second line and the previous lemma in the third line.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490671682"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

..
  End of week 6 material
	    
    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=0269bbf5-8928-453a-83c7-ac8f00ad2f1a>`_
   
Now we apply a scaling argument to translate this to triangles
with diameter `h`.

.. _scaling:

.. proof:lemma:: 

   Let `(K,\mathcal{P},\mathcal{N})` be a finite element such that
   `K` has diameter `d`, and such that the nodal variables in
   `\mathcal{N}` involve only evaluations of functions or evaluations of
   derivatives of degree `\leq l`, and `\mathcal{P}` contains all
   polynomials of degree `k` and below, with `k>l+n/2`.
   Let `u\in
   C^{k+1,\infty}(K_1)`.
   Then for `i \leq k`, the local interpolation operator
   satisfies

   .. math::

      |\mathcal{I}_{K}u-u|_{H^i(K)} \leq C_Kd^{k+1-i}|u|_{H^{k+1}(K)}.

   where `C_K` is a constant that depends on the shape of `K` but not
   the diameter.

.. proof:proof::
   
   Consider the change of variables `x \to \phi(x)=x/d`. This map takes
   `K` to `K_1` with diameter 1. Then

   .. math::

      \int_K |D^\beta(I_Ku-u)|^2 \, d x  &= d^{-2|\beta|+1}\int_{K_1}|D^\beta(I_{K_1}
      u\circ \phi - u\circ \phi)|^2 \, d x,
      
      &\leq C_1^2d^{-2|\beta+1}\sum_{|\alpha|=k+1}\int_{K_1} |D^\alpha u\circ \phi|^2\, d x, 

      &\leq C_1^2d^{-2|\beta+2(k+1)}\sum_{|\alpha|=k+1}\int_{K} |D^\alpha u|^2
      \, d x,
      
      &= C_1^2d^{2(-|\beta| + k + 1)}|u|^2_{H^{k+1}(K)},

   and taking the square root gives the result.

.. dropdown:: A video recording of the following material is available here.
		  
    .. container:: vimeo

        .. raw:: html

            <iframe src="https://player.vimeo.com/video/490671577"
            frameborder="0" allow="autoplay; fullscreen"
            allowfullscreen></iframe>

    Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c1e7b2ce-4169-4fd7-a730-ac8f00b06e45>`_
   
So far we have just developed an error estimate for the local
interpolator on a single triangle. Now we extend this to finite element
spaces defined on the whole triangulation.

.. _Iherr:

.. proof:theorem::

   Let `\mathcal{T}` be a triangulation of `\Omega` with finite
   elements `(K_i,\mathcal{P}_i,\mathcal{N}_i)`, such that the minimum
   aspect ratio `\gamma` of the triangles `K_i` satisfies `\gamma>0`,
   and such that the nodal variables in `\mathcal{N}` involve only
   evaluations of functions or evaluations of derivatives of degree
   `\leq l`, and `\mathcal{P}` contains all polynomials of degree `k`
   and below, with `k>l+n/2`.  Let `u\in C^{k+1,\infty}(K_1)`.  Let
   `h` be the maximum over all of the triangle diameters, with `0\leq
   h<1`. Then for `i\leq k`, the global interpolation operator
   satisfies

   .. math::

      \|\mathcal{I}_{h}u-u\|_{H^i(\Omega)} \leq Ch^{k+1-i}|u|_{H^{k+1}(\Omega)}.

   (Recalling that we use the "broken" finite element derivative in norms
   for `\mathcal{I}_hu` over `\Omega`.
      
.. proof:proof::
   
   .. math::
      
      \|\mathcal{I}_{h}u-u\|_{H^i(\Omega)}^2 &=
      \sum_{K\in\mathcal{T}}\|\mathcal{I}_{K}u-u\|_{H^i(K)}^2,
      
      &\leq \sum_{K\in\mathcal{T}}C_Kd_K^{2(k+1-i)}|u|_{H^{k+1}(K)}^2,
      
      &\leq C_{\max}h^{2(k+1-i)}\sum_{K\in\mathcal{T}}|u|_{H^{k+1}(K)}^2,
      
      &= C_{\max}h^{2(k+1-i)}|u|_{H^{k+1}(\Omega)}^2,

   where the existence of the `C_{\max}=\max_KC_K<\infty` is due to the
   lower bound in the aspect ratio.
   
In this section, we have built a theoretical toolbox for the
interpolation of functions to finite element spaces. In the
next section, we move on to studying the solveability of finite
element approximations.
