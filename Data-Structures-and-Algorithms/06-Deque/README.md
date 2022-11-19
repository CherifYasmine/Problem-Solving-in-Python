# Deque

Doubly ended queue is the optimized list for quicker append and pop operations from both sides of the container. It provides O(1) time complexity for append and pop operations as compared to the list with O(n) time complexity.

Python Deque is implemented using doubly linked lists therefore the performance for randomly accessing the elements is O(n).

```python
# importing "collections" for deque operations
import collections
 
# initializing deque
de = collections.deque([1,2,3])
 
# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)
 
# printing modified deque
print("The deque after appending at right is : ")
print(de)
 
# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)
 
# printing modified deque
print("The deque after appending at left is : ")
print(de)
 
# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()
 
# printing modified deque
print("The deque after deleting from right is : ")
print(de)
 
# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()
 
# printing modified deque
print("The deque after deleting from left is : ")
print(de)
```

**Output**

```python
The deque after appending at right is : 
deque([1, 2, 3, 4])
The deque after appending at left is : 
deque([6, 1, 2, 3, 4])
The deque after deleting from right is : 
deque([6, 1, 2, 3])
The deque after deleting from left is : 
deque([1, 2, 3])
```