# Loops

## Types of Loops in Python

#### `for` loops

```python
for item in iterable_object:
  # do something with item
```

**Ranges**
The class `range` lets you declare a range between two numbers (if the first number is omitted, the starting number defaults to zero).
It's commonly used in `for` loops.
`class range(start, stop[, step])`

- `range(7)` gives you all integers from 0 to 6.
- `range(1, 8)` gives you all integers from 1 to 7.
- `range(1, 10, 2)` gives you all odd numbers from 1 to 10 (technically 9)
- `range(7, 0, -1)` gives you all integers from 7 to 1 (backwards)

**`for` Loops With Ranges**
To add up all the odd numbers between 10 and 20 (inclusive):

```python
x = 0

for num in range(11,21,2):
    x += num
```

Or, without stepping:

```python
x = 0

for n in range(10, 21):
    if n % 2 != 0:
        x += n
```

#### `while` loops

Basic syntax of a `while` loop:

```python
while im_tired:
  # seek caffeine
```

`while` loops continue to execute while a certain condition is truthy, and they'll end when the condition becomes falsy.

```python
user_response = None
while user_reponse.lower() != 'please':
  user_response = input('Ah ah ah... You didn\'t say the magic word: ')
```
