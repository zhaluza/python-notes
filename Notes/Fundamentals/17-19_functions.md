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

---

## Function Parameters

Python offers a few special ways to set function parameters and handle arguments.

### Default Parameters

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

### Keyword Arguments

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

### `*args`

`*args` is a special operator that we can pass to functions. It gathers the remaining arguments as a **tuple**.

You can name it anything you want, as long as it starts with a `*`. (`*args` is the convention, though.)

Similar to the spread operator in JavaScript, `*args` will collect any additional arguments that have been passed in. It will then store them in a **tuple** under the value `args` (or whatever follows the asterisk).

```python
def print_all_args(*args):
  print(args)
print_all_args(1, 2, 3, 4)
# (1, 2, 3, 4)
```

For example, you can create a `sum_all_nums` function that takes in any number of arguments:

```python
def sum_all_nums(*args):
  total = 0
  for num in args:
    total += num
  return total
```

### `**kwargs`

Short for **keyword arguments**.

`**kwargs` works similarly to `*args`, except instead of storing all args inside a tuple, it stores them inside a **dictionary**.

```python
def fav_colors(**kwargs):
  print(kwargs)
fav_colors(zac="red", kaylee="pink")
# ['zac': 'red', 'kaylee': 'pink']

def fav_colors_statement(**kwargs):
  for person, color in kwargs.items():
    print(f"{person}'s favorite color is {color}.")
fav_colors_statement(zac="red", kaylee="pink")
# Zac's favorite color is red.
# Kaylee's favorite color is pink.
```

### Parameter Ordering

How you should order your parameters inside your functions:

1. parameters
2. `*args`
3. default parameters
4. `**kwargs`

Here's how this order works in action:

```python
def display_info(a, b, *args, developer="Zac", **kwargs):
  return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3, last_name="Haluza", job="developer"))

#### How the params are assigned:
# a - 1
# b - 2
# args (3)
# developer - "Zac"
# kwargs - {"last_name": "Haluza", "job": "developer"}

### Actual output:
[1, 2, (3,), "Zac", {'last_name': 'Haluza', 'job': 'developer'}]
```

## Argument Unpacking

### Unpacking Tuples

We can use `*` as an argument to a function to unpack values.

What if we want to pass a data structure filled with numbers into a function that sums up all arguments fed into it?

```python
def sum_all_nums(*args):
  total = 0
  for num in args:
    total += num
  print(total)
```

While we can't use a list (like `[1, 2, 3, 4]`), we can use a tuple — e.g. `(1, 2, 3, 4)`. To pass a tuple into this function as an argument, we should use a `*`, just like it's used in the parameter:

```python
nums = (1, 2, 3, 4, 5, 6)
sum_all_nums(*nums)
# 21
```

### Unpacking Dictionaries

We can use `**` as an argument to unpack dictionaries.

What if we have a function that takes in two arguments and a dictionary with two properties, and we want to pass the dictionary's properties in as arguments?

We put `**` before the name of the dictionary when we pass it into the function.

```python
names = {'first': 'Zac', 'second': 'Anxiety'}
def display_names(first, second):
  print(f'{first} says hello to {second}')

display_names(**)

# Zac says hello to Anxiety
```

```python
def add_and_multiply_numbers(a, b, c)
  return a + b * c

data = dict(a=1, b=2, c=3)

add_and_multiply_numbers(**data) #7
```
