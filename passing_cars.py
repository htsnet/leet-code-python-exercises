# Count the number of passing cars on the road.

A = [0,1,0,1,1]

def solution(A):
    if A.count(0) > 
    
    sum_cars = 0
    for i in range(0, len(A)):
        if A[i] != 1:
            for j in range(i + 1, len(A)):
                if A[i] != A[j]:
                    sum_cars += 1
    if sum_cars > 1_000_000_000:
        return -1
    return sum_cars

print(solution(A))    
