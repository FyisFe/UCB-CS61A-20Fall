- [1. Print and None](#1-print-and-none)
  - [Pure functions & Non-pure functions](#pure-functions--non-pure-functions)
    - [Pure functions](#pure-functions)
    - [Non-pure functions](#non-pure-functions)
    - [Formal definition](#formal-definition)
- [2. Multiple Environments](#2-multiple-environments)
  - [Life Cycle of a Use-Defined Function](#life-cycle-of-a-use-defined-function)

## 1. Print and None

```python
print(print(1),print(2))
# 1
# 2
# None None
```
### Pure functions & Non-pure functions

#### Pure functions
Just return values, no side effects ```abs(), pow()```.

#### Non-pure functions
Have side effects (anything happens as a result of calling a function).

#### Formal definition
>A [pure function](https://en.wikipedia.org/wiki/Pure_function) has the following properties:
> - The function return values are identical for identical arguments (no variation with local static variables, non-local variables, mutable reference arguments or input streams).
>- The function application has no side effects (no mutation of local static variables, non-local variables, mutable reference arguments or input/output streams).

## 2. Multiple Environments 
An environment is a sequence of frames.
- Global frame alone 
- A local, then global frame

Every expression is evaluated in the **context** of an environment. A name evaluates to the value bound to that name in the **earliest** frame of the current environment.
### Life Cycle of a Use-Defined Function

``` python
# Define statement
def square(x): # New func created => Name bounded to it in current frame(scope) 
    return x*x

# Call expression
square(2+2) # Operator & operand evaluated => call function

# Calling expression
4 => square(x) => 16 # New frame created => Params bound to arguments => executed in the new frame
```

