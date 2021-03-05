# Remove Duplicates from Sorted Array

## Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

## Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

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
