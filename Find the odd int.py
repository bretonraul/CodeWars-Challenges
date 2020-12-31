def find_it(seq):
    #Start here
    odd=0
    pivot=0
    result=0
    while odd%2==0:
        cont=0
        result=seq[pivot]
        for x in seq:
            if x==result:
                cont=cont+1
        pivot=pivot+1
        odd=cont
        
    return result#final result
