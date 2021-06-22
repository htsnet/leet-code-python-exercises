# Compute the number of intersections in a sequence of discs.

#### This solution is not OK! Must to be improved

A = [1, 5, 2, 1, 4, 0] # result 11 --> OK
A = [1,10,100,1] # result 4 but correct is 5

def solution(A):
    limits = []
    for i in range(len(A)):
        limit_inferior = i - A[i]
        limit_superior = i + A[i]
        limits.append([limit_inferior, limit_superior])
        
    print(limits)
    
    number = 0
    for i in range(len(limits)):
        for j in range(i+1, len(limits)):
            if limits[i][0] >= limits[j][0] or limits[i][1] <= limits[j][1]:
                number += 1
    
    if number > 10_000_000:
        return -1
    
    return number 
    
print(solution(A))   
