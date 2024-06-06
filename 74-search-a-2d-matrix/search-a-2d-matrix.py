class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            if i[len(i)-1]>=target:
                for j in i:
                    if target==j:
                        return True
        return False
        