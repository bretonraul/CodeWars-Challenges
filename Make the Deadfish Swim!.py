#Deadfish has 4 commands, each 1 character long:

 #   i increments the value (initially 0)
  #  d decrements the value
   # s squares the value
    #o outputs the value into the return array

#Invalid characters should be ignored.

#parse("iiisdoso")  ==>  [8, 64]
def parse(data):
    value=0
    array=[]
    #Starts here
    for x in data:
        if x=='i':
            value=value+1
        elif x=='d':
            value=value-1
        elif x=='s':
            value=pow(value,2)
        elif x=='o':
            array.append(value)
        
        else:print("Syntax Error")
    return array
