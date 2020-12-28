def solution(s):
    result=[]
    
    for x in list(s):
        if x.istitle():
            result += " "
            result += x
        else: result += x
    return ''.join(result)
