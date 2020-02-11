# Tuples

## What Is a Tuple?

A **tuple** is an ordered collection or grouping of items.

```python
numbers = (1, 2, 3, 4)
```

Conceptually, it's similar to a list. However, it uses a different syntax.

**Unlike a list, a tuple is immutable.**

Therefore, a tuple is an **unchanging way of storing ordered data**.

## Why Use Tuples?

- Tuples are **faster than lists**
- They can make your code **safer** (from bugs)
- They can be used as **valid dictionary keys**.

```python
locations = {
  (35.6895, 39.6917): "Tokyo Office"...
}
```

- Some methods return tuples to you, like `.items()` when working with dictionaries.

## Creating & Accessing Tuples

Create tuples using `()` or the `tuple()` function.

Access tuples with `[]`, just like lists.

```python
first_tuple = (1, 2, 3, 3, 3)

first_tuple[1] # 2
first_tuple[2] # 3
first_tuple[-1] # 3

second_tuple = tuple(5, 1, 2)

second_tuple[0] # 5
second_tuple[-1] #2
```

---

## Looping With Tuples

We can use `for` loops to iterate over tuples just like lists.

```python
names = ('Zac', 'Flavor', 'Brett')

for name in names:
  print(name)

# Zac
# Flavor'
# Brett
```

---

## Tuple Methods

#### `count`

Returns the number of times a value appears in a tuple.

```python
x = (1, 2, 3, 3, 3)

x.count(1) # 1
x.count(3) # 3
```

#### `index`

Returns the index at which a value is found in a tuple

```python
t = (1,2,3,3,3)

t.index(1) # 0
t.index(5) # ValueError: tuple.index(x): x not in tuple
t.index(3) # 2 (only the first matching index is returned)
```

#### Slices

Just like with arrays, you can **slice** lists

```python
nums = (1, 2, 3, (4, 5), 6, 7)

nums(0:)
# (1, 2, 3, (4, 5), 6, 7)

nums(0:4)
# (1, 2, 3, (4, 5))
```
