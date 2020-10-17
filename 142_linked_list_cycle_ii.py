# using hash set
# time: O(n)
# space: O(n)
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        
        node = head
        while node != None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None
        
# two pointers
# time: O(n)
# space: O(1)
class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None