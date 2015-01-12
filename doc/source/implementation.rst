The implementation exercise
===========================

The object of the implementation exercise is to gain an understanding
of the finite element method by producing a working one and two
dimensional finite element solver library. Along the way you will have
the opportunity to pick up valuable scientific computing skills in
coding, software engineering and rigorous testing.

There will be no conventional lectures for this part of the
module. Instead, there will be a two hour computer lab session every
week. Some of this time will involve explanations at the board, but
much of the time will be an opportunity to develop your finite element
implementation and receive help on how to do so.

Obtaining the skeleton code
---------------------------

This section assumes you've already done the :ref:`Bitbucket tutorial <bitbucket-git>`.

Setting up your Bitbucket fork
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You'll need your own fork of the finite element repository so that you
can add your implementation. First, `log in to bitbucket
<https://bitbucket.org/account/signin/>`_. Next you can `create a fork
of the repository
<https://bitbucket.org/finiteelement/finite_element_course/fork>`_.

 * **Select** ``This is a private repository`` (this prevents plagiarism)
 * **Unselect** ``Issue tracking`` (all issues should go to the main project)
 * Click ``Fork repository`` to create your own repository.
 * On the right, click on ``Send invitation`` and invite ``David_Ham``
   to your repository. This will ensure that the lecturer can see your
   work to provide help, feedback and marking.

Your new fork only has a master branch. You'll want to leave that
alone to collect any updates which happen on the main repository. You
will actually work on a branch, which we will call ``implementation``.

 * Click on the branch icon |git-branch| on the left.
 * Now click on ``create branch`` on the extreme right.
 * Enter ``implementation`` as the branch name.

Cloning a local copy
~~~~~~~~~~~~~~~~~~~~

At the command line on your working machine type::

  git clone git@bitbucket.org:<USERNAME>/finite_element_course.git

substituting your Bitbucket username for <USERNAME>. Next::

  cd finite_element_course
  git checkout implementation

Your working directory is now a current checkout of your
implementation branch.

Pointing Python at the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You'll need Python to be able to find the ``fe_utils`` module from
wherever it is running. To do this, you need to add your repository
directory to the ``PYTHONPATH`` environment variable. **In your
repository directory** type the following::

  cat >> ~/.bashrc << foo                                             
  export PYTHONPATH=\$PYTHONPATH:$PWD
  foo

The above line will update your ``PYTHONPATH`` every time you log
in. **Just this once** you need to update it for the current session::

  export PYTHONPATH=$PYTHONPATH:$PWD

Watching for updates and issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should make sure you are notified of all updates on the main
repository and all issues anyone raises. For this, you should navigate
to `the main repository
<https://bitbucket.org/finiteelement/finite_element_course>`. On the
top right there is an eye icon. Select the drop-down box and ensure
that ``All issues`` and ``all pull requests`` are selected.

How to do the implementation exercises
--------------------------------------

The implementation exercises build up a finite element library from
its component parts. Quite a lot of the coding infrastructure you will
need is provided already. Your task is to write the crucial
mathematical operations at key points. The mathematical operations
required are described on this website, interspersed with exercises
which require you to implement and test parts of the mathematics.

The code on which you will build is in the ``fe_utils`` directory of
your repository. The code has embedded documentation which is used to
build the :doc:`fe_utils` web documentation.


.. |git-branch| image:: git-branch.svg
   :height: 20px
