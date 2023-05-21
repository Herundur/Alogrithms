def bubbleSort(array):
    changes = -1
    while(changes != 0):
        i = 0
        currentChanges = 0
        while(i < len(array)):
            if(i + 1 >= len(array)):
                break
            if(array[i] > array[i + 1]):
                largerElement = array[i]
                smallerElement = array[i + 1]
                array[i + 1] = largerElement
                array[i] = smallerElement
                currentChanges += 1
            i += 1
        changes = currentChanges
    return array