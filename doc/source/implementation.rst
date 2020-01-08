The implementation exercise
===========================

The object of the implementation exercise is to gain an understanding
of the finite element method by producing a working one and two
dimensional finite element solver library. Along the way you will have
the opportunity to pick up valuable scientific computing skills in
coding, software engineering and rigorous testing.

There will be no conventional lectures for this part of the
module. Instead, there will be twice weekly 1 hour computer lab sessions
during the term. Some of this time will involve explanations at the
board, but much of the time will be an opportunity to develop your
finite element implementation and receive help on how to do so.

Formalities and marking scheme
------------------------------

The implementation exercise is due at the end of term. That is, by
1600 on Friday 22 March. You must submit your work uploading the git
commit code on Blackboard. You can convenently find this code on the
commits page for your repository on github. For the avoidance of
doubt, the commit you submit must date from before the deadline!

The marking scheme will be as follows:

First/distinction (70-100)  
  All parts of the implementation are correct and all tests pass. The
  code style is always very clear and the implementation of every
  exercise is transparent and elegant.
Upper second/merit (60-70)
  The implementation is correct but let down somewhat by poor coding
  style. Alternatively, submissions which are correct and well
  written up to and including solving the Helmholtz problem but
  which do not include a correct solution to boundary conditions will
  earn an upper second.
Lower second/pass (50-60)
  There are significant failings in the implementation resulting in
  many test failures, and/or the coding style is
  sufficiently poor that the code is hard to understand.
Fail (0-50)
  The implementation is substantially incomplete. Correct
  implementations may have been provided for some of the earlier exercises but
  the more advanced parts of the implementation exercise have not been
  attempted or do not work.

Extension (mastery) exercise
----------------------------

Fourth year and masters students must also complete the mastery
exercise, which will be issued half way through the term. This will be
worth 20% of the implementation exercise marks and will be marked on
the same scheme as above.   

Obtaining the skeleton code
---------------------------

This section assumes you've already done the :ref:`Git tutorial <bitbucket-git>`.

Setting up your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~

We're using a tool called `GitHub classroom <https://classroom.github.com>`_ to automate the creation of your
copies of the repository. To create your repository, `click here <https://classroom.github.com/a/yIPAQZ6_>`_.


Cloning a local copy
~~~~~~~~~~~~~~~~~~~~

At the command line on your working machine type::

  git clone <url> finite-element-course

Substituting your git repository url for <url>. Your git repository
url can be found by clicking on `clone or download` at the top right of your repository page on GitHub. 

Setting up your venv
~~~~~~~~~~~~~~~~~~~~

We're going to use a Python venv. This is a private Python environment
in which we'll install the packages we need, including our own
implementation exercise. This minimises interference between this
project and anything else which might be using Python on the
system. We can run a script from the git repository to make the venv::

  ./finite-element-course/scripts/fe_install_venv venv

This has to install several packages in the venv, so it might take a
few minutes to run.

On Windows, the set of commands is somewhat different. In this case
you would run::

  ./finite-element-course/scripts/fe_install_venv_win venv

Activating your venv
~~~~~~~~~~~~~~~~~~~~

**Every time** you want to work on the implementation exercise, you need
to activate the venv. On Linux or Mac do this with::

  source venv/bin/activate

while on Windows the command is::

  source venv/Scripts/activate

Obviously if you are typing this in a directory other than the one
containing the venv, you need to modify the path accordingly.

Setting up an implementation branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We'll keep the master branch of your repository in the original
condition so we can compare to it later, and collect any updates which
occur during the term. Instead, we'll create an implementation branch
to actually work on::

  cd finite-element-course
  git checkout -b implementation

Your working directory is now a current checkout of your
implementation branch. You'll also want to push this branch to GitHub::

  git push --set-upstream origin implementation

Watching for updates and issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should make sure you are notified of all updates on the main
repository and all issues anyone raises. For this, you should navigate
to `the main repository
<https://github.com/finite-element/finite-element-course>`_. On the
top right there is an eye icon. Select the drop-down box and switch to
``watching``.

Updating your fork
~~~~~~~~~~~~~~~~~~

When you see that the main repository has been updated, you'll need to
update your repository to incorporate those changes. *Just this once*,
you need to tell your local git repo about the main repository::

  git remote add upstream https://github.com/finite-element/finite-element-course.git

Now, *every time* you want to update you do the following:
  
#. Make sure you have commited all your local changes **and** pushed
   them to GitHub.
#. Execute the following commands::
   
     git checkout master          # Switch to the master branch.
     git pull upstream master     # Update from the main repository.
     git push                     # Push the updated master branch to GitHub.
     git checkout implementation  # Switch back to the implementation branch.
     git merge master             # Merge the new changes from master into implementation.
     git push                     # Push the updated implementation branch to GitHub.
   
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

.. hint::

   A video about creating pull requests is available `here <https://www.youtube.com/embed/JPCG-kcfQHE>`_


There will be a formal opportunity to recieve feedback on your code
progress twice during the term. To take part, you should set up a pull
request from your ``implementation`` branch to the ``master`` branch
of your repository. This will enable the lecturer to write line by
line comments on your code. 

Creating your pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Click on the ``New pull request`` button at the top of your
   repository page on GitHub.
#. Make sure **left** dropdown box ("base") is set to ``master``.
#. Make sure **right** dropdown box ("compare") is set to ``implementation``.
#. Type a suitable title in the title box. For example 
   ``Request for feedback 30/1/19``.
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

from the bash command line, replacing ``test_script.py`` with the appropriate
test file name. The ``-x`` option to ``py.test`` will cause the test
to stop at the first failure it finds, which is often the best place
to start fixing a problem. For those familiar with debuggers, the
``--pdb`` option will drop you into the Python debugger at the first
error.

You can also run all the tests by running ``py.test`` on the tests
directory. This works particularly well with the -x option, resulting
in the tests being run in course order and stopping at the first
failing test::

  py.test -x tests/


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
Return a :func:`numpy.array`
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
