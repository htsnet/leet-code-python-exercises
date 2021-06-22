# Determine whether a given string of parentheses (multiple types) is properly nested.

S = "([)()]"
S = "{[()()]}"

def checkPair(left, right):
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True
    if left == '{' and right == '}':
        return True
    return False
    

def solution(S):
    if len(S) == 0:
        return 1
    
    stack = []
    
    for symbol in S:
        if symbol == '[' or symbol == '{' or symbol == '(':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return 0
            last = stack.pop()
            #print(last)
            if not checkPair(last, symbol):
                return 0
            
    if len(stack) != 0:
        return 0
    
    return 1
    
print(solution(S))    
