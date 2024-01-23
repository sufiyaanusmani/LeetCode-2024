# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newNode = ListNode(data)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = LinkedList()
        temp1 = l1
        temp2 = l2
        remainder = 0
        while temp1 is not None and temp2 is not None:
            total = temp1.val + temp2.val + remainder
            if total <= 9:
                l.append(total)
                remainder = 0
            else:
                remainder = 1
                l.append(total % 10)
            temp1 = temp1.next
            temp2 = temp2.next
        
        if temp1 is not None:
            while temp1 is not None:
                total = temp1.val + remainder
                if total <= 9:
                    l.append(total)
                    remainder = 0
                else:
                    remainder = 1
                    l.append(total % 10)
                temp1 = temp1.next

        if temp2 is not None:
            while temp2 is not None:
                total = temp2.val + remainder
                if total <= 9:
                    l.append(total)
                    remainder = 0
                else:
                    remainder = 1
                    l.append(total % 10)
                temp2 = temp2.next

        if remainder > 0:
            l.append(remainder)

        return l.head