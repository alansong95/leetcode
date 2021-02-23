# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        ret_copy = ret = ListNode()
        while True:
            if not l1 and not l2:
                break
            elif not l1:
                ret.next = ListNode(l2.val)
                l2 = l2.next
                ret = ret.next
            elif not l2:
                ret.next = ListNode(l1.val)
                l1 = l1.next
                ret = ret.next
            elif l1.val > l2.val:
                ret.next = ListNode(l2.val)
                l2 = l2.next
                ret = ret.next
            else:
                ret.next = ListNode(l1.val)
                l1 = l1.next
                ret = ret.next
        return ret_copy.next

    def printList(self, lst):
        if lst:
            print("[", end='')
            while (lst):
                print(str(lst.val) + ",", end='')
                lst = lst.next
            print("]")
        else:
            print("[]")

solution = Solution()
l1 = ListNode(1, ListNode(2, ListNode(4, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))

l12 = None
l22 = ListNode(0)

l13 = None
l23 = None

l14 = ListNode(5)
l24 = ListNode(1, ListNode(2, ListNode(4)))
print(solution.printList(solution.mergeTwoLists(l1, l2)))
print(solution.printList(solution.mergeTwoLists(l12, l22)))
print(solution.printList(solution.mergeTwoLists(l13, l23)))
print(solution.printList(solution.mergeTwoLists(l14, l24)))

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        