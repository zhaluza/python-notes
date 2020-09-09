# Lambdas & Built-In Functions

## Lambdas

A **lambda function** is like an anonymous function in JavaScript, or a function expression. If not
saved to a variable, it can only be used once.

It takes in arguments and returns something.

```python
square2 = lambda num: num * num

add = lambda a,b: a + b
```

A lambda is an inline function that eliminates the need for writing out entire functions, which can
be helpful in certain situations.

For instance, instead of defining a function that will only be used once, you can just write a
lambda.

## Map

A `map` is a standard function that accepts at least two arguments:

- A function
- An "iterable"

An **iterable** is something that can be iterated over (list, string, dictionary, set, tuple).

A map function runs the lambda for each value in the iterable and returns a map object — which can
then be converted into another data structure.

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

## Filter

`filter` lets us return a "filtered" version of a collection of data. It returns a filter object
with the data that meets a specified condition.

```python
names = ['austin', 'penny', 'anthony', 'angel', 'billy']

# get the names starting with 'a'
a_names = filter(list(lambda name: name[0]=='a', names))

a_names
# ['austin', 'anthony', 'angel']
```

### Combining `filter` and `map`

Given this list of names: `names = ['Lassie', 'Zac', 'Rusty']`

Return a new list with the string "Your instructor is " + each value in the array, but only if the
value is less than 5 characters.

```python
list(map(lambda name: f"Your instructor is {name}",
filter(lambda value: len(value) < 5, names)))

# ['Your instructor is Zac']
```

You could accomplish this with a list comprehension:

```python
[f"Your instructor is {name}" for name in names if len(name) < 5]
```

However, it's important to be aware of the importance of filter and map.

Note that while using the filter and math methods might feel more natural for JavaScript developers,
the "Python" way is to use a comprehension.

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
