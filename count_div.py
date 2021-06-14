# Compute number of integers divisible by k in range [a..b].

A = 0
B = 0
K = 11

def solution(A, B, K):
    
    if A == B:
        if B % K == 0:
            return 1
        else:
            return 0
    if K > B:
        return 0        
    first = A
    for i in range(A, B):
        if i % K == 0:
            first = i
            break
            
    return ((B - first + 1) // K) + bool ((B - first + 1) % K)
            
                
    
    
    
print(solution(A, B, K))   
