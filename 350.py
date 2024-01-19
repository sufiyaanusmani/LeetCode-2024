class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        len1 = len(nums1)
        len2 = len(nums2)
        nums = []
        count = {}

        if len1 > len2:
            for num in nums1:
                if num in count.keys():
                    count[num] += 1
                else:
                    count[num] = 1
            for num in nums2:
                if num in count.keys() and count[num] > 0:
                    nums.append(num)
                    count[num] -= 1
        else:
            for num in nums2:
                if num in count.keys():
                    count[num] += 1
                else:
                    count[num] = 1
            for num in nums1:
                if num in count.keys() and count[num] > 0:
                    nums.append(num)
                    count[num] -= 1
        return nums
        