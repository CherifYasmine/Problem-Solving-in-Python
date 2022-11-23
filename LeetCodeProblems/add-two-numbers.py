# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = l1
        head2 = l2
        s1 = ""
        s2 = ""
        while head is not None:
            s1 = str(head.val) + s1
            head = head.next
        while head2 is not None:
            s2 = str(head2.val) + s2
            head2 = head2.next
        news = str(int(s1)+int(s2))[::-1]
        lNew = ListNode(news[0])
        for i in range(1, len(news)):
            NewNode = ListNode(int(news[i]))
            laste = lNew
            while(laste.next):
                laste = laste.next
            laste.next=NewNode
        return(lNew)
            