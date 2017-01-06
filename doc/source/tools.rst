Computational tools
===================

Access to computers
-------------------

You'll need access to a suitable computer for the implementation
work. The machines in Huxley 410 have suitable software installed, or you can use your own laptop running Windows, Linux, or OS X. 

Using the Windows machines in Huxley 410
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. From the start menu run `Git Bash`. This provides you with a Bash
   (Unix) command line from which you can run the git revision
   control software to manage your source code.

2. Run `Enthought Canopy`. There should be a shortcut link on the left
   hand side of the desktop. Alternatively, you can find it via the
   start menu. The first time you run Canopy on a particular machine,
   one or two popup windows will appear. You should agree to whatever
   they ask!

3. Launch the editor by clicking on the `Editor` button.

4. Once you have cloned your git repositiory (more on this later), you
   will need to type the following command on the Python
   command line at the beginning of each session in order to ensure
   you are running from the correct directory::

     cd H:\finite-element-course

   replacing username with your GitHub username.
     
Using your own Windows machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to use your own Windows machine, you'll simply need Python
(with the right packages) and git. We recommend you install Enthought
Canopy, but other Windows Python distributions should also work.

1. Download and install `Enthought Canopy Express` from `here <https://store.enthought.com/#canopy-individual>`_.

2. Download and install `git` from `here <https://git-scm.com/download/win>`_.

3. You should now be able to use git and Python exactly as in Huxley
   410, except that the directory where your finite element source
   code lives will be different (and may depend on how your Windows
   machine is set up).
     

Using your own Linux machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you plan to use your own machine for the module, you will need a
basic scientific Python toolchain. On Ubuntu and its relatives, this can be achieved with::

  sudo apt-get install ipython python-scipy python-pytest python-matplotlib

Using your own Mac
~~~~~~~~~~~~~~~~~~

This is an experimental set of instructions for obtaining the software
you need on Mac. Please say if you encounter any trouble.

We recommend using `Homebrew <http://brew.sh>`__ as a package manager
for the required packages on Mac OS systems.  Obtaining a build
environment for PyOP2 consists of the following:

1. Install Xcode.  For OS X 10.9 (Mavericks)  and later, this is possible through
   the App Store.  For earlier versions, try
   https://developer.apple.com/downloads (note that on OS X 10.7
   (Lion) you will need to obtain Xcode 4.6 rather than Xcode 5)

2. If you did not install Xcode 5, you will need to additionally
   install the Xcode command line tools through the downloads section
   of Xcode's preferences

3. Install homebrew, following the instructions at http://brew.sh

4. Install an up-to-date Python via homebrew::

     brew install python

5. Install numpy via homebrew::

     brew tap homebrew/python
     brew install numpy

6. Install python dependencies via pip::

     pip install decorator
     pip install ipython
     pip install matplotlib
     pip install pytest
     pip install flake8
     pip install scipy


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
work with.

If you haven't done any Python before, then go through `the official
Python tutorial <https://docs.python.org/2/tutorial/index.html>`_. If
you have done a little Python, one feature we will be using a lot is
classes, so if that is new to you you should at least review `the
classes chapter <https://docs.python.org/2/tutorial/classes.html>`_.

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
widely adopted. We'll be combining git with the online hosting service
 `GitHub <http://github.org>`_.
 
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
  "It didn't work" is useless. "I typed ``import fe_utils'' and
  recieved the following error.`` is much better.

Provide a minimal failing example
  Post the smallest piece of code which exhibits the problem. This
  makes finding the issue much easier.

Use gists 
  Copy exactly what happened, complete with error messages,
  into a gist and post the link in the issue.
