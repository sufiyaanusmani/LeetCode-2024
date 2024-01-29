class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandies = max(candies)
        l = []

        for candy in candies:
            if candy + extraCandies >= maxCandies:
                l.append(True)
            else:
                l.append(False)
        return l