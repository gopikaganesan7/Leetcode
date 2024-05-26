class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1.insert(m+i,nums2[i])
            nums1.remove(0)
        for i in range(m+n):
            for j in range(i+1,m+n):
                if(nums1[j]<nums1[i]):
                    nums1[j],nums1[i]=nums1[i],nums1[j]

            

                    