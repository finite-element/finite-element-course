Computational tools
===================

Access to computers
-------------------

You'll need access to a suitable computer for the implementation
work. If you have your own laptop running Linux (or possibly MacOS)
then you are welcome to use that. It may be possible to do the module
using a Python installation on Windows, but this is a very unsupported
option. For other Department of Mathematics students, the server
``mpe1.ma.ac.uk.uk`` is available for your work on this module and can
be accessed over ssh from anywhere on the Imperial network.

Connecting to ``mpe1`` from a lab machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Machines in 410 run Windows, but have X servers and SSH clients
which enable you to log into a remote Linux machine and run graphical
programs as if they were running locally.

Starting XMing
..............

 1. Run ``XLaunch`` from the Start menu. 
 2. You should now see a window titled ``Display settings``. Select ``Multiple windows`` and set ``Display number`` to 0. (These should be the default settings).
 3. Now click ``Next`` and continue to click ``Next`` on the next two windows.
 4. On the ``Finish configuration`` screen click ``Finish``.
 5. The Window will now disappear. This is normal. Xming is running in the background and waiting for an X program to start.

Starting PuTTY (SSH)
....................


 6. Run ``PuTTY`` from the Start menu.
 7. Set the host name to ``mpe1``. If you are not a Department of
    Mathematics student, you'll need to use another machine here, and
    you'll need to type the full hostname (e.g. ``foo.ese.ic.ac.uk``).
 8. In the left window select ``SSH`` (second to last) and under that select ``X``.
 9. Select the tick box ``Enable X11 forwarding``.
 10. Set ``X display location`` to ``:0.0``.
 11. You may wish to return to the ``Session`` section and save this
     configuration for future use. The name of the machine you are
     logging into (e.g. ``mpe1``) is a good name for the session name.
 12. Click ``Open``. If you get a warning window about the host key, click ``OK``.
 13. Log in using your Imperial College username and password.
 14. Test the setup by running ``xeyes`` on the command line. You
     should see a pair of eyes which follow the mouse pointer as it
     moves around the screen. This demonstrates that the graphical
     program forwarding is working.

Using your own machine
~~~~~~~~~~~~~~~~~~~~~~

If you plan to use your own machine for the module, you will need a
basic scientific Python toolchain and the visualisation package
Paraview. On Ubuntu and its relatives, this can be achieved with::

  sudo apt-get install ipython python-scipy python-pytest python-matplotlib paraview

If you wish to use MacOS then please consult the lecturer as we will
have to work through the install for that operating system.


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

Bitbucket and git
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
`Bitbucket <http://bitbucket.org>`_. Bitbucket is one of the two
leading revision control hosting services, the other is `GitHub
<http://github.org>`_. We've chosen Bitbucket for teaching because it
offers unlimited private repositories to academic users.

Getting started with git and Bitbucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The good folks over at Bitbucket have fortunately provided a good
tutorial for getting started with the tools. The tutorial is called
`Bitbucket 201
<https://confluence.atlassian.com/display/BITBUCKET/Bitbucket+201+Bitbucket+with+Git+and+Mercurial>`_
and you'll want to work through that first. Bitbucket supports two
revision control systems: git and mercurial. We'll be exclusively
using git so you can ignore the instructions in the tutorial for using
mercurial.

Sharing your problems with gists
--------------------------------

At some points during the module, you're sure to create bugs in your
code that you don't know how to fix. If you're not in class at the
time, you'll need a convenient way to share a piece of code or output
with the lecturer and the class. GitHub (the other hosting service)
provides this facility, which they call `gists`. For this you'll want
a GitHub account so head over there and `sign up
<https://github.com>`_.

Once you've signed up and logged in, you can navigate to
`https://gist.github.com`_ and there's a very simple webpage into which
you can paste your code or output. You should also set the language so
that GitHub formats your gist correctly. Click `create public gist`
and you're done. You can then paste the URL of your gist page into an
email or into a Bitbucket issue.
