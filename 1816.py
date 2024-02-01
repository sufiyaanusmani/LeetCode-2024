class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = s.split()
        sentence = l[:k]
        return " ".join(sentence)