class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        left = 0
        for i in range(0, len(nums)):
            if ((S - left - nums[i]) == left):
                return(i)
            left = left + nums[i]
        return -1
        