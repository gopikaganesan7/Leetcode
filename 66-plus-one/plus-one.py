class Solution(object):
    def plusOne(self, digits):
        num=0
        for i in digits:
            num*=10
            num+=i
        num=num+1
        list=[]
        while num>0:
            rem=num%10
            list.append(rem)
            num//=10
        new=list[::-1]
        return new

            
        