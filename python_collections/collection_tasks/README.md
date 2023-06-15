# Collections
There are 4 main types of collections in Python. This allows to store multiple data.

### Lists
List is a collection of data that is mutable and ordered. A list can store multiple data types such as strings, integers or a list.

**Create a list**
```python
shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]
print(type(shopping_list))
print(shopping_list)
```
**Indexing and Slicing**
```python
shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]
print(shopping_list[0])
print(shopping_list[1:3])

# change a specific element of my list
shopping_list[-1] = "orange juice"
print(shopping_list)
```
**List Methods**
```python
shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]
shopping_list.append("butter")
print(shopping_list[-1])

shopping_list.remove("butter")
print(shopping_list)

shopping_list.pop()
print(shopping_list)
```
**Mixed data type**
```python
mixture = [1, 2, 3, "one", "two", "three"]
print(mixture[:-1:2])
```
### Tuples
Tuple is a collection of data that is immutable and ordered.
```python
essential = ("bread", "eggs", "milk")
print(essential)

```
### Dictionaries
Dictionary is a collection of data that is mutable and unordered. Also, keys have to be unique.
```python
student_1 = {
    "name": "luke",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "git", "data_types", "collections"]
}
print(student_1)
print(type(student_1))

# Accessing parts of a dictionary
print(student_1["name"])
print(student_1["completed_lesson_names"][0])

# Changing values
student_1["completed_lessons"] = 3
print(student_1)

student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])
```
**Dictionary Methods**
```python
student_1 = {
    "name": "luke",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "git", "data_types", "collections"]
}
print(student_1.keys())
print(student_1.values())
print(student_1.items())
```
### Sets
Set is a collection of data that is mutable and unordered. Also, you cannot have a duplicate data in a set.
```python
car_parts = {"wheels", "windows", "exhaust", "steering wheel"}
print(car_parts)

# add to sets
car_parts.add("doors")
print(car_parts)

car_parts.remove("doors")
print(car_parts)
```
#### Frozen set
A set that is immutable
```python
x = frozenset([1, 2, 4, 5, 7, 8, 9])
print(x)

```
