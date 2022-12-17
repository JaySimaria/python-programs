# 17-12-22
# selection sort
def selection_sort(array):
    #  loop from the beginning of the array to the second to last item
    currentIndex = 0
    while (currentIndex < len(array) - 1):
        #  save a copy of the currentIndex
        minIndex = currentIndex
        #  loop through all indexes that proceed the currentIndex
        i = currentIndex + 1
        while (i < len(array)):
            #    if the value of the index of the current loop is less
            #           than the value of the item at minIndex, update minIndex
            #           with the new lowest value index
            if (array[i] < array[minIndex]):
                # update minIndex with the new lowest value index
                minIndex = i
            i += 1
        # if minIndex has been updated, swap the values at minIndex and currentIndex
        if (minIndex != currentIndex):
            temp = array[currentIndex]
            array[currentIndex] = array[minIndex]
            array[minIndex] = temp
        currentIndex += 1

if __name__ == '__main__':
    array = [12, 11, 15, 10, 9, 1, 2, 3, 13, 14, 4, 5, 6, 7, 8]
    selection_sort(array)
    print(array)