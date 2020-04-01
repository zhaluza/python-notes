# Lambdas & Built-In Functions

## Lambdas

A **lambda function** is essentially an anonymous function.

It takes in arguments and returns something.

```python
square2 = lambda num: num * num

add = lambda a,b: a + b
```

A lambda is an inline function that eliminates the need for writing out entire functions, which can be helpful in certain situations.

For instance, instead of defining a function that will only be used once, you can just write a lambda.

## Map

A `map` is a standard function that accepts at least two arguments:

- A function
- An "iterable"

An **iterable** is something that can be iterated over (list, string, dictionary, set, tuple).

A map function runs the lambda for each value in the iterable and returns a map object — which can then be converted into another data structure.

If you don't wrap `map` in another data structure, it only works once.

```python
nums = [2,4,6,8,10]

doubles = map(lambda x: x*2, nums)

list(doubles)
# [4, 8, 12, 16, 20]

list(doubles)
# []
```

Instead, you could wrap it inside a list or another data structure.

```python
nums = [2,4,6,8,10]

doubles = list(map(lambda x: x*2, nums))

list(doubles)
# [4, 8, 12, 16, 20]
```

```python
names = [
{'first': 'Zac', 'last': 'Haluza'},
{'first': 'Dash', 'last': 'Rendar'}
]

first_names = list(map(lambda x: x['first'], names))

first_names
# ['Zac', 'Dash']
```
