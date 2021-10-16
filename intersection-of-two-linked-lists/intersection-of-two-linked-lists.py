# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        lA = 0
        lB = 0
        
        while pA:
            if not pA.next: tailA = pA
            pA = pA.next
            lA +=1
            
        while pB:
            if not pB.next: tailB = pB
            pB = pB.next 
            lB +=1
            
        if pA != pB: return None
        
        delta = abs(lA-lB)
        
        pA = headA
        pB = headB
        
        if lA>lB:
            for i in range(delta):
                pA=pA.next
        else:
            for i in range(delta):
                pB=pB.next
        
        while pA != pB:
            pA=pA.next
            pB=pB.next
            
        return pA
            