
def two_sum(nums,target):
    nums_sorted=sorted(nums)
    left=0
    right=len(nums_sorted)-1
    
    while left<right:
        current_sum=nums_sorted[left]+nums_sorted[right]
        if current_sum == target:
            return(nums_sorted[left],nums_sorted[right])
        elif current_sum<target:
            left+=1
        else:
            right-=1
        
        
    return -1
nums=[1,11,14,2,7,13,20]
target=19
result=two_sum(nums,target)
print(result)