class Solution(object):
    def searchRange(self, nums, target):
        l=[]
        if len(nums)==0 or target not in nums:
            return [-1,-1]
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    l.append(i)
        l=[l[0],l[-1]]
        return l
        