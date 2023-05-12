# LEETCODE QUESTION 78: SUBSETS

'''
given: list of numbers (nums)
output: all possible combinations

example:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
#           for new number introduced, make a new subset 
#           current number + [num + current number]
            output += [curr + [num] for curr in output]
#           existing output + current number + [existing output + current number]
        
        return output
    
'''
input: [1,2,3]

output = [[]]

first iteration:
num = 1
output = [[], [1]]

second iteration:
num = 2
output = [[], [1], [2], [1,2]]   adding the new num + the new num with each existing num

third iteration:
num = 3
output = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

'''