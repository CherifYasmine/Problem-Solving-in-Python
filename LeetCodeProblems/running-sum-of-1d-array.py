class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        for i in range (0, len(nums)):
            if i == 0:
                l.append(nums[i])
            else:
                l.append(l[i-1] + nums[i])
        return(l)