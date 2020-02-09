# Dictionary Comprehension

## Explanation

#### Syntax

```python
{__:__ for __ in __}
```

- Iterates over keys by default
- To iterate over keys and values, use `.items()`

#### Examples

```python
numbers = {'first': 1, 'second': 2, 'third': 3}
squared_numbers = {key: value ** 2 for key,value in numbers.items()}
print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}
```

```python
{num: num**2 for num in [1,2,3,4,5]}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
str1 = 'ABC'
str2 = '123'
combo = {str1[i]: str2[i] for i in range (0, len(str1))}
print(combo) # {'A': '1', 'B': '2', 'C': '3'}
```

#### Conditional Logic

```python
num_list = [1,2,3,4]

{ num: ('even' if num % 2 == 0) }

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
```
