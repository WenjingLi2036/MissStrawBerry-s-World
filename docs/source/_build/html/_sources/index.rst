Documentation Demo
===================================

This is a demo page to show how to use ReadtheDocs to automatically generate documentation website based on your **Python** code. Other code such as Arduino, C/C++ should also be supported but needs to be tested.

Readthedocs automatically pulls docstrings from your code file. Some useful tutorials can be found `here <https://docs.readthedocs.com/platform/stable/tutorial/index.html>`_, `here <https://pythonforthelab.com/blog/documenting-with-sphinx-and-readthedocs>`_, and `here <https://amazonwebshark.com/open-source-documentation-with-read-the-docs>`_.

Different from Github, Readthedocs uses reStructuredText (``.rst`` format, instead of ``.md`` format of Markdown) for plain text markup. Here are some cheat sheets of the ``.rst`` format:

- `<https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_
- `<https://sphinx-tutorial.readthedocs.io/cheatsheet>`_

This demonstrates the page reference function:
:ref:`modulefactorial` and :ref:`modulepeople`.

.. note::

   This project is under active development.


Setup
---------
1. Register an account on `Read the Docs <https://docs.readthedocs.com/platform/stable/tutorial/index.html>`_

.. figure:: images/fig1.png

2. Create a new project and link it to your GitHub repository.



Contents
--------
1.

.. toctree::

   usage
   api
