# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #Have 2 pointers, fast one n steps ahead of slow one. When fast one reaches end,
        # remove node at slow node
        dummy=ListNode()
        dummy.next=head
        fast=slow=dummy
        for i in range(n):
            fast=fast.next
            
        while fast.next:
            slow=slow.next
            fast=fast.next
        
        slow.next=slow.next.next
        return dummy.next