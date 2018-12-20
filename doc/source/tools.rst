Computational tools
===================

Access to computers
-------------------

You'll need access to a suitable computer for the implementation
work. You can either use the machines in the maths department labs, or you can use your own laptop running Windows, Linux, or macOS.
The core requirements are Python 3, git, and a Python-aware text editor.

Using the Windows machines in the computer labs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Imperial's lab machines have the software you need installed, in some
cases via the `Software Hub`. To get started, double click the
`Software Hub` icon on the desktop or `click here
<https://softwarehub.imperial.ac.uk/>`_. From there you can run `git`,
which will give you a terminal to run git and Python commands, and
`atom`, which will provide you with an editor.

Using your own Windows machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to use your own Windows machine, you'll simply need Python 3
(with the right packages) and git. One option is to install Anaconda, but other Windows Python distributions should also work.

1. Download and install `Anaconda` from `here <https://www.anaconda.com>`_.

2. Download and install `git` from `here <https://git-scm.com/download/win>`_.
     

Using your own Linux machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you plan to use your own machine for the module, you will need a
basic  Python toolchain. On Ubuntu and its relatives, this can be achieved with::

  sudo apt-get install python3 git

Using your own Mac
~~~~~~~~~~~~~~~~~~

We recommend using `Homebrew <http://brew.sh>`__ as a package manager
for the required packages on Mac OS systems, however other ways of getting Python 3 may well work.

1. Install homebrew, following the instructions at http://brew.sh.

2. Install an up-to-date Python via homebrew::

     brew install python3

Editing code
~~~~~~~~~~~~

In order to write the code required for the implementation exercise,
you'll need to use a Python-aware text editor. There are many such
editors available and you can use any you like. One good option is
called `atom` which is available on the `software hub
<https://softwarehub.imperial.ac.uk/>`_ At Imperial or can be
downloaded `here <http://atom.io>`_.


The command line
----------------

A lot of the routine activity involved in this module revolves around
executing commands on the Bash command line. For example you use the
command line to work with the revision control system. If you're not
familiar with the Linux command line, then a brief guide `is available
here <http://www.tuxarena.com/static/intro_linux_cli.php>`_. That
guide focusses on the Bash shell, which is the one we will use.

Python
------

Your implementation will be written in Python based on a code skeleton
provided. This means that you'll need a certain familiarity with the
Python language. But don't panic! Python is a very easy language to
work with. This module will use Python 3. 

If you haven't done any Python before, then go through `the official
Python tutorial <https://docs.python.org/3/tutorial/index.html>`_. If
you have done a little Python, one feature we will be using a lot is
classes, so if that is new to you you should at least review `the
classes chapter <https://docs.python.org/3/tutorial/classes.html>`_.

The Matlab-like array features of Python are provided by `Numpy
<http://www.numpy.org/>`_ for which there is a `helpful tutorial
<http://wiki.scipy.org/Tentative_NumPy_Tutorial>`_. There is also a
handy `guide for Matlab users
<http://wiki.scipy.org/NumPy_for_Matlab_Users>`_. In that context, the
code provided in this course will always use Numpy arrays, and never
Numpy matrices.


.. _bitbucket-git:

GitHub and git
-----------------

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

Getting started with git and GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The very first thing you'll need is a GitHub account. Navigate to `GitHub <https://github.com/>`_ and sign up.
.. note::

   Make sure you use your Imperial College email address on
   GitHub. This enables you to request unlimited free private GitHub
   repositories and other goodies by `applying here
   <https://education.github.com/pack>`_. You don't strictly need this
   for this module, but there are some nice things in there that you
   might want anyway.

Next you need to do just a little Git setup. At the `Git Bash` command
line, type the following::
  
  git config --global user.name "Jane Bloggs"

Obviously you put in your own name rather than "Jane Bloggs". Similarly, you need to set your email::

  git config --global user.email "Jane.Bloggs12@imperial.ac.uk"

Once again, you obviously use your own email address. Now there is a
small setting which makes the output of git colourful and therefore a
lot easier to read::
  
  git config --global color.ui "auto"

.. hint::

   If you are a more confident computer user, you could go ahead and
   set up git to work with ssh, the secure shell. This will save a lot
   of password typing but it's not essential so if you are not so
   confident with computers, you can skip this bit. The instructions
   are `here
   <https://help.github.com/articles/generating-an-ssh-key/>`_.

Now go and do the `git tutorial <https://swcarpentry.github.io/git-novice/>`_ over at Software Carpentry.


Sharing your problems with gists
--------------------------------

At some points during the module, you're sure to create bugs in your
code that you don't know how to fix. If you're not in class at the
time, you'll need a convenient way to share a piece of code or output
with the lecturer and the class. GitHub
provides this facility, which they call `gists`. 

Once you've signed up and logged in, you can navigate to https://gist.github.com and there's a very simple webpage into which
you can paste your code or output. You should also set the language so
that GitHub formats your gist correctly. Click `create public gist`
and you're done. You can then paste the URL of your gist page into an
email or into a GitHub issue.

.. role:: strikethrough

Raising :strikethrough:`hell` issues
------------------------------------

If you have problems you can't solve yourself, you can share them with
the class by `raising an issue on GitHub <https://github.com/finite-element/finite-element-course/issues>`_. When you do this, here are
some tips which will help get your problem fixed:

Be precise 
  "It didn't work" is useless. "I typed ``import fe_utils`` and
  recieved the following error." is much better.

Provide a minimal failing example
  Post the smallest piece of code which exhibits the problem. This
  makes finding the issue much easier.

Use gists 
  Copy exactly what happened, complete with error messages,
  into a gist and post the link in the issue.
