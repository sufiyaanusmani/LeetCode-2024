class MyHashSet(object):

    def __init__(self):
        self.hash = []
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.hash:
            self.hash.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hash:
            self.hash.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.hash:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)