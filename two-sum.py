# # #
# Given a sorted array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# # #

# my notes/thought process 
# if the array is sorted from smallest to biggest, then we only need to check the ints smaller than the target
# we can keep adding the smallest numbers together until we get a sum
# example:
# input nums = [1,3,4,6,7] target = 10
# 1 + 3 != 10, increase (or move up) by 1 
# 3 + 4 != 10, i+1
# 4 + 6 = 10 , return 4 and 6 

def twoSum(nums, target):
    print(nums)
    for i in range(len(nums)): 
        if nums[i] < target: 
            a = nums[i]
            b = nums[i + 1]
            if (a + b) == target:
                print(nums[i], nums[i+1])
                return [nums[i], nums[i +1]]
        else: 
            return
            

twoSum([2,4,9], 6)