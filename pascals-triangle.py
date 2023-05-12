'''
Given an integer numRows, return the first numRows of Pascal's triangle.

Example:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''

# psudocode:
# my first instinct is to make a loop for the number of rows
# make a prev list to hold previous values and a current list for current values 
# also need one main result list 

class Solution:
    def generate(self, numRows):
        # initialize the triangle with the first row
        triangle = [[1]]
        
        # generates a new row, i is the number of the row
        for i in range(1, numRows):
            # gets the previous row
            prev_row = triangle[-1]
            # makes a new row (always starts with 1)
            row = [1]

            # for number in the row number
            for j in range(1, i):
                # sum of the previous row value with the current row value
                row.append(prev_row[j-1] + prev_row[j])
            # end the row with 1 
            row.append(1)
            # add row to triangle
            triangle.append(row)
        
        return triangle
