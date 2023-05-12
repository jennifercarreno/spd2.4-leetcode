#LEETCODE QUESTION 31: NEXT PERMUTATION

'''
Given an array of integers nums, find the next permutation of nums.
example: 
input: nums = [1,2,3] -> [1,3,2]
'''
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
    
        #>right
        i = len(nums)-1
        # while the array is longer than 0 and the element before (to the left) nums[i] is bigger than nums[i]
        while i-1>=0 and nums[i-1]>=nums[i]:
            i -=1
            #set i to match the element on the right
    
        #>left

        if i-1>=0: #if there is another element to the left
            j = i
            while j<len(nums) and nums[j]>nums[i-1]:
            # while j<len(nums) and nums[j] > the element to the left
                j +=1 

            #swap the min-max number
            nums[i-1],nums[j-1] = nums[j-1],nums[i-1]
        m = i 
        n = len(nums)-1
        while m < n:
            nums[m],nums[n] = nums[n],nums[m]
            m +=1
            n -=1
            
'''
input: [1,2,3]
expected output: [1,3,2]

i = 2
2-1 > 0, not 2>3

j = 2
2 < 3 and 3 > 2
j = 3

nums[i-1] = nums[1] = 2
nums[j-1] = nums[2] = 3
2,3 = 3,2
new nums = [1,3,2]

'''