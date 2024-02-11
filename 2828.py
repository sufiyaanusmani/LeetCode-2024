class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        t = ""
        for word in words:
            t += word[0]
        return t == s