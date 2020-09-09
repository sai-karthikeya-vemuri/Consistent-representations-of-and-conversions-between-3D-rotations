import pytest
import numpy as np 
#This function takes a rotation matrix and gives corresponding quaternion
def om2qu(A):
    q0=0.5*np.sqrt(1+A[0][0]+A[1][1]+A[2][2])
    q1=0.5*np.sqrt(1+A[0][0]-A[1][1]-A[2][2])
    q2=0.5*np.sqrt(1-A[0][0]+A[1][1]-A[2][2])
    q3=0.5*np.sqrt(1-A[0][0]-A[1][1]+A[2][2])
    if A[2][1]<A[1][2]:
        q1=-1*q1
    if A[0][2]<A[2][0]:
        q2=-1*q2
    if A[1][0]<A[0][1]:
        q3=-1*q3
    
    v = np.sqrt(q0**2+q1**2+q2**2+q3**2)
    q=[q0/v,q1/v,q2/v,q3/v]
    return q

def test_case1():
    A=np.eye(3)
    assert om2qu(A)==[1,0,0,0]
def test_case2():
    A=np.eye(3)
    A[0][0]=-1
    A[1][1]=-1
    assert om2qu(A)==[0,0,0,1]

