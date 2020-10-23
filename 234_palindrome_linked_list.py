# time: O(n)
# space: O(n)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals == vals[::-1] 