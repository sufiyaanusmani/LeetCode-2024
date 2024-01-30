class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = [0 for num in nums]

        for i in range(n):
            for j in range(n):
                if i != j and nums[i] > nums[j]:
                    l[i] += 1
        return l