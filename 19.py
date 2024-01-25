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

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        totalNodes = self.length(head)
        if n == 1 and head.next is None:
            return None
        c = totalNodes - n
        if c == 0:
            head = head.next
            return head
        i = 1
        prev = None
        temp = head
        while i < c:
            i += 1
            prev = temp
            temp = temp.next
        if temp.next is None:
            prev.next = None
        else:
            temp.next = temp.next.next
        return head