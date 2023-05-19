def maxSumFirstVariant(inputArray):
    left = 0
    right = 0
    maxSum = float('-inf')
    length = len(inputArray)

    while(left < length):

        right = left
        currentSum = 0
        left += 1

        while(right < length):
            currentSum += inputArray[right]
            if currentSum > maxSum:
                maxSum = currentSum
            right += 1

    return maxSum
