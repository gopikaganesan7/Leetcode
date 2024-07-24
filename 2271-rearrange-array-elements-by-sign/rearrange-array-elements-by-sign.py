class Solution(object):
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        new=[]
        for j in nums:
            if j<0:
                neg.append(j)
            if j>0:
                pos.append(j)
        n=len(nums)/2
        for i in range(n):
            new.append(pos[i])
            new.append(neg[i])
        return new

        