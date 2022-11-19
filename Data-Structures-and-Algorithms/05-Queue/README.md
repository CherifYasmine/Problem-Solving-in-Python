# Queue

We are familiar with queue in our day to day life as we wait for a service. The queue data structure aslo means the same where the data elements are arranged in a queue. The uniqueness of queue lies in the way items are added and removed. The items are allowed at on end but removed form the other end. So it is a First-in-First out method.

A queue can be implemented using python list where we can use the insert() and pop() methods to add and remove elements. Their is no insertion as data elements are always added at the end of the queue.

****Adding Elements****

```python
class Queue:
   def __init__(self):
      self.queue = list()

   def addtoq(self,dataval):
# Insert method to add element
   if dataval not in self.queue:
      self.queue.insert(0,dataval)
      return True
   return False

   def size(self):
      return len(self.queue)

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size()) >> 3
```

****Removing Element****

```python
def removefromq(self):
      if len(self.queue)>0:
         return self.queue.pop()
      return ("No elements in Queue!")
TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.removefromq()
```

```
Mon
Tue
```