# Functions

Standard format for Python functions:

```python
def name_of_function():
  # block of runnable code
```

For example:

```python
def say_hi():
  return 'Hi'

say_hi()
# Hi
```

The `return` keyword:

- Exits the function
- Pops the function off the callstack

#### Simple Example

This function will randomly return "heads" or "tails" when run:

```python
from random import random

def flip_coin():
    # note: 'random' generates num between 0 and 1

    # generate random number (0-1) using 'random'
    # return 'heads' or 'tails' depending on whether it's closer to 0 or 1
    if random() > 0.5:
        return 'heads'
    else:
        return 'tails'
```

## Default Parameters

If you want to make a certain parameter optional for the user to enter, you can assign it a value inside the function definition.

By default, the below function will **square** the inputted argument.

```python
def exponent(num, power=2):
  return num ** power
```

```python
def add(num1=10, num2=20):
  return num1 + num2

add() # 30
```

#### Benefits of Default Params

- Lets you program more flexibly (can use the same function in multiple situations)
- Avoids errors with incorrect parameters
- Examples are more readable\

## Keyword Arguments

While Python typically reads any inputted arguments according to the order the parameters are defined in the function (e.g. first argument = first parameter), you can circumvent this if you want:

```python
def full_name(first, last):
  return "Your name is {first} {last}"

full_name(first='Zac', last='Haluza') # Your name is Zac Haluza

full_name(last='Haluza', first='Zac') # Your name is Zac Haluza
```

#### Why Use Keyword Arguments?

- Allows for more flexibility
- Useful when passing a dictionary to a function and unpacking its values

## Documenting Functions

In Python, you can include a note at the top of a function to indicate its purpose. This is done using **triple quotes**: `""" """`

You can invoke the documentation by appending `.__doc__` to the end of the function's name and calling it.

```python
def say_hello():
  """A simple function that returns the string 'hello'"""
  return "Hello!"

say_hello.__doc__ # A simple function that returns the string 'hello'
```

You can also access the `doc` notes for common methods like `print` or `random.randint`.
