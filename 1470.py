class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        i = 0
        j = n
        l = []
        for _ in range(n):
            l.append(nums[i])
            l.append(nums[j])
            i += 1
            j += 1
        return l