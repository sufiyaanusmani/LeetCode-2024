class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        counts = []
        for sentence in sentences:
            s = sentence.split()
            counts.append(len(s))
        return max(counts)