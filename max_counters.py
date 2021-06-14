# Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
# using lazy update to better performance

N = 5
A = [3, 4, 4, 6, 1, 4, 4]

def solution(N, A):
    counters = [0]*N
    max_counter_value = 0
    base_value = 0
    
    for i in A:
        if i <= N:
            counters[i - 1] = max(counters[i-1], base_value) + 1
            max_counter_value = max(counters[i - 1], max_counter_value)
        else:
            base_value = max_counter_value
            
    for i in range(N):
        counters[i] = max(counters[i], base_value)
            
    return counters
    

print(solution(N, A))
