# Find the minimal average of any slice containing at least two elements.

A = [4,2,2,5,1,5,8,1,2]

def solution(A):
    min_average_value = (A[0] + A[1]) / 2
    min_average_pos = 0
    
    for i in range(0, len(A)-2):
        this_slice = (A[i] + A[i+1]) / 2
        if this_slice < min_average_value:
            min_average_value = this_slice
            min_average_pos = i
            
        this_slice = (A[i] + A[i+1] + A[i+2]) / 3
        if this_slice < min_average_value:
            min_average_value = this_slice
            min_average_pos = i    
            
    this_slice = (A[-1] + A[-2]) / 2
    if this_slice < min_average_value:
        min_average_value = this_slice
        min_average_pos = len(A)-2
    
    return min_average_pos
    
    
print(solution(A))  
