class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range (0, len(s)):
            if(t.find(s[i]) != -1):
                t = t[t.find(s[i])+1:]
            else:
                return(False)
            
        return(True)
        