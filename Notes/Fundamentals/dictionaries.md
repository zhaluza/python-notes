# Dictionaries

Lists are cool, but they only contain information without any details as to their greater context, or the relationships of the data they contain.

A **dictionary** provides this context. It's made up of **key-value pairs**.

```python
instructor = {
  "name": "Colt",
  "owns_dog": True,
  "num_courses": 4,
  "favorite_language": "Python",
  "is_hilarious": False,
  "fav_num": 44
}
```

Another way to create a dictionary in Python is to use the `dict` function:

```python
new_dictionary = dict(key = 'value')
new_dictionary # {'key': 'value'}
```

```python
cat2 = dict(name='BigBoi')
cat2 # {'name': 'BigBoi'}
```

## Accessing Values

To access a value, simply use bracket notation.

```python
cat = {
  'name': 'Blue',
  'breed': 'tabby',
  'cute': True
}

cat['name'] # 'Blue'
```

## Iterating Dictionaries

We can iterate through dictionaries using `for` loops.

There are three methods used to do this:

- `.keys()`
- `.values()`
- `.items()`

#### Accessing All Values in a Dictionary

Use `.values()`.

```python
instructor = {
  "name": "Colt",
  "owns_dog": True,
  "num_courses": 4,
  "favorite_language": "Python",
  "is_hilarious": False,
  "fav_num": 44
}
```

```python
for value in instructor.values():
  print(value)
# 'Colt'
# True
...
```

#### Accessing All Keys in a Dictionary

Use `.keys()`.

```python
instructor = {
  "name": "Colt",
  "owns_dog": True,
  "num_courses": 4,
  "favorite_language": "Python",
  "is_hilarious": False,
  "fav_num": 44
}
```

```python
for key in instructor.keys():
  print(key)
# name
# owns_dog
...
```

#### Accessing All Items & Keys in a Dictionary

Use `.items`

```python
instructor = {
  "name": "Colt",
  "owns_dog": True,
  "num_courses": 4,
  "favorite_language": "Python",
  "is_hilarious": False,
  "fav_num": 44
}
```

```python
for key,value in instructor.keys():
  print(key,value)
# name 'Colt'
# owns_dog True
...
```

## Using `in` to See If a Value Exists in a Dictionary

Given the following object:

```python
instructor = {
  "name": "Colt",
  "owns_dog": True,
  "num_courses": 4,
  "favorite_language": "Python",
  "is_hilarious": False,
  "fav_num": 44
}
```

Use `in` to see if a dictionary has a key:

```python
"name" in instructor # True
"awesome" in instructor # False
```

Use `in` and `values()` to see if a dictionary contains a value.

```python
"Colt" in instructor.values() # True
"Nope!" in instructor.values() # False
```

## Dictionary Methods

#### `clear`

Clears all the keys and values in a dictionary, leaving only an empty dictionary.

```python
dict = {'a': 1, 'b': 2, 'c': 3}
dict.clear()
dict # {}
```

#### `copy`

Makes a copy of a dictionary (not a reference)

```python
dict = {'a': 1, 'b': 2, 'c': 3}
dict_copy = dict.copy()
dict_copy # {'a': 1, 'b': 2, 'c': 3}
dict_copy is dict # False
```

#### `fromkeys`

Creates key-value pairs from comma-separated values:

```python
{}.fromkeys('a','b') # {'a': 'b'}
{}.fromkeys('email','unknown') # {'email': 'unknown'}
{}.fromkeys('a',[1,2,3,4,5]) # {'a': [1, 2, 3, 4, 5]}
```

Can also be used to create default dictionaries by inputting an array of key values:

```python
{}.fromkeys(['name', 'location', 'age', 'job'], 'unknown')
# {'name': 'unknown', 'location': 'unknown', 'age': 'unknown', 'job': 'unknown'}
```

#### `get`

Retrieves a key in an object and returns None instead of a KeyError if the key doesn't exist.

```python
d = {'a': 1, 'b': 2, 'c': 3}
d['a'] # 1
d.get('a') #1
d['b'] # 1
d.get('b') #1
d['no_key'] # KeyError
d.get('no_key') # None
```
