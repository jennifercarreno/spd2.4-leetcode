# LEETCODE QUESTION 169: MAJORITY ELEMENT

"""
given: array of numbers 
output: which number shows up the most

EXAMPLE:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        #  sort the array
#       iterates over array
        for num in nums:
#           counts how many times the number shows up in the array

#                   every time elem == num, add 1 to count
            count = sum(1 for elem in nums if elem == num)
#                   for elem in nums
#                       if elem == num
#                           sum +=1
#                           count = sum

#           if the count is more than half of the length of the array, it's the majority
            if count > majority_count:
                return num

# sorted array: [2,2,2,4,5]
# check if 0 element == majority count element 
# 





        
"""
Input: nums = [2,2,4,2,5]
Output: 2

majority count = 5//2 -> 2

FIRST ITERATION:
num = 2

elem = 2
sum = 1

elem = 2
sum = 2

elem = 4
sum = 2

elem = 2
sum = 3

elem = 5
sum = 3

count = 3

3>2 -> return num

"""

"""
Input: nums [3, 4, 5, 4, 4]
Output: 4

Majority count = 5 // 2 -> 2

FIRST ITERATION:
num = 3

elem = 3
sum = 1

elem = 4
sum = 1

elem = 5
sum = 1

elem = 4
sum = 1

elem = 4
sum = 1

count = 1

1<2 -> next num

SECOND ITERATION:
num = 4

elem = 3
sum = 0

elem = 4
sum = 1

elem = 5
sum = 1

elem = 4
sum = 2

elem = 4
sum = 3

count = 3

3 > 2 -> return 4
"""