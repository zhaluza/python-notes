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
