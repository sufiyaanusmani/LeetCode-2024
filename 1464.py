class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num = -1

        for i in range(n):
            for j in range(i+1, n):
                prod = (nums[i] - 1) * (nums[j] - 1)
                if prod > num:
                    num = prod

        return num