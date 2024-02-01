class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        for item in items:
            product = {"type": item[0], "color": item[1], "name": item[2]}
            if product[ruleKey] == ruleValue:
                count += 1

        return count