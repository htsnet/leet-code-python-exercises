# Compute number of inversion in an array.

A = [-1,6,3,4,7,4]

def solution(A):
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if i < j and A[j] < A[i]:
                #print(A[j], A[i])
                count +=1
                if count > 1_000_000_000:
                    return -1
            
    return count
    
    
    
print(solution(A))   
