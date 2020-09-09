import numpy as np
#This function takes in the three euler angles in the bunge convention in degrees and gives the corresponding axis angle pair the output is of
# form (n,alpha) in degrees 
def eu2ax(a,b,c):
    a= np.pi*a/180
    b= np.pi*b/180
    c= np.pi*c/180
    t=np.tan(b/2)
    sigma=(a+c)/2
    delta=(a-c)/2
    p=-1
    tau=np.sqrt((t*t)+(np.sin(sigma)*np.sin(sigma)))
    alpha=2*np.arctan(tau/np.cos(sigma))
    output = np.zeros((4))
    if alpha <= np.pi:
        output[3]= alpha*180/np.pi
        output[0]= -p*t*np.cos(delta)/tau
        output[1]=-p*t*np.sin(delta)/tau
        output[2]=-p*t*np.sin(sigma)/tau
    else:
        output[3]=360- alpha*180/np.pi
        output[0]= p*t*np.cos(delta)/tau
        output[1]=p*t*np.sin(delta)/tau
        output[2]=p*t*np.sin(sigma)/tau
    return output


print(eu2ax(360,90,180))