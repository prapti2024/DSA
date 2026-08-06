class Solution(object):
    def rotate(self, matrix):
        rows = len(matrix)
        col = len(matrix[0])

        for i in range(rows):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for row in matrix:
            l = 0 
            r = col - 1
            
            while l < r:
                row[l],row[r] = row[r], row[l]
                l += 1
                r -= 1
        
        return(matrix)