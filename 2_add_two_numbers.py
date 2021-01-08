# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        resCopy = res
        carry = 0

        while l1 or l2:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            _sum = val1 + val2 + carry
            if _sum > 9:
                carry = 1
                _sum = _sum - 10
            else: 
                carry = 0
            
            res.next = ListNode(_sum)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        if carry:
            res.next = ListNode(carry)
            
        return resCopy.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        resCopy = res
        carry = 0

        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, _sum = divmod(val1 + val2 + carry, 10)
            res.next = ListNode(_sum)
            res = res.next
            
        return resCopy.next