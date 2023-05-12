'''
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]
'''

def k_largest(a, k):
    # sort the array in reverse order, from largest to smallest 
    sorted_a = sorted(a, reverse=True)

    # make an empty list to hold the largest values 
    largest = []

    # loop through the array for k ammount of values 
    for i in range(0,k):
        # get an element from the sorted list and add it to the new list 
        largest.append(sorted_a[i])
    return largest