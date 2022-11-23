import string
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        d = dict.fromkeys(string.ascii_lowercase, 0)
        for c in sentence:
            d[c] = d[c]+1
        for k in d:
            if d[k] == 0:
                return False
        return(True)