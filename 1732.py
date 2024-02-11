class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes = [0]
        n = len(gain)
        for i in range(n):
            altitudes.append(altitudes[i] + gain[i])
        return max(altitudes)