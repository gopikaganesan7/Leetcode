class Solution(object):
    def generate(self, numRows):
        main=[]
        if numRows>0:
            main.append([1])
        if numRows>1:
            main.append([1,1])
        if numRows>2:
            for i in range(3,numRows+1):
                new=[_ for _ in range(i)]
                new[0]=1
                new[-1]=1
                for k in range(1,len(new)-1):
                    new[k]=main[-1][k-1]+main[-1][k]
                main.append(new)
        return main