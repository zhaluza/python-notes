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

## Sorted

`sorted` works similarly to `sort` (they both sort the elements in an iterable), but with two key
differences.

- Whereas `sorted` will sort items _in place_, `sorted` returns a new sorted list.
- `sort` is a list method (and therefore can only sort lists); `sorted` can sort other iterables
  besides lists.

```python
more_numbers = [6,1,8,2]
sorted(more_numbers) # [1, 2, 6, 8]
```

Both `sort` and `sorted` can sort in reverse order:

```python
ex_list = [1,2,3,4,5]
sorted(ex_list, reverse=True) # [5,4,3,2,1]
```

You can also use a `key` parameter to sort more specifically via a function. Lambda functions are a
good choice for this. (Both `sort` and `sorted` have this parameter.)

```python
users = [
    {"username": "sam", "tweets": ["I love cake", "I am cake" ], "fav_color": "red"},
    {"username": "xan", "tweets": ["Cake is dumb" ]},
    {"username": "ali", "tweets": ["what is cake", "?", "I have never heard of this food" ]},
]

sorted(users, key=lambda user: user['username'])
# [
#     {"username": "ali", "tweets": ["what is cake", "?", "I have never heard of this food" ]},
#     {"username": "sam", "tweets": ["Cake is dumb"]},
#     {"username": "xan", "tweets": ["I love cake", "I am cake" ], "fav_color": "red"},
# ]

sorted(users, key=lambda user: len(user['tweets']))
# [
#     {"username": "sam", "tweets": ["Cake is dumb"]},
#     {"username": "xan", "tweets": ["I love cake", "I am cake" ], "fav_color": "red"},
#     {"username": "ali", "tweets": ["what is cake", "?", "I have never heard of this food" ]},
# ]
```

## Max

`max` returns the largest item in an iterable (e.g. a string, array) or the largest of two or more
arguments.

```python
max('hello world') # w
max(1, 2, 3) #3
```

Finding the longest string in an array:

```python
names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
max(names, key=lambda name:len(name)) # 'Ollivander'
```

## Min

`min` returns the smallest item in an iterable or the smallest of two or more arguments.

```python
min([40,32,6,5,10]) # 5
min('hello world') # ' '
```

Finding the shortest string in an array:

```python
names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
min(names, key=lambda name:len(name)) # 'Tim'
```
