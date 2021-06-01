def InsertionSort(alist):
    for i in range(1,len(alist)):
        key = alist[i]
        currentvalue = i-1
        while (currentvalue > -1) and key < alist[currentvalue]: 
            alist[currentvalue+1]= alist[currentvalue] 
            currentvalue =currentvalue-1 
        alist[currentvalue+1] = key
    return alist

#bubblesort
arr = [63, 3, 5, 2, 122, 1, 9,67]
n = len(arr) 
for i in range(n):
    for j in range(0, n-i-1): 
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
print ("Sorted array is:")
print(arr)

def selectionListSort(selectedList):
    index = range(0,len(selectedList))
    for i in index:
        intMin = i
        for j in range(i+1 , len(selectedList)):
            if selectedList[j] < selectedList[intMin]:
                intMin = j
        if intMin != i:
            selectedList[intMin],selectedList[i]= selectedList[i],selectedList[intMin]
    return selectedList 

def merge_sorted_lists(list_1, list_2):
   output_list = []
   i = 0
   j = 0
   while i < len(list_1) and j < len(list_2):
       if list_1[i] < list_2[j]:
           output_list.append(list_1[i])
           i+=1
       else:
           output_list.append(list_2[j])
           j+=1
   return output_list + list_1[i:] + list_2[j:]

#list1 = [1, 3, 5]
#list2 = [2, 4, 6]
#print(merge_sorted_lists(list1, list2))

