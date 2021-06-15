# Determine whether a triangle can be built from a given set of edges.

def solution(A):
    if len(A) < 3:
        return 0
    A.sort()
    for i in range(len(A) - 2):
       if (A[i] + A[i+1] > A[i+2]):
           print(A[i],A[i+1],A[i+2])
           return 1
        
    return 0  
