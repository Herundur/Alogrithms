array = [1, -2, 3, -4, 4, 2, -3, 6, 2]
#array = [1, 0, 4, 2, 5, 6, 1, 12]

#
# MAXMUM SUM ALGORITHMS
#

from maxSum.firstVariant import maxSumFirstVariant
from maxSum.secondVariant import maxSumSecondVariant

#maxSumFirstVariant = firstVariant.maxSumFirstVariant(array)
#maxSumSecondVariant = secondVariant.maxSumSecondVariant(array)

#print(maxSumFirstVariant)
#print(maxSumSecondVariant)


#
# SORTING ALGORITHMS
#

from sorting.bubbleSort import bubbleSort
from sorting.selectionSort import selectionSort
from sorting.mergeSort import mergeSort

print("Unsorted Array: ",array)

#bubbleSort(array)
#selectionSort(array)
mergeSort(array)

print("Sorted Array: ",array)

#
# SEARCHING ALGORITHMS
#

from search.binarySearch import binarySearch
#print(binarySearch(array, 6))