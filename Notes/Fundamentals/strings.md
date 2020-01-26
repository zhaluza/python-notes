# Strings

_Note:_ strings can be wrapped with single or double quotes — just be consistent.

### Common Escape Characters

- `\\` = backslash (`\`)
- `\n` = new line
- `\'` = single quote (`'`)
- `\"` = doublt quote (`"`)

### Concatenation

As in JS, string concatenation is performed with the `+` operator.

However, strings **cannot** be concatenated with other types (unlike JavaScript).

The `+=` operator can also be used.

```python
str = 'ice'
str += ' cream'

print(str)
'ice cream'
```

### Interpolating Variables

The **F-String** is a way to include variable values in strings (the equivalent of **template literals** in JavaScript). It was introduced in Python 3.6.

```python
x = 10
formatted = f"I've told you {x} times already!"
```

You can also modify the values within the curly braces:

```python
x = 10
formatted = f"I've told you {x - 5} times already!"
```

**Older Way: `.format()`**
The older way of doing this is to use the `.format` method. It's notably clunkier.

```python
x = 10
formatted = "I've told you {} times already!".format(x)
```

### Accessing String Indices

You can access string elements by index. You can also use negative numbers to start counting backwards from the end!

```python
name = 'Sven'

print(name[0]) # S
print(name[-1]) #n
```
