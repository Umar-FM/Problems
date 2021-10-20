# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow=head
        fast=head
        if not head or not head.next: return False
        while slow or fast:
            
            if slow:slow=slow.next
            if fast: 
                fast=fast.next
                if fast:fast=fast.next
            if not fast: return False
            if slow==fast: return True
        return False