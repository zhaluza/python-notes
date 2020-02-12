# Sets

Sets are like [formal mathematical sets](<https://en.wikipedia.org/wiki/Set_(mathematics)>).

- Sets don't have duplicate values.
- Elements in sets **aren't ordered**.
- You **can't access items in a set by index**.

Sets can be useful if you need to keep track of a collection of elements but don't care about ordering, keys, or values, and if you don't want duplicates.

#### Common Use Case for Sets

- Removing duplicates from a list with many duplicates
- Can then be converted back to a list

```python
cities = ['Los Angeles', 'Kyoto', 'New York', 'Kyoto', 'New York', 'New York']

cities_set = set(cities) # {'Los Angeles', 'Kyoto', 'New York'}

cities_distilled = list(cities) # ['Los Angeles', 'Kyoto', 'New York']
```

---

## Creating / Accessing

**Sets cannot have duplicates**

```python
s = set({1, 2, 3, 4, 5, 5, 5}) # (1, 2, 3, 4, 5)
```

**Creating a new set**

```python
s = set({1, 4, 5})
```

**Creating a new set**

```python
s = set({1, 4, 5})

# We could also use this method and get the same result
s = {1, 4, 5}
```

## Set Methods

#### `add`

**Adds an element to a set.** If the element is already in the set, the set doesn't change.

```python
s = set([1, 2, 3])
s.add(4)
s # {1, 2, 3, 4}
```

#### `remove`

**Removes a value from a set.** Returns a `KeyError` if the value isn't found.
_If you need to avoid a `KeyError`, use `discard()`._

```python
set1 = {1,2,3,4,5,6}

set1.remove(3)

print(set1) # {1, 2, 4, 5, 6}
```

#### `copy`

**Creates a copy of a set.**

```python
s = set([2,3,4])
another_s = s.copy()
another_s # {2, 3, 4}
another_s is s # False
```

#### `clear`

**Removes all contents of the set.**

```python
s = set([1,2,3])
s.clear()

s # set()
```

---

## Set Math

Sets also have many other mathematical methods.

- `intersection`
- `symmetric_difference`
- `union`
- And more...

#### `union` `|`

Combines two sets into a single one (without duplicates)
**Syntax**

```python
history_students = {'Kevin', 'Tina', 'Sharon', 'Tom'}
math_students = {'Tina', 'Sean', 'Geoff', 'Sharon'}
all_students = history_students | math_students
all_students # {'Kevin', 'Tina', 'Sharon', 'Tom', 'Sean', 'Geoff'}
```

#### `intersection` `&`

Returns all elements shared by two sets.

```python
history_students = {'Kevin', 'Tina', 'Sharon', 'Tom'}
math_students = {'Tina', 'Sean', 'Geoff', 'Sharon'}
shared_students = history_students | math_students
shared_students # {'Tina', 'Sharon'}
```
