# Variables & Data Types

In Python, variables are declared directly.

```python
x = 100
y = 10
character = "Ash Williams"
```

They can be printed with the `print` command.

```python
print(x + y)
110
```

Variables can be:

- assigned to other variables
- reassigned at any time
- assigned at the same time as other variables

```python
python_is_awesome = 100
# the next line assigns the *value* of python_is_awesome to the new variable
just_another_var = python_is_awesome
python_is_awesome = 1337
all, at, once = 5, 10, 15
```

---

### Naming Restrictions & Conventions

**Restrictions:**

- Variables must start with a letter or underscore
- Rest of the name must consist of letters, numbers, or underscores
- Names are case-sensitive: cats != Cats

**Conventions:**

- Variables should be **snake_case** (underscores between words)
  - (Contrast with **camelCase** in JavaScript)
- _Most_ variables should be **lowercase**, with some exceptions
  - **CAPITAL_SNAKE_CASE** usually refers to **constants** (e.g. PI = 3.14)
  - **UpperCamelCase** usually refers to a **class**
  - Variables that **start and end with two underscores** (called "dunder" for double underscore) are supposed to be private or left alone (e.g. `__no_touchy__`)

---

## Data Types

Differences from JavaScript types are noted below:

- **Booleans** must start with _capital letters_ - `True`, `False`
- **Lists**: aka _arrays_ in JS
- **Dictionaries**: aka _objects_ in JS

### Dynamic Typing in Python

Python is highly flexible about reassigning variables to different types:

```python
awesomeness = True
print(awesomeness) # True

awesomeness = "a dog"
print(awesomeness) # a dog

awesomeness = None
print(awesomeness) # None

awesomeness = 22 // 7
print(awesomeness) # 3
```

This is known as **dynamic typing**, since variables can change types readily. In **statically typed** languages, variables are stuck with the type that's originally assigned to them.

---

### None

`None` is the equivalent of JavaScript's `null`.

---

## Converting Data Types

Data type conversion is fairly straightforward in Python.

- In **string interpolation**, data types are implicitly converted into string form.
- You can also **explicitly convert variables** by using the **name of the built-in type** as a function:

**Float to integer**

```python
decimal = 12.5783935
integer = int(decimal) #12
```

**List to string**

```python
my_list = [1, 2, 3]
my_list_as_string = str(my_list) # "[1, 2, 3]"
```

#### Note: Reserved Values

Because data type names are used to convert data types, they're also **reserved values**.

Don't make variables called `str`, `int`, `float`, etc.
