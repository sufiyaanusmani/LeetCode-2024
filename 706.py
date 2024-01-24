class MyHashMap(object):

    def __init__(self):
        self.map = [-1 for i in range(int(1e6) + 7)]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key < 10000000 + 7:
            self.map[key] = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key < 10000000 + 7:
            return self.map[key]
        else:
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key < 1000000 + 7:
            self.map[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)