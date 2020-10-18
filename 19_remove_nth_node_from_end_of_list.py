# # one pass
# # time: O(n)
# # space: O(1)
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         dummy = ListNode(0)
#         dummy.next = head
        
#         slow = dummy
#         fast = dummy
        
#         for _ in range(n+1):
#             fast = fast.next
        
#         while fast:
#             fast = fast.next
#             slow = slow.next
        
#         if n == 1:
#             slow.next = None
#         else:
#             slow.next = slow.next.next
#         return dummy.next

# # two passes
# # time: O(n)
# # space: O(1)
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         dummy = ListNode(0)
#         dummy.next = head
        
#         ptr = head
        
#         length = 0
#         while ptr:
#             ptr = ptr.next
#             length += 1
        
#         ptr = dummy
#         for _ in range(length-n):
#             ptr = ptr.next
        
#         if n == 1:
#             ptr.next = None
#         else:
#             ptr.next = ptr.next.next
            
#         return dummy.next