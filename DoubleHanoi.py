# Find the maximum number of disks that can be placed on two rods. The disks should be in decreasing order of size on the first rod and in increasing order of size on the second rod.

A = [2,3,3,4]
L = 3
R = 1


A = [1,1,1,1]
L = 1
R = 1

def solution(A, L, R):
    count = 0
    
    A.sort()
   
    lastL = -1
    lastR = -1
    for i in A:
        if lastL != i and i < L:
            lastL = i
            count += 1

        elif lastR != i and i > R:
            lastR = i
            count += 1
          
    
    return count
    
print(solution(A, L, R))    
