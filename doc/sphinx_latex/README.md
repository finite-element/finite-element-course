Custom LaTeX and HTML builders for Sphinx - Python documentation tool
=====================================================================

This is code contains LaTeX and HTML builders for Sphinx - the Python default
documentation tool which uses the ReStructuredText (RST) file format.  It
allows for custom build LaTeX documents: you can define your own LaTeX
preambule, e.g.  use whatever class you would like to use (for example the
memoir class).  Also adds a few LaTeX type directives (align, theorem, definition,
etc)

Installation
------------

To install the extension follow the standard
[way](http://sphinx-doc.org/extensions.html), i.e. put the python files
somewhere in your $PYTHONPATH and add "clatex_builder" to `extensions` list in
your conf.py file.

options
-------

The following options are recognised in the conf.py file:

```
clatex_documentclass
```
String option with the default value: `\documentclass{book}\n`: note that it
should provide whole document class command, not just the document class name.
In this way you can control document class options.

```
clatex_preambule
```
LaTeX preambule used added to the LaTeX source files.  It should not contain
only the document class statement.  This plugin will only add a minimal set of
needed LaTeX packages: hyperref, longtable, tabluary, multirow and possibly
makeidx package.  You can also add the attached tex/fresh.sty package.  It is
a simpler version of the original sphinx.sty package.  It does not use \bf
and \rm commands (which are not always defined, c.f. memoir).  For more
information see the package itself.

```
clatex_use_chapters
```
this is a boolean option with the default value `True`.  If `False` the major
section unit will be `\section` (what is useful for the article document
class).

```
clatex_begin_doc
```
By default it is an empty string.  The value of this option will be added just
after `\begin{document}` into the LaTeX source file.

```
clatex_end_doc
```
By default it is an empty string.  The value of this option will be added just
before `\end{document}`.

```
clatex_highlighter
```
Boolean options, by default `True`.  If `True` a code highlighter will be
inserted into LaTeX preambule.  You can turn it off if you are not writing
computer related stuff where you do not need to highlight code snippets.

```
clatex_hyperref_args
```
String options, by default an empty string.  List of options added to the
command `\usepackage[...]{hyperref}`.

```
clatex_makeidx
```
Boolean option, by default `False`.  If `True` will add just
`\usepackage{makeidx}\n\makeindex` into the preamble.  If it is a string the
string will be added (in this way you can add options to the
`\usepackage{makeidx}` command.  You can use `clatex_end_doc` to insert the
`\printindex` command - it is not added by default!



theorems and newtheorem function
--------------------------------

Furthermore it allows you to define LaTeX like environments and use them in
the rst source files.  There are predefined directives:

```
.. theorem::

.. proposition::

.. definition::

.. lemma::

.. example::

.. exercise::
```

The directives work in a very similar way to the corresponding LaTeX
environment: they all are numbered.  You can define your own environment.
For that you need to add your own [extension to
Sphinx](http://sphinx-doc.org/extensions.html) and add the following code to
the `setup` function:

```
def setup(app)

    newtheorem(app, 'theorem', 'Theorem', 'theorem')

```

The `newtheorem()` function works in a very similar way to the LaTeX
\newtheorem{}{}{} command.  That means that the above code will define a `..
theorem::` directive, which will use `Theorem` as the environment name and the
directives will be numbered like `theorem` (the third argument).  For example
if you add also

```
    newtheorem(app, 'definition', 'Definition', 'theorem')
```

All the definition directives will be counted together with theorem
directives.  There is currently no way to bind the numbering with the section
numbers (like Definition 1.1, 1.2 in the first chapter; 2.1, 2.2, ... etc in
the second one) - but I have started working on this and I have an idea how to
implement it - though it requires some effort.


The syntax for the directive is very similar to

```
\begin{theorem}[title]
    ...
\end{theorem}
```
the equivalent usage of theorem directive is:

```
.. theorem:: title

    ...
```

environment directive
---------------------

Furthermore, there is an environment directive which allows for more
sophisticated constructions:

```
.. environment::
    :class: ENV_CLASS
    :name: Definition
    :html_title: title used by html builder
    :latex_title: title used by latex builder

	...
```
You can also use `:title:` which if both `:html_title:` and `:latex_title:`
are ought to be the same.  This directive will probably be changed in future
releases.

textcolor role
--------------

You can also change the color with the `:textcolor:` role:

```
:textcolor:`<color_spec> colored text`
```
The color_spec is an HTML color model, e.g. #ffffff for white, #00ff00 for
green, etc.  The LaTeX builder is using \textcolor[HTML]{color_spec}{colored
text} (with the `#` removed from `color_spec`).  The HTML builder is using

```
<font color="color_spec">colored text</font>
```
to change the font color.

endpar directive
----------------

The ``.. endpar::`` directive will input </br> into HTML and an empty line
into LaTeX source file - which ends a paragraph in LaTeX.


align directive
---------------

There is also align directive which aligns the code:

```
.. align:: center

    Centered text

.. align:: flushleft

    Left aligned text

.. align:: flushright

    Right aligned text
```
You can also use 'left' and 'right' instead of 'flushleft' and 'flushright'.
