Software tools
==============

In order to do this module, you'll need some core software tools. As the module
proceeds we'll also install several more Python packages, but you don't need to
install those right now. The core tools you will need are:

    1. Python version 3.6 or later.
    2. Git (the revision control system we're going to use).
    3. A Python-aware text editor. Visual Studio Code is recommended, and all
       the instructions in this course will assume that this is what you are using.

The Faculty of Natural Sciences at Imperial has 
:doc:`centralised instructions for installing all of these tools <fons:index>`, and we'll follow those. 

Python 
......

Your implementation will be written in Python based on a code skeleton
provided. This means that you'll need a certain familiarity with the
Python language. But don't panic! Python is a very easy language to
work with. This module will use Python 3. 

If you haven't done any Python before, then go through `the official
Python tutorial <https://docs.python.org/3/tutorial/index.html>`__. If
you have done a little Python, one feature we will be using a lot is
classes, so if that is new to you you should at least review `the
classes chapter <https://docs.python.org/3/tutorial/classes.html>`__.

The Matlab-like array features of Python are provided by `Numpy
<https://www.numpy.org/>`__ for which there is a `helpful tutorial
<https://numpy.org/devdocs/user/quickstart.html>`__. There is also a
handy `guide for Matlab users
<https://numpy.org/devdocs/user/numpy-for-matlab-users.html>`__. In that context, the
code provided in this course will always use Numpy arrays, and never
Numpy matrices.

.. proof:exercise::

    If you don't already have Python 3.6 or later installed on your computer, follow
    the :doc:`FoNS Python instructions <fons:python>`. We will exclusively use
    :ref:`virtual environments <fons:python_virtual_environments>` so it doesn't
    matter at all whether you use Python from Anaconda or from another source. Mac
    users should note, though that the built-in Python will not do, so you should
    use either Homebrew or Anaconda.

.. note::

    The example code in the exercises uses :ref:`f-strings <tut-f-strings>`
    which were introduced in Python 3.6, so the code will not work in earlier
    versions of Python.

Git
...

Revision control is a mechanism for recording and managing different
versions of changing software. This enables changes to be tracked and
helps in the process of debugging code, and in managing conflicts when
more than one person is working on the same project. Revision control
can be combined with online hosting to provide secure backups and to
enable you to work on code from different locations.

In this module, you'll use revision control to access the skeleton
files, and to update those files if and when they change. You'll also
use the same revision control system to record the edits you make over
time and to submit your work for feedback and, eventually, marking.

We will be using the revision control system `git
<http://git-scm.com/>`_, which is the current state of the art and is
widely adopted. We'll be combining git with the online hosting service `GitHub <http://github.org>`_.

.. proof:exercise::

    Install Git and work through the entire Git,
    GitHub, and GitHub Classroom tutorial on the :doc:`FoNS Git instructions webpage
    <fons:git>`.

    Next, go and do the `git tutorial <https://swcarpentry.github.io/git-novice/>`_
    over at Software Carpentry.

.. hint::

   If you are a more confident computer user, you could go ahead and
   set up git to work with ssh, the secure shell. This will save a lot
   of password typing but it's not essential so if you are not so
   confident with computers, you can skip this bit. GitHub provide
   `instructions for using ssh with git
   <https://help.github.com/articles/generating-an-ssh-key/>`__.


Visual Studio Code
..................

Visual Studio Code is a Python-aware Integrated Development Environment (IDE).
This means that it incorporates editing files with other programming features
such as :ref:`debugging`, Git support, and built-in :ref:`terminal
<terminal-vscode>`. Visual Studio Code also provides an incredibly useful remote
collaborative coding feature called Live Share. This will be very useful for
getting remote help from an instructor. 

.. proof:exercise::

    Install Visual Studio Code using the
    :doc:`FoNS Visual Studio Code installation instructions <fons:vscode>`.

.. proof:exercise::

    Follow the :ref:`FoNS Visual Studio Live Share instructions
    <fons:vscode-liveshare>` instructions to learn how to set up a Live Share.
    Pair up with someone else taking the module to ensure that you can share
    your Visual Studio Code session with them, and they with you. If you need to
    find someone else taking the module to do this exercise with, you can use
    `this Piazza post <https://piazza.com/class/kiujdiwgpk5su?cid=1>`. 

The command line
................

A lot of the routine activity involved in this module revolves around
executing commands on the command line. For example you use the
command line to work with the revision control system. 

.. proof:exercise:: 

    If you're not
    familiar with the Linux command line, then follow at least the first two
    sections of the `Software Carpentry Unix Shell lesson`. That
    guide focusses on the Bash shell, but zsh and the Windows Powershell use very
    similar commands.
