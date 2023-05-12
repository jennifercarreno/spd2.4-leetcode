'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

# pseudocode:
# this is actually kind of simple, 
# we iterate through the list to find the min and max value 
# we first need to get the min value, then only look at values after the min
# find the max of the new array

def max_profit(prices):
    # if the len of prices is less than 2 then that means there's only one day 
    if len(prices) < 2:
        return 0

    # set the min and max to 0 by default
    min_price = 0
    max_profit = 0

    # saves the indexes (or day) of min/max
    buy = 0
    sell = 0

    # loops through aray to find min
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy == i
    
    # makes new array, grabs all items after the buy day
    new_array = prices[buy+1]

    # loops through the items in the days after and finds the max day index
    for i in range(len(new_array)):
        if new_array[i] > max_profit:
            max_profit = new_array[i]
            sell == i


    return sell
