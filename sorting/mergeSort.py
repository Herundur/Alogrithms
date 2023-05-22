def mergeSort(arr):
     if len(arr) > 1:
          left = arr[:len(arr)//2]
          right = arr[len(arr)//2:]

          mergeSort(left)
          mergeSort(right)

          i = 0 #current index of left array
          j = 0 #current index of right array
          k = 0 #current index of merged array
          while i < len(left) and j < len(left):
               if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
               else:
                    arr[k] = right[j]
                    j += 1
               k += 1

          while i < len(left):
               arr[k] = left[i]
               i += 1
               k += 1

          while j < len(right):
               arr[k] = right[j]
               j += 1
               k += 1

     
