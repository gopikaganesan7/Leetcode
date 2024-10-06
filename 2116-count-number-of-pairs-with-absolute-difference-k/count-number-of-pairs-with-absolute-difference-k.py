class Solution(object):
    def countKDifference(self, nums, k):
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    l.append([i,j])
        return len(l)
