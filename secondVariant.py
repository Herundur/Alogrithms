def maxSumSecondVariant(inputArray):

    maxSum = float('-inf')

    for element in inputArray:
        maxSum += element
        maxSum = max(element, maxSum)

    return maxSum

