# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        temp = head
        s = ""
        while temp is not None:
            s += str(temp.val)
            temp = temp.next
        return int(s, 2)
        