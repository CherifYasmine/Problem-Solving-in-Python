class Solution(object):
    def containsDuplicate(self, nums):
        mySet = set(nums)
        print(mySet)
        return(not(len(mySet)==len(nums)))
        