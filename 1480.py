class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = [0 for num in nums]
        n = len(nums)
        for i in range(n):
            if i == 0:
                sums[0] = nums[0]
            else:
                sums[i] = nums[i] + sums[i-1]
        return sums