# `is` vs `==`

In Python, `is` and `==` are very similar comparators. However, they are **not the same**.

```python
a = 1
a == 1 # True
a is 1 # True
```

```python
a = [1, 2, 3] # a list of numbers
b = [1, 2, 3]
a == b # True
a is b # False
```

`==` means that the things being compared have the **same value**.
`is` means that they are referring to the same item in the memory (e.g. the same object or the same variable).

**Note:** Both `==` and `is` will return truthy when referring to the same **number**. This is because they're both referring to an existing integer or float.
For strings, lists, etc., a new object is created in the memory, which is why `is` returns false.

```python
x = 13
y = 13

x == y # True
x is y # True
```
