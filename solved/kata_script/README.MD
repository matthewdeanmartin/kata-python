What is a "Script"
-----
A script could hypothetically be run in interactively in a REPL by typing it as you go.

    Python 3.4.3 (default, Jul 14 2016, 13:53:28)
    [GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> income = 20000
    >>> rent = 1200
    >>> annual_rent = rent * 12
    >>> housing_burden = annual_rent / income
    >>> housing_burden
    0.72
    >>>
    
So few functions, few loops, few if-blocks.

REPL's also favor code that can be written in one line to take advantage of the  "arrow up" so it can be modified and re-executed quickly.

Appropriate Times for Scripting
------
One-off tasks that will never happen again.

Checking how a specific part of the language works without writing a full application, such as verifying if 1/3 results in an integer result or in a float.

To take advantage of Ipython's specific features such as graphing for data exploration.

To create a "notebook" for creating a mulitmedia document with executable code mixed with text, especially for pedagogy.

Certain debugging tasks (i.e. interactively importing and inspecting a live objects attributes)

Inappropriate Scripting
------
Crafting a function. Anything with significant loops and if-blocks. A 25 line series of commands you need to run more than once.