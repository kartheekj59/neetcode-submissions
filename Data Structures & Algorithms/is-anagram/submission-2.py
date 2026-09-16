from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counterS = Counter(s)
        counterT = Counter(t)
        for k,v in counterS.items():
            if counterT.get(k,0) != v:
                return False
            del counterT[k]
        return True if len(counterT) ==0 else False
        