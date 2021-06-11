# Find the earliest time when a frog can jump to the other side of a river.

A = [1]
X = 1

import numpy as np

def checkLimits(position, array):
    if position > 0 and position <= 100_000:
        return True
    return False

def solution(X, A):
    if checkLimits(X, A):
        if len(A) == 0:
            return -1
        elif len(A) == 1 and A[0] != X:
            return -1
        elif len(A) == 1 and A[0] == X:
            return 0
        else:
            missing = []
            for i in range(0, len(A)):
                if A[i] <= X:
                    missing.append(A[i])
            missing = set(missing)
            
            for i in range(0, len(A)):
                if A[i] in missing:
                    missing.remove(A[i])
                    if A[i] == X and len(missing) == 0:
                        return i
            return -1
    else:
        return -1

print(solution(X, A))     
