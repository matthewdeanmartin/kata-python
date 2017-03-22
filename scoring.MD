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


Scoring for all styles
-----
- Syntactically valid.
- Exemplifies target style. If the exercise is explicitly to show of OOP, uses classes. For showing of functional programming, use curries, partials, composition, etc.

Level 1- Scripting
-------
Nothing parameterized, no functions, no containers.

Tests demonstrate that code runs and throws no errors

- "Well it works!" Scripting style encourages an attitude of writing code with lots of stylistic short cuts so long as the final result works for the one set of inputs we care about
- Makes appropriate decisions about "stopping due to errors" and "keeping going no matter what"

Level 2- "Modular"
-------
At least one container (other than the file), some things parameterized. In otherwords code is broken into functions with argument that have return values. When there are large numbers of functions, they are split across files (modules), when there are
large numbers of files, they are split across related folders (submodules)

Has unit tests to exercise functions and something is asserted (except for the main() or run() function)

- Functions are cohesive and do one thing
- Function count (i.e. is the code factored into many small cohesive functions/methods)
- Functions are pure when possible, i.e. have no side effects and only take arguments, return values and maybe throw exceptions. Obviously at some point in the call stack an interesting application must have side effects. If all functions have side effects and functions that could be easily refactored into a pure/non-pure function are left as a hybrid, then that is a problem.
 - Functions have as few constants as possible, i.e. when possible, use function argument instead of literals.
- Functions are generic (i.e. keep domain considerations separate from algorithmic)
- Considers edge cases (i.e. has guards, checks plausibility of return values, checks invariants which should be true both at the start and finish of the function)

Level 3- OOP, Functional, or other higher level style.
-------
OOP or functional programming. Everything parameterized, classes are general, generic code separated from the domain specific code.

Code has features specifically for testability (e.g. able to specify a known date instead of using system clock)

- A stateful class instead of functions
- A collection of related classes with IS-A and HAS-A relationships among them and a clear distinction between reference types (objects with an identity) and value types (objects that may be implemented as classes, but represent something without an identity, for example, a "Distance" object with units and distance properties mean the same thing if the values of the properties are the same)
- Well behaved modules, functions and classes (i.e. implement things the ecosystem expects, such as type annotations, docstrings, __dunder__ methods on classes, module headers (encoding type, import future))


Negative Marks
---
- Functions called for side effects unnecessarily
- Bad linting & formatting
- Throws on basic errors. Continues despite serious errors
- Flat (i.e. no functions, classes, unless it is a scripting exercise) 1/2 credit for modular (i.e. breaking code into many files using the file as the primary container)
- Too clever for own good (i.e. "write once" code that is so complex you'll never be able to safely edit it again)

Disqualifying Marks
---
- Copying pasting a solved answer found on the internet. It's dishonest and juvenile.
- Incoherent
