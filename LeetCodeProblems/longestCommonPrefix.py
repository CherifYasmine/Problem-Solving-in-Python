class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)==0):
            return ""
        longest = strs[0]
        for i in range (1, len(strs)):
            while not(strs[i].startswith(longest)):
                    longest = longest[:-1]
                    print(longest)
        return(longest)