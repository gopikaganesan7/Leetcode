class Solution(object):
    def isPowerOfTwo(self, n):
        flag=0
        if n==1 or n==2:
            return True
        else:
            a=1
            for i in range(2,32):
                for j in range(1,i+1):
                    a=a*2
                    if a==n:
                        flag=1
                        break
        if flag==0:
            return False
        else:
            return True
                    