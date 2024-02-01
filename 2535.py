class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elementSum = sum(nums)
        digitSum = 0
        for num in nums:
            s = str(num)
            for ch in s:
                digitSum += int(ch)
        return abs(elementSum - digitSum)