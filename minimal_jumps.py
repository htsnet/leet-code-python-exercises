# Count minimal number of jumps from position X to Y.

def checkLimits(number):
    if number >= 1 and number <= 1_000_000_000:
        return True
    return False

def solution(X, Y, D):
    if checkLimits(X) and checkLimits(Y) and checkLimits(D):
        if X <= Y:
            distance = Y - X
            if distance > 0:
                steps = distance // D + bool(distance % D) # divide and round to the next integer
                return steps
            else:
                return 0
            
        else:
            return 0
        
    else:
        return 0

print(solution(10, 85, 30))      
