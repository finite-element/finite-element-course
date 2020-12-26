.. only:: latex

   ============================================
   Finite elements, analysis and implementation
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


.. only:: html

   This is the webpage for the `Imperial College London Mathematics
   <http://www.imperial.ac.uk/maths>`_  module
   MATH96063/MATH97017/MATH97095 Finite Elements: numerical analysis and
   implementation. There's an introductory video explaining what the module is about `online here <https://player.vimeo.com/video/426777950?autoplay=1>`_.

   Other people are welcome to make use of the
   material here. The authors welcome feedback and would particularly
   appreciate an `email <mailto:david.ham@imperial.ac.uk>`_ if this
   material is used to teach anywhere.

   .. toctree::

      practicalities

   .. image:: _static/brenner_scott.png
      :align: right
      :width: 20ex

   A PDF version of the course notes is `available here
   <Finiteelementcourse.pdf>`_.

   Part 1: Numerical analysis
   --------------------------

   The theory  part of
   the module will be led by `Prof. Colin Cotter
   <http://www.imperial.ac.uk/people/colin.cotter>`_. The material is presented
   by means of a set of lecture notes, with lecture videos interspersed in the
   notes. 

   The text for this part of the module is Brenner and Scott *The
   Mathematical Theory of Finite Element Methods*. Imperial College has
   fortunately paid for PDF access to this book, so it is accessible from
   the Imperial College network at `Springer Link
   <http://link.springer.com/book/10.1007%2F978-0-387-75934-0>`_.

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

   Weekly material
   ~~~~~~~~~~~~~~~

   The Spring Term weekly material for 2021 for this part of the course is as follows.

   #. Week 1: Up to and including :numref:`Definition {number}<def-discrete-poisson>`.
   #. Week 2: Up to and including :numref:`Exercise {number}<exe-1d-lagrange-basis>`.
   #. Week 3: Up to and including :numref:`Definition {number}<P1unisolve>`.
   #. Week 4: Up to and including :numref:`Exercise {number}<exer-argyris>`.
   #. Week 5: Up to and including :numref:`Definition {number}<def-averaged-taylor>`.
   #. Week 6: Up to and including :numref:`Lemma {number}<IerrK1>`.
   #. Week 7: Up to and including :numref:`Exercise {number}<exe-pure-neumann>`.
   #. Week 8: Up to the end of Section 4.
   #. Week 9: Up to and including :numref:`Theorem {number}<thm-cea>`.
   #. Week 10: Up to the end of Section 5.

   Past exam papers
   ~~~~~~~~~~~~~~~~
   Please note that for 2015-2018, there was no mastery component in the
   examination, and so there were four questions. From 2019 on there are
   four questions plus one mastery question for 4th year/Masters credits.
   
   * `2015 exam paper <_static/FE2015-exam-revised.pdf>`_ and `solutions <_static/FE2015-exam-soln.pdf>`_
   * `2016 exam paper <_static/FE2016-exam.pdf>`_ and `solutions <_static/FE2016-exam-soln.pdf>`_
   * `2017 exam paper <_static/FEExam-2017.pdf>`_ and `solutions <_static/FEExam-2017-soln.pdf>`_
   * `2018 exam paper <_static/FEExam-2018.pdf>`_ and `solutions <_static/FEExam-2018-soln.pdf>`_
   * `2019 exam paper <_static/FEExam-2019.pdf>`_ and `solutions <_static/FEExam-2019-solns.pdf>`_
   * `revision checklist <_static/revision-checklist.pdf>`_

.. only:: html

    Part 2: Implementation
    ----------------------

    The implementation part of the module aims to give the students a
    deeper understanding of the finite element method through writing
    software to solve finite element problems in one and two dimensions.

    This part of the module will be taught by `Dr David Ham
    <http://www.imperial.ac.uk/people/david.ham>`_. The key to this part of the
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
