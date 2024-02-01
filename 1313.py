class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        for i in range(0, n, 2):
            freq = nums[i]
            val = nums[i+1]
            ans.extend([val] * freq)

        return ans            