def selectionSort(array):
    i = 0
    c = 0
    while(i < len(array)):
        c = i
        smallest = array[i]
        smallestIndex = i
        while(c < len(array)):
            if(smallest > array[c]):
                smallestIndex = c
                smallest = array[c] 
            c += 1
        array[i], array[smallestIndex] = array[smallestIndex], array[i]
        i += 1
    return array