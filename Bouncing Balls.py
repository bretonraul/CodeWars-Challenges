def bouncing_ball(h, bounce, window):
    if h<=0 or bounce<=0 or bounce>=1 or window>=h:
        return -1
    cont=0    
    while h>window:
        h=h*bounce
        if h>window:
            cont=cont+2
        else:cont=cont+1
    return cont
