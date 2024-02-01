class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        target = [-1 for _ in range(n)]

        for i in range(n):
            if target[index[i]] == -1:
                target[index[i]] = nums[i]
            else:
                target.insert(index[i], nums[i])
                target.pop()

        return target