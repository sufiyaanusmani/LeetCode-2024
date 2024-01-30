class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        n = len(nums)
        for i in range(n):
            binary = bin(i)[2:]
            count = 0
            for ch in binary:
                if ch == "1":
                    count += 1
            if count == k:
                sum += nums[i]

        return sum