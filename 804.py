class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = {"a": ".-","b":"-...","c":"-.-.","d":"-..",'e':".",
                 "f": "..-.","g": "--.","h": "....","i": "..","j":".---",
                 "k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.",
                 "q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-",
                 "w":".--","x":"-..-","y":"-.--","z":"--.."}
        codes = []
        for word in words:
            s = ""
            for ch in word:
                s += morse[ch]
            if s not in codes:
                codes.append(s)
        return len(codes)
