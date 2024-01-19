class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = len(nums1)
        n2 = len(nums2)
        indexes = []
        ans = []
        for num in nums1:
            ans.append(-1)
            for i in range(n2):
                if num == nums2[i]:
                    indexes.append(i)
        
        for i in range(n1):
            for j in range(indexes[i] + 1, n2):
                if nums2[j] > nums1[i]:
                    ans[i] = nums2[j]
                    break
        return ans

