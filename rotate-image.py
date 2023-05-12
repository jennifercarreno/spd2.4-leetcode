#LEETCODE QUESTION 48: ROTATE IMAGE
"""
given: a matrix representing an image 
output: the matrix rotated by 90 degrees

example
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
#       length of first row in matrix
        n = len(matrix[0]) 
#       for i in range len of row
        for i in range(n // 2 + n % 2):
#           corners in each row
            for j in range(n // 2):
#               storing the last cell in the selected row
                tmp = matrix[n - 1 - j][i]
#               shifts the cells over 
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
#               sets the temporary cell as the first
                matrix[i][j] = tmp