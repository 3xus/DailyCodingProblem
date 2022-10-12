#Problem 01 by Google

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

# lst_num = [10,15,3,7,28,10,15]
# k = 30

def SumNumbers(lst_num, k):
    for i in range(0,len(lst_num)):
        for j in range(0,len(lst_num)):
            if i != j and k == lst_num[i]+lst_num[j]:
                return True
    return False

# SumNumbers(lst_num, k)

