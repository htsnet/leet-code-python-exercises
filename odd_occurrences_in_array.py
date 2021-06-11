# Find value that occurs in odd number of elements.

def checkLimits(array):
    if len(array) >= 1 and len(array) <= 1_000_000 and len(array) % 2 == 1:
        for i in array:
            if i >=1 and i <= 1_000_000_000:
                return True
            else:
                return False
    return False

def solution(A):
    if checkLimits(A):
        while True:
            last_number = A[-1]
            del A[-1]
            try:
                index = A.index(last_number)
                del A[index]
            except:
                return last_number
                
        
        
    else:
        return 0

print(solution([2,3,3,4]))   
