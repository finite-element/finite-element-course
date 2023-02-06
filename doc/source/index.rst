.. only:: latex

   ============================================
   Numerical Methods for Variational problems
   ============================================

   .. raw:: latex

      \frontmatter
      \mainmatter
      \part{Numerical analysis}

.. only:: latex

    .. toctree::
        :numbered:
        :maxdepth: 2

        L1_introduction
        L2_fespaces
        L3_interpolation
        L4_feprobs
        L5_convergence
	L6_stokes

.. only:: html

   This is the webpage for the `University of Luxembourg Master in Mathematics
   <https://wwwen.uni.lu/studies/fstm/master_in_mathematics/programme2>`__  course
   Numerical Methods for Variational Problems.

   This webpage is adapted with permission from the `original
   <https://finite-element.github.io>`__ authored by Prof. Colin
   Cotter and Dr. David Ham at Imperial College London. The section on Modern
   Finite Element practice was authored by Dr. Jack S. Hale at the University
   of Luxembourg.

   The authors welcome feedback and would particularly
   appreciate an `email <mailto:david.ham@imperial.ac.uk>`__ if this
   material is used to teach anywhere.

   .. toctree::

      practicalities

   Weekly material
   ---------------

   The numerical analysis and implementation parts of the module run in
   parallel. The modern practice part of the module will take place after the
   numerical analysis and implementation parts. Each part has videos and
   exercises embedded in its notes. This table indicates the progress that you
   should make through each component each week.

   .. list-table::
        :widths: 10 45 45
        :header-rows: 1

        *   - Week
            - Numerical analysis
            - Implementation
        *   - 1
            - Up to and including :numref:`Exercise
              {number}<def-robin>`.
            - Do the background tutorials and installation work given under
              :doc:`tools` and :doc:`implementation`.
        *   - 3
            - Up to and including :numref:`Exercise
              {number}<exe-1d-lagrange-basis>`.
            - Up to the end of :numref:`quadrature`.
        *   - 5
            - Up to and including :numref:`Definition {number}<P1unisolve>`.
            - Up to and including :numref:`Exercise {number}<ex-vandermonde>`.
        *   - 7
            - Up to and including :numref:`Exercise {number}<exer-argyris>`.
            - Up to and including :numref:`Exercise {number}<ex-tabulate>`.
        *   - 9
            - Up to and including :numref:`Definition
              {number}<def-averaged-taylor>`.
            - Up to the end of :numref:`secfinitelement`.
        *   - 11
            - Up to and including :numref:`Lemma {number}<IerrK1>`.
            - Up to and including :numref:`Exercise {number}<ex-local>`.
        *   - 13
            - Up to and including :numref:`Exercise {number}<exe-pure-neumann>`.
            - Up to the end of :numref:`secfunctionspaces`.
        *   - 15
            - Up to the end of :numref:`fe_problems`.
            - Up to the end of :numref:`secfunctions`.
        *   - 16
            - Up to and including :numref:`Theorem {number}<thm-cea>`.
            - Up to the end of :numref:`secdirichlet`.
        *   - 16
            - Up to the end of :numref:`convergence`.
            - Time for the mastery exercise, (catch up time for year 3).

   .. image:: _static/brenner_scott.png
      :align: right
      :width: 20ex

   A PDF version of the course notes is `available here
   <Finiteelementcourse.pdf>`_.

   Part 1: Numerical analysis
   --------------------------
   
   The material is presented by means of a set of lecture notes, with lecture
   videos interspersed in the notes. 

   The text for this part of the module is Brenner and Scott *The
   Mathematical Theory of Finite Element Methods*. The University of Luxembourg has
   paid for PDF access to this book, so it is accessible from
   the University of Luxembourg network at `Springer Link
   <http://link.springer.com/book/10.1007%2F978-0-387-75934-0>`__.

   However, this course has the material rearranged to synchronise the
   content better between the lecture notes and the implementation
   exercise.
   
   Lecture notes:
   ~~~~~~~~~~~~~~

    .. toctree::
        :numbered:
        :maxdepth: 2

        L1_introduction
        L2_fespaces
        L3_interpolation
        L4_feprobs
        L5_convergence
	L6_stokes

   Past exam papers
   ~~~~~~~~~~~~~~~~
   Past examination papers from the Imperial College London course are available here:

   * `2015 exam paper <_static/FE2015-exam-revised.pdf>`__ and `solutions <_static/FE2015-exam-soln.pdf>`__
   * `2016 exam paper <_static/FE2016-exam.pdf>`__ and `solutions <_static/FE2016-exam-soln.pdf>`__
   * `2017 exam paper <_static/FEExam-2017.pdf>`__ and `solutions <_static/FEExam-2017-soln.pdf>`__
   * `2018 exam paper <_static/FEExam-2018.pdf>`__ and `solutions <_static/FEExam-2018-soln.pdf>`__
   * `2019 exam paper <_static/FEExam-2019.pdf>`__ and `solutions <_static/FEExam-2019-solns.pdf>`__
   * `revision checklist <_static/revision-checklist.pdf>`__
   * `2020 exam paper <_static/FEExam-2020.pdf>`__ and `solutions <_static/FEExam-2020-solns.pdf>`__
   * `2021 exam paper <_static/FEExam-2021.pdf>`__ and `solutions <_static/FEExam-2021-solns.pdf>`__
   * `revision checklist  <_static/revision-checklist.pdf>`__
   
   The examination at the University of Luxembourg will be adapted to the
   specific needs of the students attending the course.

.. only:: html

    Part 2: Implementation
    ----------------------

    The implementation part of the module aims to give the students a
    deeper understanding of the finite element method through writing
    software to solve finite element problems in one and two dimensions.

    The key to this part of the
    module is to build up a working finite element implementation over the course
    of the term, and thereby to gain a practical understanding of the method.

    The starting point for the implementation method is the skeleton code, an
    outline of a simple finite element library written in Python. Many of the
    critical algorithms in the skeleton code are left unimplemented, it will be
    your task to implement them over the course of the term.

    Each chapter of the implementation describes how a part of the finite element
    method is implemented. Along the way are videos which explain the text, or
    walk through the algorithms presented. Also interspersed in the text are
    exercises, typically requiring you to implement the algorithm just
    presented. We will look at how to do this in more detail presently.



    .. toctree::
        :maxdepth: 3

        tools
        implementation

    Implementation exercise contents:

.. raw:: latex
         
   \part{Implementation Exercise}
   \setcounter{chapter}{-1}

.. only:: latex

   .. include:: implementation.rst

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
   9_mixed_problems
   zbibliography

.. only:: html

   Part 3: Modern practice
   -----------------------

   The modern practice part of the module will close the gap between the
   theoretical and implementation aspects of the finite element method outlined
   in parts 1 and 2, and the finite element method as an active topic of
   research and a key tool of modern scientific and engineering investigation.

   The starting point will be a gentle introduction to the open source DOLFINx
   or Firedrake software systems for the automatic solution of PDEs using the
   finite element method.

   This section of the course will be shown as Python Jupyter Notebooks run on
   the Google Colab cloud computing environment. A Google account is required.

.. toctree::
   :numbered
   :maxdepth: 2

   P1_poisson
