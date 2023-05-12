'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

# pseudocode: strip the data of any spaces or symbols,reverse and compare

class Solution:
    def isPalindrome(self, s):

        # makes new var to put clean string
        clean_string = []

        # lowercase all letters
        lowercase = s.lower()

        # checks if the character is a digit, if not then add to clean string
        for character in lowercase:
            if not character.isdigit():
                clean_string.append(character)

        # join all elements in a string
        clean_string = ''.join(clean_string)

        # check if the string and the reversed string are the same
        if clean_string == clean_string[::-1]:
            return True
        return False


