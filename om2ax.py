import math
import pytest
import numpy as np 
from numpy import linalg as LA
#This function takes in the rotation matrix and gives axis angle pair in radians
def om2ax(A):
    p=-1
    w= math.acos(0.5*((A[0][0]+A[1][1]+A[2][2])-1))
    if w==0:
        f = [0,0,1,0]
    else:
        values,vectors= LA.eig(A)
        if values[0]==1:
            vector=vectors[:,0]
        elif values[1]==1:
            vector=vectors[:,1]
        else:
            vector= vectors[:,2]
        if A[2][1]!=A[1][2]:
            vector[0]=sign(p*(A[2][1]-A[1][2]))*abs(vector[0])
        if A[0][2]!=A[2][0]:
            vector[1]=sign(p*(A[0][2]-A[2][0]))*abs(vector[1])
        if A[1][0]!=A[0][1]:
            vector[2]=sign(p*(A[1][0]-A[0][1]))*abs(vector[2])
        f = [vector[0],vector[1],vector[2],w]
    return f




def test_case1():
    A=np.eye(3)
    assert om2ax(A)==[0,0,1,0]


def test_case2():
    A=np.eye(3)
    A[1][1]=-1
    A[2][2]=-1
    assert om2ax(A)==[1,0,0,np.pi]


