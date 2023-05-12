'''
Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, return a list of all letter combinations they could have been trying to type on the keypad.
Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
'''

# pseudocode: 
# my first instinct is to organize the the digits by keypad position
# then iterate through the possible letters by their digits 

def t9_letters(digits):
    # Define a dictionary mapping each digit to its corresponding set of letters
    keypad = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    def letter_combinations(digits):
        if len(digits) == 0:
            return ['']
        else:
            # gets the first digit and sets it aside 
            first_digit = digits[0]

            # separates the rest of the digits 
            rest_of_digits = digits[1:]
            # calls the function again so that it separates the numbers one by one
            rest_of_combinations = letter_combinations(rest_of_digits)

            # make empty list for combinations 
            result = []

            # loops through the letters belonging to the first digit (ex. 2 -> a,b,c)
            for letter in keypad[first_digit]:
                # gets the rest of the digits and combines it with the first digit
                for combination in rest_of_combinations:
                    result.append(letter + combination)
            return result
    
    return letter_combinations(digits)
