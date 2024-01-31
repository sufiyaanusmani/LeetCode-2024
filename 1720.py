class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        n = len(encoded)
        l = [0 for _ in range(n+1)]
        l[0] = first
        for i in range(n):
            l[i+1] = encoded[i] ^ l[i]
        return l