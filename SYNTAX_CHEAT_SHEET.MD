Python 3 Syntax Cheat Sheet
----

Literals, Variable Declaration and Assignment
----
x = 1 # assign int 1 to x
x = 1.0 # assign float 1 to x
x = "a" # assign string "a" to x

Function
----
    def add(a,b):
        return a, b

Class
---
    class Adder(object):
        def __intit__(self, a, b):
        
Operations
----
`x += 1` means `x = x + 1`

`26 % 5` means return remainder of 26/5

Complex Types: Lists
-----
Can hold any datatype.
    x = []
    x.append("foo")

Special Functions
---
    x = [1,2,3]
    print(len(x))
    print()