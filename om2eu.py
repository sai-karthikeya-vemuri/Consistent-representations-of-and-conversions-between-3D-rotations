import pytest

import numpy as np 
#This function takes in the rotation matrix and gives euler angles in bunge convention in radians

def om2eu(A):
    if  abs(A[2][2]) != 1:
        xhi= 1/np.sqrt(1-(A[2][2]*A[2][2]))
        theta = [np.arctan2(A[2][0]*xhi,A[2][1]*xhi*-1),np.arccos(A[2][2]),np.arctan2(xhi*A[0][2],xhi*A[1][2])]
    else:
        theta = [np.arctan2(A[0][1],A[0][0]),0.5*np.pi*(1-A[2][2]),0]
    return theta

def test_case1():
    A= np.eye(3)
    assert om2eu(A)== [0,0,0]
  
def test_case2():
    A=np.eye(3)
    A[0][0]=-1
    A[1][1]=-1
    print(A)
    assert om2eu(A)==[2*np.pi,0,np.pi]
def test_case3():
    A= np.zeros((3,3))
    A[0][2]=1
    A[1][1]=-1
    A[2][0]=1
    assert om2eu(A)==[0.5*np.pi,0.5*np.pi,0.5*np.pi]
