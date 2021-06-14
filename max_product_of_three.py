# Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

def solution(A):
    A.sort()
    try1 = A[-1] * A[-2] * A[-3]
    try2 = A[-1] * A[0] * A[1]
    return max(try1, try2)
