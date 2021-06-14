# Find the minimal nucleotide from a range of sequence DNA.

def solution(S, P, Q):
    response = []
    for i in range(0, len(P)):
        cut = S[P[i] : Q[i] + 1]
        if cut.find("A") != -1:
            response.append(1)
        elif cut.find("C") != -1:
            response.append(2)
        elif cut.find("G") != -1:
            response.append(3)
        else:
            response.append(4)
        
        
    return response
