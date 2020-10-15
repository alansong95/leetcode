class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow_pointer = head
        fast_pointer = head.next
        
        while fast_pointer and slow_pointer != fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            if fast_pointer:
                fast_pointer = fast_pointer.next
            else:
                return False
        if fast_pointer:
            return True
        else:
            return False
        