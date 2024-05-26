class Solution(object):
    def lengthOfLastWord(self, s):
        l=s.split()
        for i in range(len(l)):
            if i==len(l)-1:
                return len(l[i])
                

        