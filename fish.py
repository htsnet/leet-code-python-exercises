# N voracious fish are moving along a river. Calculate how many fish are alive.

A = [4,3,2,1,5]
B = [0,1,0,0,0]

def solution(A, B):
    alives= len(A)
    stack = []
    
    for i in range(0, len(A)):
        if B[i] ==  1:
            stack.append(A[i])
        else:
            while len(stack):
                if stack[-1] > A[i]:
                    alives -= 1
                    break
                if stack[-1] < A[i]:
                    alives -= 1
                    stack.pop()
        
    return alives
    
print(solution(A,B))    
