# one pass
# time: O(n)
# space: O(1)
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        if n == 1:
            slow.next = None
        else:
            slow.next = slow.next.next
        return dummy.next