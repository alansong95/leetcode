class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        return ptr.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if not self.head:
            return self.addAtHead(val)
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
        elif index > 0 and index < self.size:
            node = Node(val)

            ptr = self.head
            for _ in range(index-1):
                ptr = ptr.next
            
            node.next = ptr.next
            ptr.next = node
            self.size += 1
        elif index == self.size:
            self.addAtTail(val)
        else:
            pass
        


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            pass
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
        elif index == self.size - 1:
            ptr = self.head
            while ptr.next.next:
                ptr = ptr.next
            ptr.next = None
            self.size -= 1
        else:
            ptr = self.head
            for _ in range(index-1):
                ptr = ptr.next
            
            if ptr.next:
                ptr.next = ptr.next.next
            else:
                ptr.next = None
            self.size -= 1
            
    
    def printList(self):
        ptr = self.head
        print('[', end='')
        while ptr:
            print(ptr.val, '->', end='')
            ptr = ptr.next
        print(']')


        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# Test case 0
# obj.addAtHead(0)

# obj.addAtTail(1)
# obj.addAtTail(2)

# obj.addAtIndex(-1, -99)
# obj.addAtIndex(4, -99)

# obj.addAtIndex(3, 3)
# obj.addAtIndex(2, 2.5)
# obj.addAtIndex(0, 0.1)
# obj.addAtHead(0.01)

# obj.printList()
# obj.deleteAtIndex(-1)
# obj.deleteAtIndex(7)

# obj.deleteAtIndex(3)
# obj.deleteAtIndex(0)
# obj.deleteAtIndex(obj.size-1)
# obj.printList()

# test case 1
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.printList()
# obj.addAtIndex(1,2)
# obj.printList()

# print(obj.get(1))
# obj.deleteAtIndex(1)
# print(obj.get(1))
# obj.printList()

# test case 2
obj.addAtTail(1)
obj.get(0)
obj.printList()

# ["MyLinkedList","addAtHead","get","addAtIndex","addAtIndex","deleteAtIndex","addAtHead","addAtHead","deleteAtIndex","addAtIndex","addAtHead","deleteAtIndex"]
# [[],[9],[1],[1,1],[1,7],[1],[7],[4],[1],[1,4],[2],[5]]

# ["MyLinkedList","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","addAtTail","addAtTail","deleteAtIndex","addAtHead","addAtHead","get","addAtTail","addAtHead","get","addAtTail","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","get","addAtIndex","addAtHead","get","addAtHead","deleteAtIndex","addAtHead","addAtTail","addAtTail","addAtIndex","addAtTail","addAtHead","get","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtHead","addAtTail","addAtHead","addAtHead","addAtTail","addAtTail","get","get","addAtHead","addAtTail","addAtTail","addAtTail","addAtIndex","get","addAtHead","addAtIndex","addAtHead","addAtTail","addAtTail","addAtIndex","deleteAtIndex","addAtIndex","addAtHead","addAtHead","deleteAtIndex","addAtTail","deleteAtIndex","addAtIndex","addAtTail","addAtHead","get","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","deleteAtIndex","get","get","addAtHead","get","addAtTail","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtTail","addAtTail","get","addAtIndex","addAtHead","deleteAtIndex","addAtTail","get","addAtHead","get","addAtHead","deleteAtIndex","get","addAtTail","addAtTail"]
# [[],[38],[66],[61],[76],[26],[37],[8],[5],[4],[45],[4],[85],[37],[5],[93],[10,23],[21],[52],[15],[47],[12],[6,24],[64],[4],[31],[6],[40],[17],[15],[19,2],[11],[86],[17],[55],[15],[14,95],[22],[66],[95],[8],[47],[23],[39],[30],[27],[0],[99],[45],[4],[9,11],[6],[81],[18,32],[20],[13],[42],[37,91],[36],[10,37],[96],[57],[20],[89],[18],[41,5],[23],[75],[7],[25,51],[48],[46],[29],[85],[82],[6],[38],[14],[1],[12],[42],[42],[83],[13],[14,20],[17,34],[36],[58],[2],[38],[33,59],[37],[15],[64],[56],[0],[40],[92],[63],[35],[62],[32]]