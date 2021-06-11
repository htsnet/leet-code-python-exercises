# Find the missing element in a given permutation.

A = [1,2,3,5]
print(len(A))



def checkLimits(array):
    if len(array) >= 0 and len(array) <= 100_000:
            return True
    return False

def solution(A):
    if checkLimits(A):
        A.sort()
        if len(A) == 0:
            return 1
        elif A[0] > 1:
            return 1
        elif len(A) == 1:
            return 2
        else:
            last = A[0]
            for i in range(1,len(A)):
                print("compara", last, A[i], i)
                if last + 1 == A[i]:
                    last = A[i]
                else:
                    print("saida", last + 1)
                    return last + 1
            print(last, A[-2])                
            if last == A[-1]:
                return A[-1] + 1
            else:
                return last + 1
    else:
        return 1

print(solution(A))   
