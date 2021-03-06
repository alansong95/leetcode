class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        popped = None
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            popped = self.stack2.pop()
            if self.stack2:
                while self.stack2:
                    self.stack1.append(self.stack2.pop())
        return popped
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        peek = None
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            peek = self.stack2[-1]
            if self.stack2:
                while self.stack2:
                    self.stack1.append(self.stack2.pop())
        return peek

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.first = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if self.first is None:
            self.first = x
        self.stack1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        popped = None
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            popped = self.stack2.pop()
            if self.stack2:
                self.first = self.stack2[-1]
                while self.stack2:
                    self.stack1.append(self.stack2.pop())
            else:
                self.first = None
        return popped
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.first
    
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()