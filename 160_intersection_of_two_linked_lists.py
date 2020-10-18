# # brute force
# # time: O(mn)
# # space: O(1)
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         ptrA = headA
#         ptrB = headB
#         while ptrA:
#             while ptrB:
#                 if ptrA == ptrB:
#                     return ptrA
#                 ptrB = ptrB.next
#             ptrA = ptrA.next
#             ptrB = headB
#         return None

# # iterate two times
# # time: O(m+n)
# # space: O(1)
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         # first iter: figure out the difference in length
#         ptrA = headA
#         ptrB = headB
        
#         while ptrA and ptrB:
#             ptrA = ptrA.next
#             ptrB = ptrB.next
            
#         diff_count = 0
#         while ptrA:
#             ptrA = ptrA.next
#             diff_count += 1
        
#         while ptrB:
#             ptrB = ptrB.next
#             diff_count -= 1
            
#         # second iter: figure out the answer
#         ptrA = headA
#         ptrB = headB
        
#         if diff_count > 0:
#             for i in range(diff_count):
#                 ptrA = ptrA.next
#         elif diff_count < 0:
#             for i in range(-1 * diff_count):
#                 ptrB = ptrB.next
                
#         while ptrA and ptrB:
#             if ptrA == ptrB:
#                 return ptrA
#             ptrA = ptrA.next
#             ptrB = ptrB.next
#         return None