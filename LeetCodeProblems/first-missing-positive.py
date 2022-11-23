class Solution(object):
    def firstMissingPositive(self, nums):
        a = set(nums)
        for i in range(1, len(nums)+2):
            if i not in a:
                return i
        