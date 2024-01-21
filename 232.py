class Stack(object):
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        data = self.arr[len(self.arr) - 1]
        self.arr.pop()
        return data

    def peek(self):
        return self.arr[len(self.arr) - 1]

    def length(self):
        return len(self.arr)

class MyQueue(object):

    def __init__(self):
        self.mainStack = Stack()
        self.tempStack = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        n = self.mainStack.length()
        for _ in range(n):
            self.tempStack.push(self.mainStack.pop())
        self.mainStack.push(x)
        for _ in range(n):
            self.mainStack.push(self.tempStack.pop())

    def pop(self):
        """
        :rtype: int
        """
        data = self.mainStack.pop()
        return data

    def peek(self):
        """
        :rtype: int
        """
        return self.mainStack.peek()
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.mainStack.length() > 0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()