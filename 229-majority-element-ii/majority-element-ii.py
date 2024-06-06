class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)//3
        l=set()
        for i in nums:
            if nums.count(i)>n:
                l.add(i)
        li=list(l)
        return li
        

        