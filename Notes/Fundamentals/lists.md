# Lists

On a fundamental level, lists work like arrays do in Javascript. These are a few examples of lists:

```python
numList = [29, 449, 929]
stringList = ['hey', 'man', 'nice', 'shot']

var1 = 'hello'
var2 = 'world'
varList = [var1, var2]
```

---

## Accessing Values in a List

As in JavaScript, Python lists are zero-indexed, and individual elements can be accessed using brackets.

```python
friends = ['Tom', 'Jade', 'Savannah']
print(friends[1]) # 'Jade'
print(friends[3]) # IndexError
```

#### Accessing Values from the End

You can access values starting from the end of a list by using negative numbers.

```python
friends = ['Tom', 'Jade', 'Savannah']
print(friends[-1]) # 'Savannah'
print(friends[-2]) # 'Jade'
print(friends[-3]) # 'Tom'
```

#### Checking Whether a Value Is in a List

To see whether a value is in a list, use the following syntax: `value in list`. It will return a boolean.

```python
friends = ['Tom', 'Jade', 'Savannah']
'Jade' in friends # True
'Colt' in friends # False
```

---

## Iterating Through a List

You can iterate through a list in a few different ways:

#### `for...in` loop

```python
numbers = [1,2,3,4]
for number in numbers:
  print(number)

# 1
# 2
# 3
# 4
```

#### `while` loop

```python
numbers = [1,2,3,4]
i = 0
# len method - get length of argument
while i < len(numbers):
  print(numbers[i])
  i += 1

# 1
# 2
# 3
# 4
```

---

## List Methods

#### `len`: get length

```python
list = [10, 20, 30]
len(list) # 3
```

#### `list`: create a list

```python
list(range(1,5))
list # [1, 2, 3, 4, 5]

r = range(100)
list_2 = list(r)
list_2 #[0...99]
```

### `append`

Adds an item to the end of a list.

```python
list = [1,2,3,4]

list.append(5)

print(first_list) # [1,2,3,4,5]
```

### `extend`

Adds all values to the end of a list (i.e. concatenates them).

```python
list = [1,2,3,4]

list.extend([5,6,7,8])

print(list) # [1,2,3,4,5,6,7,8]
```

### `insert`

Inserts an item **at a given position**.

```python
list = [1, 2, 3, 4]

list.insert(2, 'Hi!')

print(list) # [1, 2, 'Hi!', 3, 4]

list.insert(-1, 'The end!')

# Since the '-1' index was originally list[4],
# 'The end!' will now be located at list[4]
print(list) # [1, 2, 'Hi!', 3, 'The end!', 4]

# to insert an element at the very end (w/o append)

list.insert(len(list), 'The actual end')

print(list) # [1, 2, 'Hi!', 3, 'The end!', 4, 'The actual end']
```
