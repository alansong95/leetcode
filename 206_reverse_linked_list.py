# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head:
#             ptr = head
#             while ptr.next:
#                 temp = ptr.next
#                 ptr.next = temp.next
#                 temp.next = head
#                 head = temp
#             return head

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head or not head.next:
#             return head
#         h = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return h