class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)
        l = [0, 0]

        for i in range(n):
            if nums1[i] in nums2:
                l[0] += 1

        for i in range(m):
            if nums2[i] in nums1:
                l[1] += 1

        return l