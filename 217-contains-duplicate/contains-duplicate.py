class Solution(object):
    def containsDuplicate(self, nums):
        k=set()
        for i in nums:
            if i in k:
                return True
            k.add(i)
        return False         