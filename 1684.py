class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        letters = list(allowed)
        count = 0
        for word in words:
            consistent = True
            for ch in word:
                if ch not in letters:
                    consistent = False
                    break
            if consistent == True:
                count += 1
        return count