class Solution(object):
    def isHappy(self, n):
        temp=n
        cnt=0
        while temp!=1 and cnt<20:
            cnt+=1
            add=0
            while temp>0:
                rem=temp%10
                temp=temp//10
                add+=(rem*rem)
            temp=add
        if temp==1:
            return True
        else:
            return False
        
        