class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #n = len(matrix)
        m,n = len(matrix),len(matrix[0])
        r,c = 0,n-1
        while r<m and c>=0:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                r+=1
            else:
                c-=1
        return False

        #Brute Force
        '''for row in matrix:
            for ele in row:
                if ele == target:
                    return True
        return False'''

        