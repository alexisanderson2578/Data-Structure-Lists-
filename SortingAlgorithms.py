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

def merge_sort(list): #actual merge sort of a list
   if len(list) <= 1: #base case, once the elements have been broken into individual numbers it returns the list
       return list

   print("This is the original list: ", list)

   mid = len(list)//2 #this is where the list gets halved

   left_half = list[:mid]
   print("This is the left half of the list: ", left_half)

   right_half = list[mid:]
   print("This is the right half of the list: ", right_half)

   left_half = merge_sort(left_half) #recursive call to merge sort the left half

   right_half = merge_sort(right_half) #recursive call to merge sort the right half

   print(left_half) #this was put in to follow the process, can be deleted 
   print(right_half)#this was put in to follow the process, can be deleted

   return merge_sorted_lists(left_half, right_half) #calling the first function to merge and sort the first and second halves

list = [26, 54, 93, 17, 77, 31, 44, 55, 20]
print(merge_sort(list))

