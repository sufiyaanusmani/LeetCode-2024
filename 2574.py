class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = [0 for _ in range(n)]

        for i in range(n):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            l[i] = abs(left - right)
        return l
        