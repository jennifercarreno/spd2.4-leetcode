# LEETCODE QUESTION 821: SHORTEST DISTANCE TO A CHARACTER

'''
given: string and a character (string)
output: array with numbers representing distance to c
Input: s = "loveleetcode", c = "e"

EXAMPLE:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

'''


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
             
        prev = float('-inf')

        # array that will get returned
        ans = []

        # forward search (left to right)
        # iterates through each charater in string
        for i, x in enumerate(S):

                # checks if x is the character we're looking for and setting prev to 0
                if x == C: prev = i
                # appends distance to first array
                ans.append(i - prev)

        prev = float('inf')

        # length of sting in an array but backwards (backwards search, right to left)
        for i in xrange(len(S) - 1, -1, -1):
                # checks if x is character
                if S[i] == C: prev = i
                # compares previous distance to current and sees which is less, replaces distance if less
                ans[i] = min(ans[i], prev - i)
        # returns list of smallest distances
        return ans