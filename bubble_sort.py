#o(n^2)algo
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]: 
                arr[j],arr[j+1]=arr[j+1],arr[j]
array=[3,4,3,4,5,1,2,3]
bubble_sort(array)
print(array)

