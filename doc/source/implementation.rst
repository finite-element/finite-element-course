The implementation exercise
===========================

The object of the implementation exercise is to gain an understanding
of the finite element method by producing a working one and two
dimensional finite element solver library. Along the way you will have
the opportunity to pick up valuable scientific computing skills in
coding, software engineering and rigorous testing.

This part of the module is very practical, and there are never conventional
lectures for it, even when everything is taught on campus. Each week you should
work through the notes and videos until you come to an exercise. Each exercise
will invite you to implement another part of a finite element implementation, so
that by the end of the term we will be solving finite element problems.

Along the way, there will be the opportunity to get help and feedback through
the module Piazza board, weekly online labs, and through pull requests for
feedback in weeks 4 and 7. 

Formalities and marking scheme
------------------------------

The implementation exercise is due at 1300 on Monday 20 March 2023. Submission
is via GitHub: the last commit pushed to GitHub and dated before the deadline
will be marked.

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

Code execution performance is not a primary concern of this module, however the
code must still be algorithmically correct. This means not just returning the
correct answer but also having the correct algorithmic complexity. Occasionally
students submit code that uses quadratic algorithms where linear ones would be
possible. The result is that examples that should run in seconds and take
megabytes of memory instead take gigabytes of memory and many hours to complete.
Such submissions are incorrect, and will be marked as such.

Extension (mastery) exercise
----------------------------

Fourth year and masters students must also complete the mastery
exercise, which is :numref:`mixed` This will be
worth 20% of the implementation exercise marks and will be marked on
the same scheme as above.   

Obtaining the skeleton code
---------------------------

.. only:: html

    .. dropdown:: A video recording of the following material is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495157536"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c92e73b4-b383-4412-b5f9-ac9f00b08789>`_

This section assumes you've already done everything to :doc:`set up the software
tools you need <tools>`.

Set up a folder to hold the repository and virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can call this folder anything you like, and store it anywhere that suits
you, though don't move it once you've created it as this will break the virtual
environment. Suppose you would like to keep the new folder in a folder called
:file:`docs` in your home directory. We first :doc:`open a
terminal<fons:terminal>` and switch to the folder:

.. code-block:: console

    $ cd docs

Note that `$` is the command prompt (which might be a different character such
as `%` or `>` for you). You don't type the prompt. Start with `cd`. Next we
create the folder we'll use for this course. Suppose we choose to call it
:file:`finite-element`, then we would type:

.. code-block:: console

    $ mkdir finite-element

`mkdir` stands for "make directory". *Directory* is an alternative term to
*folder*. Finally we switch ("change directory") into that folder:

.. code-block:: console

    $ cd finite-element

Setting up your venv
~~~~~~~~~~~~~~~~~~~~

We're going to use a Python venv. This is a private Python environment
in which we'll install the packages we need, including our own
implementation exercise. This minimises interference between this
project and anything else which might be using Python on the
system. With your current working folder set to the course folder, run:

.. code-block:: console

    $ python3 -m venv fe_venv

If your Python interpreter has a different name (e.g. `python3.11` or `py`)
then you type that instead.

Activating your venv
~~~~~~~~~~~~~~~~~~~~

**Every time** you want to work on the implementation exercise, you need
to activate the venv. On Linux or Mac do this with:

.. code-block:: console

    $ source fe_venv/bin/activate

while on Windows the command is:

.. code-block:: console

    > source fe_venv/Scripts/activate

Obviously if you are typing this in a directory other than the one
containing the venv, you need to modify the path accordingly.

Setting up your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~

We're using a tool called `GitHub classroom <https://classroom.github.com>`_ to automate the creation of your
copies of the repository. To create your repository, `click here <https://classroom.github.com/a/ZEeJSgi5>`_.

Cloning a local copy
~~~~~~~~~~~~~~~~~~~~

At the command line on your working machine type:

.. code-block:: console

    $ git clone <url> finite-element-course

Substituting your git repository url for <url>. Your git repository
url can be found by clicking on `clone or download` at the top right of your repository page on GitHub. 

Installing the course Python package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your git repository contains a Python package. Installing this will cause the
other Python packages on which it depends to be installed into your venv, and
will create various visualisation scripts you'll need later in the module. Run:

.. code-block:: console

    $ python -m pip install -e finite-element-course/


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
than large ones. 

Testing your work
-----------------

As you complete the exercises, there will often be test scripts which
exercise the code you have just written. These are located in the
``test`` directory and employ the `pytest <http://pytest.org/>`_
testing framework. You run the tests with:

.. code-block:: console

    $ py.test test_script.py

from the bash command line, replacing ``test_script.py`` with the appropriate
test file name. The ``-x`` option to ``py.test`` will cause the test
to stop at the first failure it finds, which is often the best place
to start fixing a problem. For those familiar with debuggers, the
``--pdb`` option will drop you into the Python debugger at the first
error.

You can also run all the tests by running ``py.test`` on the tests
directory. This works particularly well with the -x option, resulting
in the tests being run in course order and stopping at the first
failing test:

.. code-block:: console

    $ py.test -x tests/

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

Getting help
------------

It's expected that you will find there are tasks in the implementation exercise
that you don't know how to do. Your first port of call should be the Ed
forum, followed by the weekly live lab sessions.

Using Ed
~~~~~~~~

The key advantage of asking for help on Ed is that you can do this at any
point during the week, whenever you are stuck. The whole class can see the forum,
but you can choose to publish anonymously so nobody need know who asked the
question. You should also watch the other questions as they appear on Ed,
because you will find that you learn a lot from what other people ask, as well
as the answers they get. Other students might notice issues that didn't even
occur to you! 

Do please try to answer other students' questions. Doing so
is actually a really effective way of understanding the work better, since you
will be looking at the tasks from another student's perspective.

Formulating a good question
~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the key skills in getting help with code is to ask the question in a
structured way which provides all the information required by the person helping
you. Not only does this radically increase the chances of getting a useful
response first time, but often the process of thinking through how to ask the
question leads you to its solution before you even ask. Please review the
information from the second year Principles of Programming :ref:`instructions on
raising an issue <pop:issue-report>`.

.. note::

    Please don't post large pieces of code to Piazza. Just post minimal examples
    if they help. However always commit and push your work, and post the
    :ref:`git commit hash <fons:git-hash>` in the repository. The lecturer can
    always find your work from the git hash, so long as you've pushed to GitHub.

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
