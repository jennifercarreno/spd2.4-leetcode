#LEETCODE QUESTION 8: STRING TO INTEGER
'''
convert a string to a 32-bit integer

Read in and ignore any leading whitespace. : '__2'-> 2

Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present. : '-3' -> -3, '2' ->2


Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored. : '2a3' -> 2

Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.

Return the integer as the final result.


example: 
Input: s = "4193 with words"
Output: 4193

constraints: 
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
'''

class Solution:
    def myAtoi(self, input: str) -> int:
        sign = 1 
        result = 0
        index = 0
        n = len(input)
        
        INT_MAX = pow(2,31) - 1 
        INT_MIN = -pow(2,31)
        
        # Discard all spaces from the beginning of the input string.
        while index < n and input[index] == ' ':
            index += 1
        
        # sign = +1, if it's positive number, otherwise sign = -1. 
        
        if index < n and input[index] == '+':
            sign = 1
            index += 1
        elif index < n and input[index] == '-':
            sign = -1
            index += 1
        
        # Traverse next digits of input and stop if it is not a digit. 
        # End of string is also non-digit character.
        while index < n and input[index].isdigit():
            digit = int(input[index])
            
            # Check overflow and underflow conditions. 
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
                return INT_MAX if sign == 1 else INT_MIN
            
            # Append current digit to the result.
            result = 10 * result + digit
            index += 1
        
        # We have formed a valid number without any overflow/underflow.
        # Return it after multiplying it with its sign.
        return sign * result
    
'''
Input: s = "4193 with words"
Output: 4193

sign = 1
result = 0
index = 0
n = 15

first element:
input[index] : 4
4 != ''
index = 0

4 != +
index = 0
4 != -
index = 0

digit = 4
result = 10*0 + 4 -> 4
index = 1

next element:
input[index]: 1
1 != '', +, -

digit = 1
index = 2
result = 10*4 +1 -> 41

next: 
input[index]: 9 
9 != '', +,-

digit = 9
result = 10*41 +9 -> 419

next:
input[index]: 3
3 != ''
digit = 3
index = 3
result = 10*419 + 3 -> 4193

next:
input[index] : ''
'' == ''
index = 4
result = 4193

next:
input[index]: 'w'
'w' != '', +, -
'w' is not a digit
result = 1 * 4193 -> 4193
'''
    