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
        

