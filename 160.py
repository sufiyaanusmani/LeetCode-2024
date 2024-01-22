# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1 = 0
        len2 = 0
        temp = headA
        while temp is not None:
            len1 += 1
            temp = temp.next
        temp = headB
        while temp is not None:
            len2 += 1
            temp = temp.next
        difference = abs(len1 - len2)
        temp1 = headA
        temp2 = headB
        if difference > 0:
            if len1 > len2:
                for _ in range(difference):
                    temp1 = temp1.next
            else:
                for _ in range(difference):
                    temp2 = temp2.next
        
        while temp1 is not None:
            if temp1 is temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        return None