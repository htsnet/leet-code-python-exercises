# Compute number of distinct values in an array.

A = [0,1,0,1,1]

def solution(A):
    B = set(A)
    return len(B)

print(solution(A))  
