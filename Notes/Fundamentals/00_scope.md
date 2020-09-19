# Scope

In Python, variables declared **outside a function** are accessible globally throughout the file.

However, variables declared **inside a function** are _only accessible inside that function_.

```python
animal = 'liger'

def say_hello():
  return f'Hello {animal}'

say_hello() # 'Hello liger'
```

```python
def say_hello():
  animal = 'liger'
  return f'Hello {animal}'

say_hello() # 'Hello liger'
print(animal) # NameError
```

## Global Scope

As mentioned above, variables declared outside functions are globally accessible.

While Python can **read** global variables without a problem, it can't **change** them quite as easily.

```python
total = 0

def increment():
  total += 1
  return total

increment() # Error
```

By default, Python will assume that `total` is a variable local to the function. To make it realize that it's a global variable, declare it inside the function using the `global` keyword:

```python
total = 0

def increment():
  global total
  total += 1
  return total

increment() # 1
```

Generally speaking, it isn't a good idea to rely on global variables.

## Nonlocal scope

The `nonlocal` keyword lets us modify a parent's variables in a child (aka nested) function.

In other words, it lets you work with a variable that isn't global, but is defined in a parent/ancestor function.

```python
def outer():
  count = 0
  def inner():
    nonlocal count
    count += 1
    return count
  return inner()

outer() # 1
```

**Note:** The `global` and `nonlocal` keywords aren't commonly used, but they provide an important look into how Python handles scope.
