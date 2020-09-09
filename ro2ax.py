import numpy as np 
import pytest
import math
 #This function converts given rodrigues vector into axis angle pair (radian)

def ro2ax(r):
     x = np.sqrt(r[0]**2+r[1]**2+r[2]**2)
     n = [r[0]/x,r[1]/x,r[2]/x,2*math.atan(x)]
     return n
    
def test_case1():
    r=[0,0,-1]
    x= np.around(ro2ax(r),1)
    print(x)
    y=[0,0,1,0]
    z=np.array_equal(x,y)
    assert z==True
