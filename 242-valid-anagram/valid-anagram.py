class Solution(object):
    def isAnagram(self, s, t):
        k=0
        for i in s:
            if i not in t:
                return False
            if s.count(i)!=t.count(i): 
                return False
            if len(t)!=len(s):
                return False
        return True