class Solution(object):
    def maximumGap(self, nums):
        if(len(nums)<2):
            return 0
        nums=sorted(nums)
        max=-99999
        for i in range(1,len(nums)):
            diff=nums[i]-nums[i-1]
            if diff>max:
                max=diff
        return max
        