import numpy as np 
#This function takes 3 euler angles in bunge convention in radians and gives a quartenion
def eu2qu(a1,a2,a3):
    c = np.cos(a2/2)
    s=np.sin(a2/2)
    sigma =(a1+a3)/2
    delta = (a1-a3)/2
    p=-1
    q= [0,0,0,0]
    q = [c*np.cos(sigma),-1*p*s*np.cos(delta),-1*p*s*np.sin(delta),-1*p*c*np.sin(sigma)]
    if q[0]<0:
        q= -1*q
    return q

print(eu2qu(0,0.25*np.pi,0))


