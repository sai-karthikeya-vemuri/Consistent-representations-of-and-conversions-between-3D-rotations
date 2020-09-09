import math
import numpy as np 
import pytest
#This function converts quarternion into axis angle pair in radians
def qu2ax(q):
    w=2*math.acos(q[0])
    if w==0:
        n=[0,0,1,0]
    elif q[0]==0:
        n=[q[1],q[2],q[3],np.pi]
    elif q[0]>0:
        s = 1/np.sqrt(q[1]**2+q[2]**2+q[3]**2)
        n = [s*q[1],s*q[2],s*q[3],w]
    else:
        s = -1/np.sqrt(q[1]**2+q[2]**2+q[3]**2)
        n = [s*q[1],s*q[2],s*q[3],w]
    return n
def test_case1():
    x = qu2ax([1,0,0,0])
    y = [0,0,1,0]
    i = np.array_equal(x,y)
    assert i == True
def test_case2():
    x = qu2ax([0,0,0,1])
    y = [0,0,1,np.pi]
    i = np.array_equal(x,y)
    assert i == True