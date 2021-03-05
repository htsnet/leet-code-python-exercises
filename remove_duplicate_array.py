# Remove Duplicates from Sorted Array

nums = [1,1,2,2,2,2,2,3,3,3,3,4] # change this array for new tests
if len(nums) >= 2:
    i = len(nums) - 1
    #print(i)
    while i >= 1:
        #print('inside while', i)
        if nums[i] == nums[i-1]:
            del nums[i]
        i -= 1
        #print('after', i)
print(nums)
