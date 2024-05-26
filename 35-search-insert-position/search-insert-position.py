class Solution(object):
    def searchInsert(self, nums, target):
        index=0
        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if i<target:
                    index+=1
            return index
            
        