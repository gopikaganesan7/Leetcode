class Solution(object):
    def reverse(self, x):
        flag=0
        max=2**31
        if x<0:
            flag=1
        temp=abs(x)
        rev=0
        while temp>0:
            rem=temp%10
            rev=(rev*10)+rem
            temp=temp//10
        if flag==1:
            rev=-abs(rev)
        if rev>max-1 or rev< -abs(max):
            return 0
        return rev
        
        