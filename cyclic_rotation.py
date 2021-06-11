# Rotate an array to the right by a given number of steps.

def rotate_one(array_received):
    last = array_received[-1]
    for i in range(len(array_received) - 1, 0, -1):
        array_received[i] = array_received[i - 1]
    array_received[0] = last
    return array_received

def solution(array, times):
    if len(array) > 0:
        if times >= 0 and times < 100:
            for i in range (0, times):
                print(array)
                array = rotate_one(array)
            
            return array
    else:
       return []
    

    
print(solution([1], 3))  
