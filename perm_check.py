# Check whether array A is a permutation.

def solution(A):
    A.sort()
    for i in range(0, len(A)):
        if A[i] != i + 1:
            return 0
        
    return 1
