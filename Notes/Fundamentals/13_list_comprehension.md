# List Comprehension

List comprehension lets you iterate through the elements of a list and perform certain actions on them.

It uses the following syntax:
```python
[action for element in list]
```

For example: 
```python
nums = [1,2,3,4,5]
[x * 10 for x in nums]
# [10, 20, 30, 40, 50]
```

## List Comprehension vs. Loops

While we could do the same thing with a regular loop, the list comprehension syntax makes our code much more concise.

**`for` loop:**
```python
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
  doubled_number = num * 2
  doubled_numbers.append(doubled_number)

print(doubled_numbers) # [2, 4, 6, 8, 10]
```

**List comprehension:**
```python
numbers = [1, 2, 3, 4, 5]

doubled_number = [num * 2 for num in numbers]

print(doubled_numbers) # [2, 4, 6, 8, 10]
```

## More List Comprehension Examples
```python
name = 'zac'

[char.upper() for char in name] # ['Z', 'A', 'C']
```

```python
friends = ['ashley', 'matt', 'michael']

[friend[0].upper() for friend in friends] # ['Ashley', 'Matt', 'Michael']
```

```python
[num * 10 for num in range(1, 6)]
# [10, 20, 30, 40, 50]
```

It's helpful for data conversion:
```python
numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list) # ['1', '2', '3', '4', '5']
```

## List Comprehension With Conditional Logic
To introduce conditional logic into list comprehension in Python, you simply expand the syntax described above:
```python
# Plain 'if' statement
[action for element in list if condition]

# 'if/else' statement
[action if condition else action for element in list]
```

The following example will sort the numbers in a list into two separate lists, `evens` and `odds`.
```python
numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]

odds = [num for num in numbers if num % 2 != 0]
```

The next line will multiply all even elements by 2 and divide all odd elements by 2:
```python
[num*2 if num % 2 == 0 else num/2 for num in numbers]
# [0.5, 5, 1.5, 8, 2.5, 12]
```

This one's a little trickier. It will iterate through the string and append everything but the vowels to an empty string.
```python
with_vowels = 'This is so much fun!'

''.join(char for char in with_vowels if char not in 'aeiou')

# 'This s s mch fn!'
```