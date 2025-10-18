Usage
================

.. autofunction:: my_module.factorial.factorial

.. _modulepeople:

Module People
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.factorial()`` function:

.. py:method:: MyClass.foo(args)
   
   Function to calculate the factorial of *n*.

   .. code-block:: python

      from my_module.factorial import factorial

      result = factorial(5)
      print(result)  # Output: 120
   :param n: An integer whose factorial is to be calculated.
   :type n: int
   :return: The factorial of the given integer *n*.
   :rtype: int 


Function to calculate the factorial of *n*.


The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.factorial`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

.. _modulefactorial:

Module Factorial
----------------
