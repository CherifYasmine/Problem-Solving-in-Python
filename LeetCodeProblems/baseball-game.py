class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        myStack = []
        for a in operations:
            if(a=="C"):
                myStack.pop()
            elif(a=="D"):
                myStack.append(int(myStack[-1])*2)
            elif(a=="+"):
                last = int(myStack[-1])
                myStack.pop()
                new = last + int(myStack[-1])
                myStack.append(int(last))
                myStack.append(int(new))
            else:
                myStack.append(int(a))
        sum = 0
        while(myStack!=[]):
            sum = sum + myStack[-1]
            myStack.pop()
        return(sum)