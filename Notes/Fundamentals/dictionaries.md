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
