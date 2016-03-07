The implementation exercise
===========================

The object of the implementation exercise is to gain an understanding
of the finite element method by producing a working one and two
dimensional finite element solver library. Along the way you will have
the opportunity to pick up valuable scientific computing skills in
coding, software engineering and rigorous testing.

There will be no conventional lectures for this part of the
module. Instead, there will be eigteen 1 hour computer lab sessions
during the term. Some of this time will involve explanations at the
board, but much of the time will be an opportunity to develop your
finite element implementation and receive help on how to do so.

Formalities and marking scheme
------------------------------

The implementation exercise is due at the end of term. That is, by
1700 on Wednesday 23 March. You must submit your work by emailing the
lecturer the git commit code for the version of the code you would
like marked. You can convenently find this code on the commits page
for your repository on bitbucket. For the avoidance of doubt, the
commit you submit must date from before the deadline!

The marking scheme will be as follows:

High first (80-100)
  As for bare first, but additionally the extension (mastery)
  component of the implementaton exercise has been completed correctly
  and clearly.
Bare first (75-80)  
  All parts of the implementation are correct and all tests pass. The
  code style is always very clear and the implementation of every
  exercise is transparent and elegant.
Upper second (60-75)
  The implementation is correct but let down somewhat by poor coding
  style. Alternatively, submissions which are correct and well
  written up to and including solving the Helmholtz problem but
  which do not include a correct solution to boundary conditions will
  earn an upper second.
Lower second (45-60)
  Most of the exercise is correctly implemented, but there are some
  test failures, or there are significant failures in coding style or
  in the transparency and elegance of solutions.
Third (30-45)
  There are significant failings in the implementation resulting in
  many test failures, and/or the coding style and elegance are
  sufficiently poor that the code is hard to understand.
Fail (0-30)
  The implementation is substantially incomplete. Correct
  implementations may have been provided for some of the earlier exercises but
  the more advanced parts of the implementation exercise have not been
  attempted or do not work.

Extension (mastery) exercise
----------------------------

Completing the core implementation exercise will result in (at most) a
mark of 80% for the implementation part of the module. The remaining
20% will be allocated to an extension exercise which will be issued in
the middle of the term. This is intended to enable the students who
are doing best in the module to demonstrate their mastery of the
material by implementing work which goes beyond the main body of work.
  

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

  git clone <url>

Substituting your git repository url for <url>. Your git repository
url is at the top right of your repository page on Bitbucket. Next::

  cd finite_element_course
  git checkout implementation

Your working directory is now a current checkout of your
implementation branch.

Pointing Python at the code on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


By far the easiest way to have your Python find the code is to ensure
your working directory is the right one. Type the following at the
Python command line::

  cd h:\finite_element_course


Pointing Python at the code on OS X or Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You'll need Python to be able to find the ``fe_utils`` package from
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
<https://bitbucket.org/finiteelement/finite_element_course>`_. On the
top right there is an eye icon. Select the drop-down box and ensure
that ``All issues`` and ``all commits`` are selected.

Updating your fork
~~~~~~~~~~~~~~~~~~

When you see that the main repository has been updated, you'll need to
update your fork to incorporate those changes. It is possible to do
this using git commands on the command line, but there is a more
simple graphical way to do it:

#. Make sure you have commited all your local changes **and** pushed
   them to bitbucket.
#. Navigate to the bitbucket overview page for your repository. If
   there are changes to the main repository which are not yet in your
   fork, there will be a blue box on the right saying ``This fork is n
   commits behind finiteelement/finite_element_course.`` You should
   click on ``Sync now.``
#. A window will appear confirming that you want to sync the
   repositories. Click ``Sync``.
#. Click on the branches icon: |git-branch|. Move your mouse over the
   ``implementation`` row and an elipsis (...) will appear on the
   right. Click on the elipsis and select ``Sync branch`` from the
   menu that appears.
#. A window will appear confirming that you want to sync the
   branches. Click ``Sync``.
#. Update your local copy of the repository by typing ``git pull``.

Skeleton code documentation
---------------------------

There is web documentation for the complete :doc:`fe_utils`. There is
also an :ref:`alphabetical index <genindex>` and a :ref:`search page<search>`.

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

As you do the exercises, **commit your code** to your repository. This
will build up your finite element library. You should commit code
early and often - small commits are easier to understand and debug
than large ones. **Never** commit back to the ``master`` branch of your
fork, that should always remain a clean copy of the main repository.

Pull requests for feedback
--------------------------

There will be a formal opportunity to recieve feedback on your code
progress every two weeks. To take part, you should set up a pull
request from your ``implementation`` branch to the ``master`` branch
of your repository. This will enable the lecturer to write line by
line comments on your code. Make sure the pull request is against the
``master`` branch of your private fork - if you pull request against
the main repository then the whole class will be able to plagiarise
your work and laugh at your mistakes!

Creating your pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Click on the pull request icon |pullrequest| on the left of your
   fork's bitbucket page. 
#. On the top right of the pull requests screen click on ``Create pull
   request``.
#. Change the **left** dropdown box to ``implementation``.
#. Change the **top right** dropdown box to list your fork instead of
   the main repository. Leave the bottom right box set to ``master``.
#. Type a suitable title in the title box. For example 
   ``Request for feedback 30/1/15``.
#. If you have any comments you would like to pass on to the lecturer
   (for example questions about how you should have done a particular
   exercise) then type these in the ``Description`` box.
#. Click ``Create pull request``.


Testing your work
-----------------

As you complete the exercises, there will often be test scripts which
exercise the code you have just written. These are located in the
``test`` directory and employ the `pytest <http://pytest.org/>`_
testing framework. You run the tests with:: 

   py.test test_script.py

on the Bash command line or::

   !py.test test/test_script.py

from within Python, replacing ``test_script.py`` with the appropriate
test file name. The ``-x`` option to ``py.test`` will cause the test
to stop at the first failure it finds, which is often the best place
to start fixing a problem. For those familiar with debuggers, the
``--pdb`` option will drop you into the Python debugger at the first
error.


Coding style and commenting
---------------------------

Computer code is not just functional, it also conveys information to
the reader. It is important to write clear, intelligible code. **The
readability and clarity of your code will count for marks**.

The Python community has agreed standards for coding, which are
documented in `PEP8
<https://www.python.org/dev/peps/pep-0008/>`_. There are programs and
editor modes which can help you with this. The skeleton implementation
follows PEP8 quite closely. You are encouraged, especially if you are
a more experienced programmer, to follow PEP8 in your
implementation. However nobody is going to lose marks for PEP8
failures.

Tips and tricks for the implementation exercise
-----------------------------------------------

Work from the documentation.
   The notes, and particularly the exercise specifications, contain
   important information about how and what to implement. If you just
   read the source code then you will miss out on important
   information.
Read the hints
   The pink sections in the notes starting with a lightbulb are
   hints. Usually they contain suggestions about how to go about
   writing your answer, or suggest Python functions which you might
   find useful.
Don't forget the 1D case
   Your finite element library needs to work in one and two dimensions.
Return a :class:`numpy.array`
   Many of the functions you have to write return arrays. Make sure
   you actually return an array and not a list (it's usually fine to
   build the answer as a list, but convert it to an array before you
   return it).

.. |git-branch| image:: git-branch.*
   :height: 20px
   :width: 3ex

.. |pullrequest| image:: _static/pullrequest.png
   :height: 20px
   :width: 3ex
