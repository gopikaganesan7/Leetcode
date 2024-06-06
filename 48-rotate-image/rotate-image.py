class Solution(object):
    def rotate(self, matrix):
        temp=[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                temp[i][j]=matrix[j][i]
        cnt=0
        for i in temp:
            matrix[cnt]=i[::-1]
            cnt+=1
        return matrix
