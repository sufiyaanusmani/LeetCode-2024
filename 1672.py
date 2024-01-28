class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sums = []
        for account in accounts:
            sums.append(sum(account))
        return max(sums)
        