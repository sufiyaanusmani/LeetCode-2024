class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if i < j and j < k:
                        if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                            count += 1

        return count