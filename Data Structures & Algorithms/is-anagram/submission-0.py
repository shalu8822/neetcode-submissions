class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if len(s) != len(t):
            return False
        i,j=0,0
        res = True
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i +=1
                j+=1
            else:
                res = False
                break
        return res