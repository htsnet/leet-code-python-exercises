# Find value that occurs in odd number of elements.

# solution 1: more time to large arrays
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

A = [9,3,9,3,9,7,9, 2, 2, 5, 5, 8, 8, 7, 6, 6, 15, 15, 21]    
print(solution(A))   


# solution 2: faster
def checkLimits(array):
    if len(array) >= 1 and len(array) <= 1_000_000 and len(array) % 2 == 1:
        for i in array:
            if i >=1 and i <= 1_000_000_000:
                return True
            else:
                return False
    return False

def solution(A):
    print(A)
    if checkLimits(A):
        while True:
            A.sort()
            print(A)
            i = 0
            while i <= (len(A) - 2):
                print(A[i], A[i+1])
                if A[i] == A[i+1]:
                    i += 2
                    pass
                else:
                    return A[i]
            return A[-1]    
        
        
    else:
        return 0

A = [9,3,9,3,9,7,9, 2, 2, 5, 5, 8, 8, 7, 6, 6, 15, 15, 21]    
print(solution(A))   
   
