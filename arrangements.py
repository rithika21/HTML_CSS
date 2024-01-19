# ARRANGEMENT 1 link : https://pastebin.com/izd2qjqv
 #ARRANGEMENT 1: 
def partition(arr, low, high):
    i = low-1   # i elements will be smaller, index of left part
 
    for j in range(low, high):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
 
def alternate_pos_neg(arr):
    n = len(arr)//2
 
    # Partitioning
    pivot_index = partition(arr, 0, len(arr)-1)
 
    neg_idx = 0
    pos_idx = n
 
    while pos_idx < 2*n and neg_idx < n:
        arr[pos_idx], arr[neg_idx] = arr[neg_idx], arr[pos_idx]
        pos_idx += 2
        neg_idx += 2
    
    return arr
 
array = [-1, 2, 3, -4, -5, 6, 7, -2, 9, -10]
print(alternate_pos_neg(array))
 
# ARANGEMENT 2
 
def partition(arr, low, high):
    i = low-1   # i elements will be smaller, index of left part
 
    for j in range(low, high):
        if arr[j]%2 != 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
 
def alternate_odd_even(arr):
    n = len(arr)//2
 
    # Partitioning
    pivot_index = partition(arr, 0, len(arr)-1)
 
    neg_idx = 0
    pos_idx = n
 
    while pos_idx < 2*n and neg_idx < n:
        arr[pos_idx], arr[neg_idx] = arr[neg_idx], arr[pos_idx]
        pos_idx += 2
        neg_idx += 2
    
    return arr
 
array = [3, 4, 1, 1, 6, 8, 10, 11, 9, 10]
print(alternate_odd_even(array))
 
# ARRANGEMENT 3
 
def partition(arr, low, high):
    i = low-1   # i elements will be smaller, index of left part
 
    for j in range(low, high):
        if arr[j] != 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
 
def alternate_odd_even(arr):
    n = len(arr)//2
 
    # Partitioning
    pivot_index = partition(arr, 0, len(arr)-1)
 
    # neg_idx = 0
    # pos_idx = n
 
    # while pos_idx < 2*n and neg_idx < n:
    #     arr[pos_idx], arr[neg_idx] = arr[neg_idx], arr[pos_idx]
    #     pos_idx += 2
    #     neg_idx += 2
    
    return arr
 
array = [3, 0, 1, 0, 6, 0, 10, 11, 0, 10]
print(alternate_odd_even(array))
