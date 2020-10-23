# time: O(n)
# space: O(n)
# class Solution(object):
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         vals = []
#         curr = head
#         while curr:
#             vals.append(curr.val)
#             curr = curr.next
#         return vals == vals[::-1] 

# time: O(n)
# space: O(1)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        
        # find the end of the first half
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        second_head = self.reverseList(slow.next)
    
        while second_head:
            if head.val != second_head.val:
                return False
            head = head.next
            second_head = second_head.next
        return True
    
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        return prev