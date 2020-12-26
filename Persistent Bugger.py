num=39
cont=0

while num>=10:
    mult=1
    for x in str(num):
        mult*=int(x)
    num=mult
    cont=cont+1


