class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s = ""
        for ch in sentence:
            if ch not in s:
                s += ch
        return len(s) == 26