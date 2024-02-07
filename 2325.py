class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        keys = key.replace(" ", "")
        a = ""
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        cipher = {}
        i = 0
        j = 0
        while i < 26:
            key = str(keys[j])
            if key not in cipher.keys():
                cipher[key] = alphabets[i]
                i += 1
            j += 1

        secret = ""
        for ch in message:
            if ch == " ":
                secret += " "
            else:
                secret += cipher[str(ch)]
        return secret