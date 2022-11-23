class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if(len(arr)==-1):
            return([-1])
        maxi = -1
        for i,a in reversed(list(enumerate(arr))):
            myMax = max(arr[i], maxi)
            arr[i] = maxi
            maxi = myMax
        return(arr)