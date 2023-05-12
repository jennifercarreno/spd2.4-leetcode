# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

# pseudocode:
# my first thought is to sort the arrays
# once the arrays are sorted we can add the largest and smallest values together
# we should keep track of the sums, similar to a function that checks for the largest number 
# so the process would be, a+b = c, next round of addition and then if c > c2, c is the closest sum


def array_sum(a,b,t):
    a.sort()
    # print(a)
    # print(b.sort())
    b.sort()
    

    # pointer variables, one at the largest, one at the smallest
    i = 0
    j = len(b) - 1

    # keeping track of sums 
    current_sum = 0
    closest_sum = []

    while i < len(a) - 1 and j >= 0:
        current_sum = a[i] + b[j]
        if closest_sum:
            if abs(t-current_sum) < (closest_sum[0] + closest_sum[1]):
                closest_sum = [a[i], b[j]]
            if current_sum < t:
                i+=1
            else:
                j-=1
    return closest_sum
    
a= [9, 13, 1, 8, 12, 4, 0, 5]
b= [3, 17, 4, 14, 6]
array_sum(a, b, 20)