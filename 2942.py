class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        indexes = []
        for i in range(len(words)):
            if x in words[i]:
                indexes.append(i)
        return indexes
        class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        indexes = []
        for i in range(len(words)):
            if x in words[i]:
                indexes.append(i)
        return indexes
        