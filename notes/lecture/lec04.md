- [1. Design Functions](#1-design-functions)
  - [Pure functions & Non-pure functions](#pure-functions--non-pure-functions)
    - [Pure functions](#pure-functions)
    - [Non-pure functions](#non-pure-functions)
    - [Formal definition](#formal-definition)
- [2. Multiple Environments](#2-multiple-environments)
  - [Life Cycle of a Use-Defined Function](#life-cycle-of-a-use-defined-function)

## 1. Design functions

- One function one job
- Don't repeat yourself (DRY)
- Define function generally

## Higher-order functions

> Higher-order functions are functions that take other functions as arguments or return functions.

```python
from math import pi

def area_square(x):
    assert x>0, 'Must be positive' # Repeate yourself
    return x*x

def area_circle(x):
    assert x>0, 'Must be positive' # Repeate yourself
    return pi*x*x

####### Generalization ####### 
def area(x, shape_constant): # <= higher order function
    assert x>0, 'Must be positive'
    return x*x*shape_constant

def area_square(x):
    return area(x,1)

def area_circle(x):
    return area(x,pi)
```