## all

Returns `True` if all elements of the iterable are truthy (or if the iterable is empty).

```python
all([0,1,2,3]) # False
all([char for char in 'eio' if char in 'aeio']) # True
all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True
```

## any

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

## sorted

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

## max

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

Finding the most played song in a list:

```python
songs = [
  {"title": "I, The Destroyer", "playcount": 3},
  {"title": "Hysteria", "playcount": 6},
  {"title": "Icarus Lives", "playcount": 88},
  {"title": "Concealing Fate, Pt. 2", "playcount": 31},
]

max(songs, key=lambda song: song['playcount']) # {"title": "Icarus Lives", "playcount": 88}
max(songs, key=lambda song: song['playcount'])['title'] # "Icarus Lives"
```

## min

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

Finding the least played song in a list:

```python
songs = [
  {"title": "I, The Destroyer", "playcount": 3},
  {"title": "Hysteria", "playcount": 6},
  {"title": "Icarus Lives", "playcount": 88},
  {"title": "Concealing Fate, Pt. 2", "playcount": 31},
]

min(songs, key=lambda song: song['playcount']) # {"title": "I, The Destroyer", "playcount": 3}
min(songs, key=lambda song: song['playcount'])['title'] # "I, The Destroyer"
```

## reversed

Like `sorted` and `sort`, `reversed` works similarly to `reverse`, but on other things besides
lists.

Using `reverse`

```python
nums = [1,2,3,4]
nums.reverse() # [4,3,2,1]
```

Using `reversed` _(note: returns an iterator object - needs to be converted)_

```python
nums = [1,2,3,4]
list(reversed(nums)) # [4,3,2,1]

greeting = 'hello'
''.join(list(reversed(greeting))) # 'olleh'

# just use a slice method for this, though
"hello"[::-1] # 'olleh'
```

You can use `reversed` to loop backwards through a given range!

```python
for x in reversed(range(0,10)):
  # do something awesome
```

## len

Method that provides the length of a string or object. Calls the element's `__len__` property behind
the scenes.

```python
len([1,2,3,4]) #4
```

## abs

Returns the absolute value of a number. Can be an integer or floating point number

## sum

Takes in an iterable and an optional start - returns the sum of _start_ and the items of an iterable
from left to right.

```python
sum([1,2,3]) # 6
sum([1,2,3], 10) # 16
```

_Note: don't use `sum` to concatenate an array of strings - use `join` instead_

## round

Returns a number rounded to _ndigits_ precision after the decimal point. If _ndigits_ is omitted or
is `None`, it returns the nearest integer.

```python
round(5.2894) # 5
round(5.2894, 3) # 5.289
```

## zip

Makes an iterator that aggregates elements from each of the iterables. Returns an iterator of
tuples, where the 1st tuple is an aggregate of all the 1st elements, the 2nd tuple is an aggregate
from all the 2nd elements, etc.

It stops when the shortest input iterable is exhausted.

```python
first_zip = zip([1,2,3], [4,5,6])
list(first_zip) # [(1,4), (2, 5), (3, 6)]
dict(first_zip) # {1: 4, 2: 5, 3: 6}
```

You can also "unzip" iterators by using the `*` operator.

```python
five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
list(zip(*five_by_two)) # [(0,1,2,3,4), (1,2,3,4,5)]
```

### More complex `zip` examples

Use `zip` and `max` to find the highest value corresponding to a certain index (mapped to an
individual).

```python
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['Dan', 'Ang', 'Kate']

final_grades = {tup[0]:max(tup[1], tup[2]) for tup in zip(students, midterms, final)}
print(final_grades) # {'Dan': 98, 'Ang': 91, 'Kate': 78}
```

You can also get the same result by implementing `map` inside the `zip` function:

```python
scores = zip(
  students,
  map(
    lambda pair: max(pair),
    zip(midterms, finals)
  )
)

print(dict(scores)) # {'Dan': 98, 'Ang': 91, 'Kate': 78}
```
