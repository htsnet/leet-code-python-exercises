
# Find the smallest positive integer that does not occur in a given sequence.

def solution(A):
    A.sort()
    minimum = 1
    for i in range(0, len(A)):
        if A[i] > 0:
            if A[i] > minimum:
                return minimum
            elif A[i] == minimum:
                minimum += 1
                
            
    return minimum 
