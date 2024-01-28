class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for operation in operations:
            if "++" in operation:
                x += 1
            elif "--" in operation:
                x -= 1
        return x