class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) / 2
            if (nums[mid] == target):
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = left + 1
        return(-1)
        