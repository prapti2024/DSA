class Solution(object):
    def spiralOrder(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])

        rowbeg = 0
        colbeg = 0
        rowend = rows - 1
        colend = columns - 1

        ans = []

        while rowbeg <= rowend and colbeg <= colend:

            for i in range(colbeg, colend + 1):
                ans.append(matrix[rowbeg][i])
            rowbeg += 1

            for j in range(rowbeg, rowend + 1):
                ans.append(matrix[j][colend])
            colend -= 1

            if rowbeg <= rowend:
                for i in range(colend, colbeg - 1, -1):
                    ans.append(matrix[rowend][i])
                rowend -= 1

            if colbeg <= colend:
                for j in range(rowend, rowbeg - 1, -1):
                    ans.append(matrix[j][colbeg])
                colbeg += 1

        return ans