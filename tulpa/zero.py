'''Zero is ...

- First item with some lengthy
  text wrapping hopefully
  across several lines.

  * We can have subitems
  * separated by a blank line
  * and indented.

- Second item

'''


def sum(a : int, b : int) -> int:
    ''' This function is intended to return the sum of two integer values

    Here's a doctest block:

    >>> print 'python-specific usage examples: '
    >>> sum(1,2) -> 3


    :param int a: An integer to be computed
    :param int b: An integer to be computed

    :returns: The sum of two integer values 

    |
    
    ==  ==
    aA  bB
    cC  dD
    ==  ==

    .. _pocoo:  http://sphinx.pocoo.org

|
|
|

    '''
    return a + b


def sum2(a : int, b : int) -> int:
    ''' This function is intended to return the sum of two integer values

here's a doctest block:

>>> print 'python-specific usage examples: '
>>> sum(1,2) -> 3


:param int a: An integer to be computed
:param int b: An integer to be computed

:returns: The sum of two integer values 


.. code-block:: python
   :emphasize-lines: 3,5

      def some_function():
            interesting = False
            print 'This line is highlighted.'
            print 'This one is not...'
            print '...but this one is.'


    '''
    return a + b
