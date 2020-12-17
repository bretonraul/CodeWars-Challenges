number=10
i = 1
y=0
while True:
    i = i + 1
    if i%3==0 or i%5==0:
        y = y+i
    if(i >= number-1):
        break

print(y)
        

