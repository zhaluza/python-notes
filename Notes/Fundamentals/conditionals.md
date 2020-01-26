# Conditionals

Python's conditional logic is more or less identical to JavaScript, Ruby, etc.

However, **it's extremely sensitive to white space**. Conditional statements must contain the proper spacing to work.

Remember to include the **colons** as well.

General conditional syntax (w/ pseudocode)

```python
if some condition is true:
  do something
elif some other condition is true:
  do something
else:
  do something
```

Real code:

```python
if name == "Kara Thrace":
  print("You are the harbinger of death")
elif name == "Gaius Baltar":
  print("No more Mister Nice Gaius")
else:
  print("So say we all")
```

Multiple `elif`s:

```python
color = input("What's your favorite color?")
if color == 'purple':
  print('excellent choice!')
elif color == 'teal':
  print('not bad!')
elif color == 'seafoam':
  print('mediocre!')
elif color == 'pure darkness':
  print('I like how you think')
else:
  print('YOU MONSTER!')
```

---

## Truthiness & Falsiness

Things that are naturally **falsy** in Python:

- Empty objects
- Empty strings
- `None`
- `0`

---

## Logical Operators

Python uses the following logical operators to make Boolean logic comparisons and statements: `and`, `or`, `not`.

Examples:

```python
if a and b:
  print(c)

if am_tired or is_bedtime:
  print('go to sleep')

if not is_weekend:
  print('go to work')
```
