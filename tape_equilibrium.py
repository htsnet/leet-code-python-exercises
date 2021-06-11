# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

A = [-2,-3,-4,-1]


def checkLimits(array):
    if len(array) >= 0 and len(array) <= 100_000:
            return True
    return False

def solution(A):
    if checkLimits(A):
        if len(A) == 0:
            return 0
        elif len(A) == 1:
            return abs(A[0])
        else: 
            part1 = 0
            part2 = sum(A)
            differences = []
            for i in range(0,len(A) - 1):
                part1 = A[i] + part1
                part2 = part2 - A[i]
                dif = abs(part1 - part2)
                differences.append(dif)
                
            return min(differences)
    else:
        return 0

print(solution(A))  
