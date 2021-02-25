class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.last = None
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.last = x
        self.queue1.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        popped = None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        popped = self.queue1.pop(0)
        if self.queue2:
            self.last = self.queue2[-1]
        else:
            self.last = None
            
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return popped

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.last

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()