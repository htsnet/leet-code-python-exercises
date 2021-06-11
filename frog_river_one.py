# Find the earliest time when a frog can jump to the other side of a river.

A = [1,3,1,4,2,3,5,4]
X = 5

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
            for i in range(1, X + 1):
                if i <= X:
                    missing.append(i)
            missing = set(missing)
            
            for i in range(0, len(A)):
                if A[i] in missing:
                    missing.remove(A[i])
                    if len(missing) == 0:
                        return i
            return -1
    else:
        return -1

print(solution(X, A))     
