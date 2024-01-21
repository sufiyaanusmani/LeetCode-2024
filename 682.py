class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        scores = []
        for operation in operations:
            if operation == "C":
                scores.pop()
            elif operation == "D":
                scores.append(scores[len(scores) - 1] * 2)
            elif operation == "+":
                scores.append(scores[len(scores) - 1] + scores[len(scores) - 2])
            else:
                scores.append(int(operation))

        return sum(scores)