class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n1 = len(candyType) / 2
        n2 = len(list(set(candyType)))
        return min(n1, n2)