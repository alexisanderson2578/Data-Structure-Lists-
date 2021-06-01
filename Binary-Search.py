def rec_list(sorted_list, lower, upper, item):
    if upper >= lower:
        midpoint = (lower + upper) // 2
        if sorted_list[midpoint] == item:
            return True
        elif sorted_list[midpoint] > item:
            return rec_list(sorted_list,lower, midpoint -1, item)
        else:
            return rec_list(sorted_list, midpoint +1, upper, item)
    else:
        return False

def search_sorted_list(sorted_list,item):
    return rec_list(sorted_list, 0,len(sorted_list)-1, item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(search_sorted_list(testlist, 3))
print(search_sorted_list(testlist, 13))
