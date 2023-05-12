
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in


def sum(num1, num2):

    
    if num1.isdigit() == False or num2.isdigit() == False:
        if '.' in num2 or '.' in num1:
            dnum1 = num1.replace('.','')
            dnum2 = num2.replace('.', '')

            if dnum1.isdigit() == False or dnum2.isdigit() == False:
                print('not a digit')
                return ('not a digit')
            else:
                num1 = eval(num1)
                num2 = eval(num2)

    
    sum = num1 + num2
    print(sum)
    return str(sum)

sum('200.2', '2.3')