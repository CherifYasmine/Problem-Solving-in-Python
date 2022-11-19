# Set

unordered collection of data that is mutable and does not allow any duplicate element. Sets are basically used to include membership testing and eliminating duplicate entries. The data structure used in this is Hashing, a popular technique to perform insertion, deletion, and traversal in O(1) on average.

```python
# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(Set)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in Set:
	print(i, end =" ")
print()

# Checking the element
# using in keyword
print("Geeks" in Set)
```

Output

```python
Set with the use of Mixed Values
{1, 2, 'Geeks', 4, 6, 'For'}

Elements of set:
1 2 Geeks 4 6 For
True
```

****Adding Items to a Set****

```python
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])

Days.add("Sun")
print(Days)
```

Output

`set(['Wed', 'Sun', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])`

****Removing Item from a Set****

```python
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])

Days.discard("Sun")
print(Days)
```