
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



# other solution
A = [1,2,3,4]

def solution(A):
    start = 1
    array = set(A)

    for i in array:
        if i > start:
            return start
        elif i == start:
            start += 1
            
    return start
    
print(solution(A))  
