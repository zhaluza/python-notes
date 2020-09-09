## All

Returns `True` if all elements of the iterable are truthy (or if the iterable is empty).

```python
all([0,1,2,3]) # False
all([char for char in 'eio' if char in 'aeio']) # True
all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True
```

## Any

Returns `True` if any element of the iterable is truthy. If the iterable is empty, it returns
`False`.

```python
any([0,1,2,3]) # True
any([val for val in [1,2,3] if val > 2]) # True
any([val for val in [1,2,3] if val > 5]) # False
```

#### Generator Expressions

Note that
[generator expressions can be a better option than list comprehensions](https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension)
if you want to save space on an expression you're running only once.

```python
# Generator expression
(x*2 for x in range(256))

# List comprehension
[x*2 for x in range(256)]
```

"Basically, use a generator expression if all you're doing is iterating once. If you want to store
and use the generated results, then you're probably better off with a list comprehension."
