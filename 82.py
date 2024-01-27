# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        prev = None
        l = []
        while temp is not None:
            prev = temp
            temp = temp.next
            if temp is not None and prev is not None and prev.val == temp.val:
                l.append(temp.val)
                l = list(set(l))
                prev.next = temp.next
                temp = prev
        temp = head
        prev = None
        while head is not None and head.val in l:
            head = head.next
        while temp is not None:
            prev = temp
            temp = temp.next
            if temp is not None and temp.val in l:
                prev.next = temp.next
                temp = prev
        return head