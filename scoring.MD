Feature Sets
-------------
Feature sets should progress along this order:
- Executes with no keyboard input
- Console input
- Validation, error handling, error recovery
- Games - computer is naive player
- Games - computer is smart player
- Algorithms are brute force (i.e. no effort to be efficient)
- Algorithms take steps to reduce computation time (For real life code, these kata are too simple to call for performance optimization!)


Level 1- Scripting
-------
Nothing parameterized, no functions, no containers.

Tests demonstrate that code runs and throws no errors

Level 2- "Modular"
-------
At least one container (other than the file), some things parameterized. In otherwords code is broken into functions with argument that have return values. When there are large numbers of functions, they are split across files (modules), when there are
large numbers of files, they are split across related folders (submodules)

Has unit tests to exercise functions and something is asserted (except for the main() or run() function)


Level 3- OOP, Functional, or other higher level style.
-------
OOP or functional programming. Everything parameterized, classes are general, generic code separated from the domain specific code.

Code has features specifically for testability (e.g. able to specify a known date instead of using system clock)


Positive Marks:
----
- Function count
- Functions reference only arguments
- Functions return values and are not called on for side effects
- Functions do one thing
- Functions are generic (i.e. keep domain considerations separate from algorithmic)
- Classes instead of functions
- Well behaved modules, functions and classes (i.e. implement things the ecosystem expects, such as type annotations, docstrings, __dunder__ methods on classes, module headers (encoding type, import future))
- Considers edge cases (i.e. has guards)
- Exemplifies target style. If the exercise is explicitly to show of OOP, uses classes. For showing of functional programming, use curries, partials, composition, etc. 

Negative Marks
---
- Functions called for side effects
- Bad linting & formatting
- Throws on basic errors
- Flat (i.e. no functions, classes, unless it is a scripting exercise) 1/2 credit for modular (i.e. breaking code into many files using the file as the primary container)
- Too clever for own good (i.e. "write once" code that is so complex you'll never be able to safely edit it again)

Disqualifying Marks
---
- Copying pasting a solved answer found on the internet. It's dishonest and juvenile.
- Incoherent
