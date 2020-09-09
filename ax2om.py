import numpy as np 
import pytest

#This function takes a axis angle pair (radians) as a four element vector and converts it into corresponding rotation matrix 
def ax2om(n):
    c= np.cos(n[3])
    s= np.sin(n[3])
    p=-1
    A=np.zeros((3,3))
    A[0][0]= c + (1-c)*(n[0]**2)
    A[0][1]= (1-c)*n[0]*n[1] + s*n[2]
    A[0][2]= (1-c)*n[0]*n[2] - s*n[1]
    A[1][0]= (1-c)*n[0]*n[1] - s*n[2]
    A[1][1]= c + (1-c)*(n[1]**2)
    A[1][2]= (1-c)*n[2]*n[1] + s*n[0]
    A[2][0]= (1-c)*n[0]*n[2] + s*n[1]
    A[2][1]= (1-c)*n[2]*n[1] - s*n[0]
    A[2][2]= c + (1-c)*(n[2]**2)
    return A

def test_case1():
    n=[0,0,1,0]
    x= np.eye(3)
    y=np.array_equal(ax2om(n),x)
    print(ax2om(n))
    assert y== True 


def test_case2():
    n=[-1,0,0,np.pi]
    x= np.eye(3)
    x[1][1]=-1
    x[2][2]=-1
    y=np.array_equal(np.around(ax2om(n),1),x)
    print(np.around(ax2om(n),2))
    assert y== True 

