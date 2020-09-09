import numpy as np
import scipy
#This function converts given euler angles (Bunge Convention, degrees)into corresponding equivalent rotation matrix
def eu2om(a,b,d):
    
    a= (np.pi)*a/180
    b= (np.pi)*b/180
    d= (np.pi)*d/180


    A=np.zeros((3,3))
    c1=np.cos(a)
    s1=np.sin(a)
    c2=np.cos(d)
    s2=np.sin(d)
    c=np.cos(b)
    s=np.sin(b)
    
    A[0][0]=(c1*c2) - (s1*c*s2)
    A[0][1]=(s1*c2) + (c1*c*s2)
    A[0][2]=s*s2
    A[1][0]=(-c1*s2)-(s1*c*c2)
    A[1][1]=(-s1*s2)+ (c1*c*c2)
    A[1][2]=s*c2
    A[2][0]=s1*s
    A[2][1]=-c1*s
    A[2][2]=c
    return A

print(np.around(eu2om(270,180,0),1))