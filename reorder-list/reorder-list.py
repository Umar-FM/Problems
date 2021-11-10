# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next: return
        
        #cut list in half
        fast,slow=head,head
        while fast.next:
            fast=fast.next
            if fast.next:fast=fast.next
            prev=slow
            slow=slow.next
        
        prev.next=None
        
        l1 = head
        l2 = slow
        
        #reverse second list
        prev=None
        curr=l2
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        l2=prev
                
        while l2:
            nxt= l1.next
            l1.next=l2
            l1=l2
            l2=nxt
        
        