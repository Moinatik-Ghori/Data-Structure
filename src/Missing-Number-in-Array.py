'''
Problem Description :

You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x.
You have to find x. The input array is not sorted.


Solution :

Find the sum sum_of_elements of all the numbers in the array.
Then find the sum expected_sum of first n numbers using the arithmetic series sum formula
The difference between these i.e. expected_sum - sum_of_elements, is the missing number in the array.

'''
def findMissingNumber(n,arr):
    # Getting the length of Array
    arrLen =  len(arr)

    # Runnig Partial Buttle sort to get the smallest number. Check Bubble sort for better understanding.
    for j in range(arrLen - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    smallestNumber = arr[arrLen-1]

    # Running While loop to calculate the Expected summation.
    num = n
    expectedSum = 0
    counting = smallestNumber
    while num > 0:
        num-=1
        expectedSum = expectedSum + counting
        counting+=1

    # Running For loop to count sum of given Array
    sumofArray = 0
    for j in arr:
        sumofArray = sumofArray + j

    print("Expected Sum ", expectedSum)
    print("Sum of Array ", sumofArray)

    # Missing numbe is difference between Expected sum and Sum of array.
    return expectedSum - sumofArray

if __name__ == "__main__":
    n = 9
    arr = [109, 101 , 106, 102 , 105, 108, 103, 104]
    number = findMissingNumber(n,arr)
    print("Missing Number is ",number)