.. only:: clatex

   ============================================
   Finite elements, analysis and implementation
   ============================================

   .. raw:: latex

      \frontmatter

   ===================================================
   M5MA47 Finite elements: analysis and implementation
   ===================================================

   .. include:: implementation.rst

.. only:: html

   This is the webpage for the `Imperial College London Mathematics
   <http://www.imperial.ac.uk/maths>`_ final year and masters module
   M4A47/M5A47 Finite Elements: numerical analysis and
   implementation. Other people are welcome to make use of the
   material here. The authors welcome feedback and would particularly
   appreciate an `email <mailto:david.ham@imperial.ac.uk>`_ if this
   material is used to teach anywhere.

   .. toctree::

      practicalities

   .. image:: _static/brenner_scott.png
      :align: right
      :width: 20ex

   Part 1: Numerical analysis
   --------------------------

   The theory part of the module will consist of two hours per week
   primarily composed of lectures, with occasional tutorials. This part of
   the module will be led by `Dr Colin Cotter
   <http://www.imperial.ac.uk/people/colin.cotter>`_.

   The text for this part of the module is Brenner and Scott *The
   Mathematical Theory of Finite Element Methods*. Imperial College has
   fortunately paid for PDF access to this book, so it is accessible from
   the Imperial College network at `Springer Link
   <http://link.springer.com/book/10.1007%2F978-0-387-75934-0>`_.

   Lecture slides:
   ~~~~~~~~~~~~~~~

   * `Lecture 1 <_static/Lecture1.pdf>`_
   * `Lecture 2 <_static/Lecture2.pdf>`_
   
   Exercises:
   ~~~~~~~~~~

   * `Exercise 1 <_static/FE_examples1.pdf>`_
     
   Past exam papers
   ~~~~~~~~~~~~~~~~

   * `2015 exam paper <_static/FE2015-exam-revised.pdf>`_ and `solutions <_static/FE2015-exam-soln.pdf>`_
   * `Mock exam paper <_static/FE_mock_paper.pdf>`_
   * `revision checklist <_static/revision-checklist.pdf>`_

   Part 2: Implementation
   ----------------------

   The implementation part of the module aims to give the students a
   deeper understanding of the finite element method through writing
   software to solve finite element problems in one and two dimensions.

   This part of the module will be taught by `Dr David Ham
   <http://www.imperial.ac.uk/people/david.ham>`_ in two hours per week
   of computer laboratory time.

.. only:: html

   .. toctree::
      :maxdepth: 3

      tools
      implementation

   Implementation exercise contents:


.. raw:: latex
         
   \mainmatter

.. toctree::
   :numbered:
   :maxdepth: 2

   1_quadrature
   2_finite_elements
   3_meshes
   4_function_spaces
   5_functions
   6_finite_element_problems
   7_boundary_conditions
   8_nonlinear_problems
   zbibliography
