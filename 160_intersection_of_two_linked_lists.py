class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptrA = headA
        ptrB = headB
        while ptrA:
            while ptrB:
                if ptrA == ptrB:
                    return ptrA
                ptrB = ptrB.next
            ptrA = ptrA.next
            ptrB = headB
        return None

