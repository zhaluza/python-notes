# Integers & Floats

**Integers** refer to whole numbers, such as 23, 492, and -1.

**Floating points** refer to numbers with decimals - 6.1, 1.3333, etc.

Floating point numbers (aka _floats_) potentially take up much more space in Python.

You can use the function `type()` to discern between ints, floats, etc.

```python
>>> type(1.9)
<class 'float'>
>>> type(2)
<class 'int'>
```

## Integer Division

When you divide using `/` in Python, the result will **always** be a float.

```python
>>> 10 / 2
5.0
```

`//` is the **integer division** symbol. It will "floor" your solution and round down.

```python
>>> 10//3
3
```
