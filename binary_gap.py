# Find longest sequence of zeros in binary representation of an integer.

def solution(N):
    if N > 1: 
        binary = bin(N)
        list_numbers = str(binary).split('1')
        del list_numbers[0]
        del list_numbers[-1]
        each_part = []
        for i in list_numbers:
            each_part.append(len(i))

        print(each_part)
        if len(each_part) > 0:
            return max(each_part)
        else:
            return 0
    else:
        return 0
    
print(solution(1041))
