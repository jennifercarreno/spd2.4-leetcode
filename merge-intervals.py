#LEETCODE QUESTION #56: MERGE INTERVALS

"""
given: an array of intervals where intervals[i] = [starti, endi]
output:return an array of the non-overlapping intervals, merge all overlapping intervalsthat cover all the intervals in the input.

example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: 
<-[1-[2-3]-4-5-6]-7-[8-9-10]-11-12-13-14-[15-16-17-18]->

constraints:
intervals[i].length == 2 (interval length is at least 2)
0 <= starti (all numbers are positive)

"""

class Solution:
    def merge(self, intervals):
#       sotrs the list of intervals by the first element
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            
#           merged[-1][1] = last element of previous interval
#           interval[0] = first of current interval

            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
#             max returns the biggest number
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
'''
input: intervals = [[1,5], [3,7], [9,10]]
output: intervals = [[1,7], [9,10]]

first iteration:
interval = [1,5]
 -- merged is empty, so just append
merged = [[1,5]]

second iteration:

interval = [3,7]
merged[-1][1] = 5 , interval[0] = 3 -> 5<3 -> False
 -- overlap bc second interval starts before first interval ends
max(5, 7) -> 7
merged[[1,7]] (last element of previous interval is replaced by the max number)

third iteration:
[9,10]
last element of previous interval: 7
interval[0]: 9
7 < 9 -> True
merged = [[1,7], [9,10]]


'''