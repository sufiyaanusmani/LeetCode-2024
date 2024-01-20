class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []

        for word in words:
            for i in range(len(rows)):
                if word[0].lower() in rows[i]:
                    rowNum = i
                    break
            flag = True
            for ch in word.lower():
                if ch not in rows[i]:
                    flag = False
            if flag == True:
                ans.append(word)
        return ans
        