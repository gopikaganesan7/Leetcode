class Solution(object):
    def setZeroes(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==0):
                    for k in range(m):
                        if matrix[i][k]!=0:
                            matrix[i][k]='*'
                    for g in range(n):
                        if matrix[g][j]!=0:
                            matrix[g][j]='*'
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='*':
                    matrix[i][j]=0
        return matrix


