import pytest
import numpy as np 
# This function converts a axis angle pair in radians into unit quarternions

def ax2qu(n):
    q=[np.cos(n[3]/2),np.sin(n[3]/2)*n[0],np.sin(n[3]/2)*n[1],np.sin(n[3]/2)*n[2]]
    return q


def test_case1():
    n=[0,0,1,0]
    assert ax2qu(n) == [1,0,0,0]
def test_case2():
    n =[0,0,-1,0.5*np.pi]
    x=np.around(ax2qu(n),7)
    y = np.array([0.7071068,0,0,-0.7071068])
    z = np.array_equal(x,y)
    assert z==True

