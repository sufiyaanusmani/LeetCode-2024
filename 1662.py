class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        w1 = ""
        for ch in word1:
            w1 += ch
        w2 = ""
        for ch in word2:
            w2 += ch
        return w1 == w2