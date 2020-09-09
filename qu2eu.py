import math
import numpy as np 
import pytest
#This function converts a given quartenion into corresponding euler angles
def qu2eu(q):
    p=-1
    q03=q[0]**2+q[3]**2
    q12=q[1]**2+q[2]**2
    xhi=np.sqrt(q03*q12)
    if q12==0:
        theta = [np.arctan2(-2*p*q[0]*q[3],q[0]**2-q[3]**2),0,0]
    elif q03==0:
        theta = [np.arctan2(2*q[1]*q[2],q[1]**2-q[2]**2),np.pi,0]
    else:
        theta =[np.arctan2((q[1]*q[3]-p*q[0]*q[2])/xhi,(-p*q[0]*q[1]-q[2]*q[3])/xhi),np.arctan2(2*xhi,q03-q12),np.arctan2((p*q[0]*q[2]+q[1]*q[3])/xhi,(q[2]*q[3]-p*q[0]*q[1])/xhi)]
    return theta

print(qu2eu([1,0,0,0]))
def test_case1():
    q=[1,0,0,0]
    theta = np.around(qu2eu(q),1)
    theta_expected = [0,0,0]
    i = np.array_equal(theta_expected,theta)
    assert i==True
def test_case2():
    q=[0.7071068,0,0,0.7071068]
    theta = qu2eu(q)
    theta_expected = [0.5*np.pi,0,0]
    i = np.array_equal(theta_expected,theta)
    assert i==True
