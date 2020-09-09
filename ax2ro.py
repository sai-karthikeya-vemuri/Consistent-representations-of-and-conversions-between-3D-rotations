import numpy as np 
import pytest

#This function takes in axis angle pair in radians and converts it into corresponding rodrigues vector

def ax2ro(n):
    if n[3]==np.pi:
        print("rodrigues vector is not possible as tan(90)=infinity")
    
    n[3]=np.tan(n[3]/2)
    return n

def test_case1():
    n=[0,0,1,0.5*np.pi]
    x=np.around(ax2ro(n),1)

    assert x[3]==1