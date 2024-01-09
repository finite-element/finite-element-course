.. default-role:: math

.. _poisson:

Revisiting the Poisson problem
==============================

As well as being an independent field of academic study, the finite
element method plays an important supporting role for solving boundary value
problems in the context of scientific enquiry and engineering design. 

It is therefore important to recognise that most users (scientists,
mathematicians, engineers etc.) of finite element methods are not hugely
interested in the underlying mathematics or implementation, but in actually
solving their own problems!

Since its inception in the 1960s specialists in finite elements have written an
almost uncountable number of software packages for solving finite element
problems. A small number of these have gone to underpin the now multi-billion
dollar engineering design and analysis software sector. Packages such as
ABAQUS, COMSOL Multiphysics and ADINA are now used everyday by hundreds of
thousands of engineers and scientists across the globe. 

These software packages offer an end-to-end finite element analysis, including
computer-aided design tools, advanced mesh creation capabilities, finite
element solution, post-processing and visualisation. Their focus is primarily
on ease-of-use and robustness. They can solve a pre-defined set of PDEs that
the user can select from, for example the heat equation, or linear elasticity.
Customising the PDE and its discretisation usually requires writing a 'user
element' in a low-level language like C or FORTRAN. Users have little control
or insight into the precise solution algorithms used, and cannot easily move
beyond the capabilities that are provided. Most are closed-source, meaning that
users cannot access or modify the underlying source code. Users with highly
specific and uncommon problems usually still need to 'code their own', as we
did in the implementation exercise.

In the last decade a new kind of finite element software relying on automatic
code generation techniques has emerged. This type of software is aimed at
engineers, academics and scientists who need to go beyond what fixed
functionality software described above can provide. Two examples are the FEniCS
Project and Firedrake that are written and maintained by groups of academics
and engineers worldwide, including the authors of these notes.

Although these two packages differ in the details, they share the following key
points:

.. list:
   * That the variational formulation of a finite element problem can be
     written in a high-level programming language that closely resembles
     mathematics as it is on written on the page.
   * That this high-level representation of a finite element problem can be
     automatically translated into highly performant computer code that can run
     on a variety of computer platforms, from laptops to high-performance
     computers.
   * That this way of implementing finite element solvers is not only flexible,
     fast and less error-prone than writing your own from scratch, but can
     actually be quite fun!

To make a link with what you have already learned in the previous part of the
course, we will begin by solving the Poisson problem in either FEniCSx or
Firedrake, depending on the preferences of your instructor. Please click on the
appropriate link below to access the Python Jupyter Notebook in the Google Colab
environment:

`Poisson in DOLFINx
<https://githubtocolab.com/jhale/finite-element-course/blob/jhale/unilu-course/doc/source/notebooks/dolfinx/poisson.ipynb>`__
