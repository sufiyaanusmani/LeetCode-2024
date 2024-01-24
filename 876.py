# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def length(self, head):
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = self.length(head)
        temp = head
        i = 1
        while i <= count // 2:
            temp = temp.next
            i += 1
        return temp